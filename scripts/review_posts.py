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

def get_hunk_lines(patch):
    """
    Parses a git patch string and returns a set of valid line numbers 
    (lines present in the new version of the file that are part of the diff hunks).
    """
    if not patch:
        return set()
        
    valid_lines = set()
    # Regex to match hunk headers: @@ -old_start,old_len +new_start,new_len @@
    hunk_header_pattern = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")
    current_line_number = 0
    
    lines = patch.split('\n')
    
    for line in lines:
        if line.startswith('@@'):
            match = hunk_header_pattern.match(line)
            if match:
                start_line = int(match.group(1))
                current_line_number = start_line
            continue
            
        if line.startswith('-'):
            continue
            
        if line.startswith('+') or line.startswith(' '):
            valid_lines.add(current_line_number)
            current_line_number += 1
            
    return valid_lines

def review_text_json(text):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not found.")
        return None
    
    genai.configure(api_key=api_key)
    
    # Prioritize gemini-flash-latest as requested
    model_names = ['gemini-flash-latest', 'gemini-2.0-flash', 'gemini-pro-latest']
    
    numbered_text = add_line_numbers(text)
    
    # Improved Prompt
    prompt = """
    You are a professional editor reviewing a blog post.
    The content below has line numbers added to the beginning of each line (e.g., "10: ...").
    
    **Goal:** Identify objective errors in spelling, grammar, and punctuation.
    
    **Guidelines:**
    1.  **Maintain Author's Voice:** Do NOT suggest stylistic changes unless the phrasing is confusing or grammatically incorrect. Respect the author's tone.
    2.  **Ignore Code:** Do NOT review or correct content inside code blocks (fenced with ```).
    3.  **Ignore Frontmatter:** Ignore the Hugo frontmatter (metadata between the first two '---' separators).
    4.  **Be Concise:** Keep explanations short and direct.
    
    **Output Format:**
    Return a **JSON list** of objects. Each object must have:
    - `"line"`: (Integer) The line number where the issue is found.
    - `"original"`: (String) The exact text being corrected.
    - `"suggestion"`: (String) The fully corrected text for that line.
    - `"explanation"`: (String) A brief explanation of the error.
    
    **Example:**
    [
        {
            "line": 42,
            "original": "Thier is a error.",
            "suggestion": "There is an error.",
            "explanation": "Spelling correction ('Thier' -> 'There')."
        }
    ]
    
    If no issues are found, return an empty list: `[]`.
    Output **ONLY** valid JSON. Do not use markdown code blocks (```json) if possible, but if you do, the script will handle it.
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
            elif text_response.startswith("```"):
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
            is_changed = file.status in ["added", "modified", "renamed"]
            
            if is_post and is_markdown and is_changed:
                print(f"Processing {file.filename} (Status: {file.status})...")
                
                try:
                    if not os.path.exists(file.filename):
                        print(f"File {file.filename} not found locally. Skipping.")
                        continue

                    # Parse valid lines from patch
                    valid_lines = get_hunk_lines(file.patch)
                    if not valid_lines:
                         print(f"No patch info (valid diff hunks) found for {file.filename}. This might mean the file is binary or too large, or no textual changes.")
                         # If we can't determine valid lines, we skip to avoid API errors
                         continue
                        
                    with open(file.filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if not content.strip():
                        continue

                    review_data = review_text_json(content)
                    
                    if review_data:
                        for item in review_data:
                            try:
                                line_num = int(item.get("line"))
                            except (ValueError, TypeError):
                                print(f"Invalid line number in response: {item.get('line')}")
                                continue

                            suggestion = item.get("suggestion")
                            explanation = item.get("explanation")
                            
                            if line_num and suggestion:
                                # Check if line is within the diff
                                if line_num not in valid_lines:
                                    print(f"Skipping comment on line {line_num} (outside of diff hunks).")
                                    continue

                                body = f"{explanation}\n```suggestion\n{suggestion}\n```"
                                
                                draft_comments.append({
                                    "path": file.filename,
                                    "line": line_num,
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
                    commit_obj = repo.get_commit(pr.head.sha)
                    pr.create_review(
                        commit=commit_obj,
                        body="Gemini Automated Review",
                        event="COMMENT",
                        comments=draft_comments
                    )
                    print("Review comments posted successfully.")
                except Exception as e:
                    print(f"Failed to post review comments: {e}")
                    # Fallback: Print comments to log if API fails
                    print("Draft comments were:")
                    print(json.dumps(draft_comments, indent=2))
        else:
            print("No applicable files to review or no issues found in changed lines.")
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
