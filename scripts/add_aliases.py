import os
import re
import glob

def add_aliases_to_posts(posts_dir):
    md_files = glob.glob(os.path.join(posts_dir, "**/*.md"), recursive=True)
    
    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if it already has aliases
        if "aliases =" in content:
            continue
            
        # Extract date and slug from front matter
        date_match = re.search(r'date = "(\d{4})-(\d{2})-\d{2}T', content)
        slug_match = re.search(r'slug = "(.*?)"', content)
        
        if date_match and slug_match:
            year = date_match.group(1)
            month = date_match.group(2)
            slug = slug_match.group(1)
            
            # The old URL format
            alias_path = f"/{year}/{month}/{slug}.html"
            
            # Insert aliases right before the second '+++'
            parts = content.split('+++', 2)
            if len(parts) >= 3:
                front_matter = parts[1]
                
                # Check if draft is there, insert after it or just before the closing +++
                if "draft =" in front_matter:
                     front_matter = front_matter.replace('draft = false', f'draft = false\naliases = ["{alias_path}"]')
                     front_matter = front_matter.replace('draft = true', f'draft = true\naliases = ["{alias_path}"]')
                else:
                     front_matter = front_matter + f'aliases = ["{alias_path}"]\n'
                
                new_content = parts[0] + '+++' + front_matter + '+++' + parts[2]
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                    
    print(f"Processed {len(md_files)} files.")

if __name__ == "__main__":
    posts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "keithrozario_blog", "content", "posts")
    add_aliases_to_posts(posts_dir)
