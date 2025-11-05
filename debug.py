import os
import shutil
from pathlib import Path

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively crawl through content directory and generate HTML pages
    from all markdown files found.
    """
    print(f"Searching for markdown files in: {dir_path_content}")
    
    # Ensure destination directory exists
    Path(dest_dir_path).mkdir(parents=True, exist_ok=True)

    # Walk through all files and directories in content path
    for root, dirs, files in os.walk(dir_path_content):
        print(f"Checking directory: {root}")
        print(f"Files found: {files}")
        for file in files:
            if file.endswith('.md'):
                print(f"Found markdown file: {file}")
                # Get full path to the markdown file
                md_path = os.path.join(root, file)

                # Calculate relative path from content directory
                relative_path = os.path.relpath(root, dir_path_content)
                if relative_path == '.':
                    relative_path = ''

                # Determine output HTML filename and path
                html_filename = file.replace('.md', '.html')
                html_output_path = os.path.join(dest_dir_path, relative_path, html_filename)
                print(f"Will generate: {html_output_path}")

                # Ensure the output directory exists
                os.makedirs(os.path.dirname(html_output_path), exist_ok=True)

                # Generate the HTML page
                generate_page(md_path, template_path, html_output_path)
                print(f"Generated: {html_output_path}")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read markdown file
    with open(from_path, 'r') as md_file:
        markdown_content = md_file.read()
    
    # Read template file
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()
    
    # Convert markdown to HTML
    html_content = markdown_to_html(markdown_content)
    
    # Replace template placeholders
    title = extract_title(markdown_content)
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    
    # Write the final HTML file
    with open(dest_path, 'w') as html_file:
        html_file.write(final_html)

def copy_dir(src, dest):
    """Copy directory recursively from src to dest"""
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)

def markdown_to_html(markdown):
    """Convert markdown to HTML"""
    import re
    # Convert headers
    html = re.sub(r'^# (.*)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
    # Convert paragraphs
    html = re.sub(r'^(?!<h1>)(.+)$', r'<p>\1</p>', html, flags=re.MULTILINE)
    return html

def extract_title(markdown):
    """Extract title from markdown (first h1 header)"""
    import re
    match = re.search(r'^# (.*)$', markdown, re.MULTILINE)
    if match:
        return match.group(1)
    return "Default Title"

def main():
    # Clear and recreate public directory
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    
    # Copy static assets
    copy_dir("static", "public")
    
    # Generate pages recursively from all markdown files in content directory
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
