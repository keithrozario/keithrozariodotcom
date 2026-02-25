import xml.etree.ElementTree as ET
import os
import re
import json
import hashlib
from datetime import datetime

# Namespaces for parsing
namespaces_decl = 'xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:wfw="http://wellformedweb.org/CommentAPI/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:wp="http://wordpress.org/export/1.2/"'
namespaces = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/',
    'dc': 'http://purl.org/dc/elements/1.1/'
}

def parse_comments(xml_file, output_base_dir):
    print(f"Reading {xml_file}...")
    try:
        with open(xml_file, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Find all items
    item_pattern = re.compile(r'<item>(.*?)</item>', re.DOTALL)
    items = item_pattern.findall(content)
    
    print(f"Found {len(items)} items. Scanning for comments...")
    
    comment_count = 0
    post_count = 0

    for i, item_content in enumerate(items):
        wrapped_content = f'<root {namespaces_decl}><item>{item_content}</item></root>'
        
        try:
            root = ET.fromstring(wrapped_content)
            item = root.find('item')
            
            # Get Post Info
            title_elem = item.find('title')
            title = title_elem.text if title_elem is not None else "Untitled"
            if title is None: title = "Untitled"
            
            post_name_elem = item.find('wp:post_name', namespaces)
            if post_name_elem is not None and post_name_elem.text:
                post_slug = post_name_elem.text
            else:
                post_slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

            # Extract Comments
            comments = item.findall('wp:comment', namespaces)
            if not comments:
                continue
                
            post_dir = os.path.join(output_base_dir, post_slug)
            if not os.path.exists(post_dir):
                os.makedirs(post_dir)
            
            for comment in comments:
                comment_id = comment.find('wp:comment_id', namespaces).text
                author = comment.find('wp:comment_author', namespaces).text
                author_email = comment.find('wp:comment_author_email', namespaces).text
                author_url = comment.find('wp:comment_author_url', namespaces).text
                comment_date = comment.find('wp:comment_date', namespaces).text
                comment_content = comment.find('wp:comment_content', namespaces).text
                comment_approved = comment.find('wp:comment_approved', namespaces).text
                
                # Skip unapproved comments or pingbacks/trackbacks if desired
                if comment_approved != '1':
                    continue
                
                # Generate Gravatar hash
                email_hash = hashlib.md5(author_email.lower().encode('utf-8')).hexdigest() if author_email else ""

                data = {
                    "id": comment_id,
                    "author": author,
                    "email_hash": email_hash,
                    "url": author_url,
                    "date": comment_date,
                    "content": comment_content
                }
                
                # Save as JSON
                file_name = f"comment-{comment_id}.json"
                file_path = os.path.join(post_dir, file_name)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    
                comment_count += 1
            
            post_count += 1
            
        except ET.ParseError:
            continue
        except Exception as e:
            print(f"Error processing item {i}: {e}")
            continue

    print(f"Migration complete. Extracted {comment_count} comments across {post_count} posts.")

if __name__ == "__main__":
    xml_file = "keithrozariocom.WordPress.2026-02-13.xml"
    output_dir = "keithrozario_blog/data/comments"
    parse_comments(xml_file, output_dir)
