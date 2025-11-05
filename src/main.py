#!/usr/bin/env python3
import os
import shutil
from markdown_converter import convert_markdown_to_html, extract_title

def generate_page(from_path, template_path, dest_path):
    """Generate HTML page from markdown using template"""
    print(f"  Generating: {os.path.basename(from_path)} -> {os.path.basename(dest_path)}")
    
    try:
        # Read markdown file
        with open(from_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Extract title
        title = extract_title(markdown_content)
        
        # Convert markdown to HTML
        html_content = convert_markdown_to_html(markdown_content)
        
        # Read template
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        # Apply template
        final_html = template_content.replace("{{ Title }}", title)
        final_html = final_html.replace("{{ Content }}", html_content)
        
        # Create destination directory
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        # Write file
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
            
        return True
        
    except Exception as e:
        print(f"    ✗ Error: {e}")
        return False

def main():
    print("Static Site Generator")
    print("=" * 40)
    
    # Define paths
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(project_root, "static")
    public_dir = os.path.join(project_root, "public")
    template_file = os.path.join(project_root, "templates", "template.html")
    
    print(f"Project: {os.path.basename(project_root)}")
    
    # Step 1: Clean and create public directory
    print("\n1. Setting up public directory...")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
        print("  ✓ Cleaned existing directory")
    
    os.makedirs(public_dir)
    print("  ✓ Created public directory")
    
    # Step 2: Copy static files
    print("\n2. Copying static files...")
    if os.path.exists(static_dir):
        shutil.copytree(static_dir, public_dir, dirs_exist_ok=True)
        print("  ✓ Static files copied")
    else:
        print("  ✗ Static directory not found")
        return 1
    
    # Step 3: Generate all HTML pages
    print("\n3. Generating HTML pages...")
    
    # Define all pages to generate
    pages = [
        ("content/index.md", "public/index.html"),
        ("content/blog/glorfindel/index.md", "public/blog/glorfindel/index.html"),
        ("content/blog/tom/index.md", "public/blog/tom/index.html"),
        ("content/blog/majesty/index.md", "public/blog/majesty/index.html"),
        ("content/contact/index.md", "public/contact/index.html"),
    ]
    
    success_count = 0
    for from_path, dest_path in pages:
        full_from_path = os.path.join(project_root, from_path)
        full_dest_path = os.path.join(project_root, dest_path)
        
        if generate_page(full_from_path, template_file, full_dest_path):
            success_count += 1
            print(f"    ✓ {os.path.basename(from_path)}")
        else:
            print(f"    ✗ {os.path.basename(from_path)}")
    
    print(f"  Generated {success_count}/{len(pages)} pages")
    
    if success_count == len(pages):
        print("\n" + "=" * 40)
        print("✓ SITE GENERATION COMPLETE!")
        print("\nGenerated pages:")
        print("  - / (Home)")
        print("  - /blog/glorfindel/")
        print("  - /blog/tom/")
        print("  - /blog/majesty/")
        print("  - /contact/")
        print("\nStart server with: cd public && python3 -m http.server 8888")
        return 0
    else:
        print("\n✗ Some pages failed to generate")
        return 1

if __name__ == "__main__":
    exit(main())
