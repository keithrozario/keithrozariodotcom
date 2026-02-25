import os
import sys
import json
import re
import google.generativeai as genai
from github import Github

def get_pr_files(g, repo_name, pr_number):
    try:
        repo = g.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        return pr.get_files()
    except Exception as e:
        print(f"Error fetching PR files: {e}")
        return []

def add_line_numbers(text):
    lines = text.splitlines()
    numbered_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]
    return "\n".join(numbered_lines)

def review_text_json(text):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not found.")
        return None
    
    genai.configure(api_key=api_key)
    
    model_names = ['gemini-2.0-flash', 'gemini-flash-latest', 'gemini-pro-latest']
    
    numbered_text = add_line_numbers(text)
    
    # Prompt explicitly asking for JSON
    prompt = """
    You are a professional editor reviewing a blog post.
    The content below has line numbers added to the beginning of each line (e.g., "10: ...").
    
    Please review the content for:
    - Spelling mistakes.
    - Grammatical errors.
    - Punctuation issues.
    - Awkward phrasing.
    
    Ignore the Hugo frontmatter (content enclosed by the first two '---' separators at the start of the file).
    
    Return your review as a JSON list of objects. Each object must have:
    - "line": The integer line number where the issue is found.
    - "original": The exact text of the line (or part of it) being corrected.
    - "suggestion": The full corrected text for that line (or lines).
    - "explanation": A brief explanation of the issue.
    
    Example output format:
    [
        {
            "line": 10,
            "original": "Thier is a error.",
            "suggestion": "There is an error.",
            "explanation": "Corrected spelling of 'There' and grammar."
        }
    ]
    
    If no issues are found, return an empty list: []
    Do NOT output markdown formatting (like ```json), just the raw JSON if possible, or wrap in ```json block.
    """
    
    full_prompt = f"{prompt}\n\nContent:\n{numbered_text}"

    for model_name in model_names:
        print(f"Trying model: {model_name}...")
        model = genai.GenerativeModel(model_name)
        try:
            response = model.generate_content(full_prompt)
            # Try to extract JSON from response
            text_response = response.text.strip()
            
            # Remove markdown code block if present
            if text_response.startswith("```json"):
                text_response = text_response[7:]
            if text_response.startswith("```"):
                text_response = text_response[3:]
            if text_response.endswith("```"):
                text_response = text_response[:-3]
                
            text_response = text_response.strip()
            
            return json.loads(text_response)
            
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {model_name}: {e}. Response was: {response.text[:100]}...")
            continue # Try next model or fail
            
        except Exception as e:
            print(f"Error calling Gemini API with {model_name}: {e}")
            error_str = str(e).lower()
            if "404" in error_str or "not found" in error_str or "429" in error_str or "quota" in error_str or "limit" in error_str:
                continue 
            else:
                return None 

    print("All models failed.")
    return None

def main():
    # Ensure we are at repo root
    if os.path.basename(os.getcwd()) == "scripts":
        os.chdir("..")

    github_token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    pr_number = os.environ.get("PR_NUMBER")
    dry_run = os.environ.get("DRY_RUN", "").lower() == "true"

    if not all([github_token, repo_name, pr_number]):
        print("Missing environment variables: GITHUB_TOKEN, GITHUB_REPOSITORY, or PR_NUMBER.")
        sys.exit(1)

    try:
        pr_number = int(pr_number)
    except ValueError:
        print("Invalid PR_NUMBER.")
        sys.exit(1)

    try:
        g = Github(github_token)
        print(f"Reviewing PR #{pr_number} in {repo_name}")
        
        repo = g.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        files = pr.get_files()
        
        draft_comments = []
        
        for file in files:
            is_post = file.filename.startswith("keithrozario_blog/content/posts/")
            is_markdown = file.filename.endswith(".md")
            is_changed = file.status in ["added", "modified"]
            
            if is_post and is_markdown and is_changed:
                print(f"Processing {file.filename} (Status: {file.status})...")
                
                try:
                    if not os.path.exists(file.filename):
                        print(f"File {file.filename} not found locally. Skipping.")
                        continue
                        
                    with open(file.filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if not content.strip():
                        continue

                    review_data = review_text_json(content)
                    
                    if review_data:
                        for item in review_data:
                            line_num = item.get("line")
                            suggestion = item.get("suggestion")
                            explanation = item.get("explanation")
                            
                            if line_num and suggestion:
                                body = f"{explanation}\n```suggestion\n{suggestion}\n```"
                                
                                # Use PyGithub's structure for create_review comments
                                # Note: 'line' parameter requires the file to be part of the review.
                                # Review comments must be on lines part of the diff? 
                                # For 'added' files, all lines are new. For 'modified', only changed lines.
                                # If we comment on a line not in the diff, create_review might fail or ignore it.
                                # We'll try. If it fails, we might need fallback.
                                
                                draft_comments.append({
                                    "path": file.filename,
                                    "line": int(line_num),
                                    "body": body
                                })
                    else:
                        print(f"No review generated for {file.filename}.")
                        
                except Exception as e:
                    print(f"Error processing file {file.filename}: {e}")
                    continue

        if draft_comments:
            if dry_run:
                print("\n[DRY RUN] Generated Review Comments:\n")
                print(json.dumps(draft_comments, indent=2))
            else:
                try:
                    # Post a PR review with all comments
                    pr.create_review(
                        commit=pr.head.sha,
                        body="Gemini Automated Review",
                        event="COMMENT",
                        comments=draft_comments
                    )
                    print("Review comments posted successfully.")
                except Exception as e:
                    print(f"Failed to post review comments: {e}")
                    # Fallback? Maybe post as issue comment if review fails
        else:
            print("No applicable files to review or no issues found.")
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
