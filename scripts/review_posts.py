import os
import sys
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

def review_text(text):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not found.")
        return None
    
    genai.configure(api_key=api_key)
    
    # Try gemini-2.0-flash first, then fallback
    model_names = ['gemini-2.0-flash', 'gemini-flash-latest', 'gemini-pro-latest']
    
    default_prompt = """
    You are a professional editor. Please review the following blog post markdown content for grammar, spelling, and punctuation errors.
    
    Focus on:
    - Typographical errors.
    - Grammatical mistakes.
    - Punctuation issues.
    
    Do NOT focus on:
    - Style or tone (unless it's egregious).
    - Code blocks (ignore content within fenced code blocks).
    
    Format your response as a markdown list of specific issues found, referencing the approximate location or context if possible.
    If no issues are found, simply say "No issues found."
    """
    
    base_prompt = os.environ.get("GEMINI_PROMPT", default_prompt)
    full_prompt = f"{base_prompt}\n\nContent:\n{text}"

    for model_name in model_names:
        print(f"Trying model: {model_name}...")
        model = genai.GenerativeModel(model_name)
        try:
            response = model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            print(f"Error calling Gemini API with {model_name}: {e}")
            error_str = str(e).lower()
            if "404" in error_str or "not found" in error_str or "429" in error_str or "quota" in error_str or "limit" in error_str:
                continue # Try next model
            else:
                return None # Other error, stop trying

    # If all failed
    print("All models failed.")
    try:
        print("Available models:")
        for m in genai.list_models():
            print(f"- {m.name}")
    except Exception as e:
        print(f"Could not list models: {e}")
        
    return None

def main():
    # Ensure we are at repo root
    if os.path.basename(os.getcwd()) == "scripts":
        os.chdir("..")

    github_token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    pr_number = os.environ.get("PR_NUMBER")

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
        
        files = get_pr_files(g, repo_name, pr_number)
        
        comments = []
        
        for file in files:
            # Robust filtering:
            # 1. Must be in the posts directory.
            # 2. Must be a markdown file.
            # 3. Must be added or modified (not deleted or renamed without modification).
            is_post = file.filename.startswith("keithrozario_blog/content/posts/")
            is_markdown = file.filename.endswith(".md")
            is_changed = file.status in ["added", "modified"]
            
            if is_post and is_markdown and is_changed:
                print(f"Processing {file.filename} (Status: {file.status})...")
                
                try:
                    # Check if file exists locally (it should after checkout)
                    if not os.path.exists(file.filename):
                        print(f"File {file.filename} not found locally. Skipping.")
                        continue
                        
                    with open(file.filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if not content.strip():
                        print(f"File {file.filename} is empty. Skipping.")
                        continue

                    review = review_text(content)
                    
                    if review:
                        comments.append(f"## Review for `{file.filename}`\n\n{review}")
                    else:
                        print(f"No review generated for {file.filename}.")
                        
                except Exception as e:
                    print(f"Error processing file {file.filename}: {e}")
                    continue
            else:
                 # verbose logging for skipped files if needed, currently silent to avoid noise
                 pass

        if comments:
            repo = g.get_repo(repo_name)
            pr = repo.get_pull(pr_number)
            full_comment = "# Blog Post Review (Gemini)\n\n" + "\n\n---\n\n".join(comments)
            
            if os.environ.get("DRY_RUN", "").lower() == "true":
                print("\n[DRY RUN] Generated Comment:\n")
                print(full_comment)
            else:
                pr.create_issue_comment(full_comment)
                print("Review posted successfully.")
        else:
            print("No applicable files to review or no issues found.")
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
