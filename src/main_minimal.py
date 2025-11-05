#!/usr/bin/env python3
import os
import shutil

def extract_title(markdown):
    """Simple title extractor"""
    lines = markdown.split('\n')
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('# ') and len(stripped_line) > 2:
            return stripped_line[1:].strip()
    return "Untitled"

def copy_static_files():
    """Copy static files"""
    static_dir = "../static"
    public_dir = "../public"
    
    if not os.path.exists(static_dir):
        return False
    
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    
    shutil.copytree(static_dir, public_dir)
    return True

def generate_simple_page():
    """Generate a simple page without complex markdown processing"""
    # Read content
    with open("../content/index.md", "r") as f:
        content = f.read()
    
    # Read template
    with open("../templates/template.html", "r") as f:
        template = f.read()
    
    # Extract title
    title = extract_title(content)
    
    # Simple content (for now)
    html_content = f"<h1>{title}</h1><p>Content would go here</p>"
    
    # Apply template
    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    
    # Write file
    os.makedirs("../public", exist_ok=True)
    with open("../public/index.html", "w") as f:
        f.write(final_html)
    
    return True

def main():
    print("Minimal Static Site Generator")
    
    if copy_static_files() and generate_simple_page():
        print("✓ Site generated successfully!")
        return 0
    else:
        print("✗ Site generation failed!")
        return 1

if __name__ == "__main__":
    exit(main())
