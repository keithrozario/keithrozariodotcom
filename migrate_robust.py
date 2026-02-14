import xml.etree.ElementTree as ET
import os
import re
import html
from datetime import datetime

# Namespaces for parsing
namespaces_decl = 'xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:wfw="http://wellformedweb.org/CommentAPI/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:wp="http://wordpress.org/export/1.2/"'
namespaces = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/',
    'dc': 'http://purl.org/dc/elements/1.1/'
}

def parse_wordpress_xml_robust(xml_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

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
    
    print(f"Found {len(items)} items. Processing...")
    
    success_count = 0
    fail_count = 0
    
    newline = chr(10)

    for i, item_content in enumerate(items):
        wrapped_content = f'<root {namespaces_decl}><item>{item_content}</item></root>'
        
        try:
            root = ET.fromstring(wrapped_content)
            item = root.find('item')
            
            post_type_elem = item.find('wp:post_type', namespaces)
            if post_type_elem is None: continue
            post_type = post_type_elem.text
            
            if post_type not in ['post', 'page']: continue
            if item.find('wp:status', namespaces).text != 'publish': continue

            title_elem = item.find('title')
            title = title_elem.text if title_elem is not None else "Untitled"
            if title is None: title = "Untitled"
            # ESCAPE QUOTES FOR TOML
            title = title.replace('"', '\\"')
                
            post_name_elem = item.find('wp:post_name', namespaces)
            if post_name_elem is not None and post_name_elem.text:
                post_name = post_name_elem.text
            else:
                post_name = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
                
            post_date_elem = item.find('wp:post_date', namespaces)
            if post_date_elem is not None:
                try:
                    date_obj = datetime.strptime(post_date_elem.text, '%Y-%m-%d %H:%M:%S')
                    date_str = date_obj.isoformat()
                except:
                    date_str = datetime.now().isoformat()
            else:
                date_str = datetime.now().isoformat()
                
            content_elem = item.find('content:encoded', namespaces)
            post_content = content_elem.text if content_elem is not None else ""
            if post_content is None: post_content = ""
                
            post_content = re.sub(r'src=".*?(?:wp-content/uploads|files)/(.*?)"', r'src="/uploads/\1"', post_content)
            post_content = re.sub(r'href=".*?(?:wp-content/uploads|files)/(.*?)"', r'href="/uploads/\1"', post_content)
            
            tags = []
            categories = []
            for cat in item.findall('category'):
                domain = cat.get('domain')
                if cat.text:
                    if domain == 'post_tag': tags.append(cat.text)
                    elif domain == 'category': categories.append(cat.text)
                    
            fm_lines = []
            fm_lines.append("+++")
            fm_lines.append(f'title = "{title}"')
            fm_lines.append(f'date = "{date_str}"')
            fm_lines.append('draft = false')
            if tags: fm_lines.append(f'tags = {tags}')
            if categories: fm_lines.append(f'categories = {categories}')
            fm_lines.append("+++")
            fm_lines.append("")
            
            front_matter = newline.join(fm_lines)
            
            file_path = os.path.join(output_dir, f"{post_name}.md")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(front_matter)
                f.write(newline)
                f.write(post_content)
            
            success_count += 1
            
        except ET.ParseError as e:
            fail_count += 1
            continue
        except Exception as e:
            fail_count += 1
            continue

    print(f"Migration complete. Success: {success_count}, Failed: {fail_count}")

if __name__ == "__main__":
    xml_file = "keithrozariocom.WordPress.2026-02-13.xml"
    output_dir = "keithrozario_blog/content/posts"
    parse_wordpress_xml_robust(xml_file, output_dir)
