import sys
import os
import shutil

def generate_page(from_path, template_path, dest_path, basepath="/"):
    # Read the template and markdown files
    with open(template_path, 'r') as f:
        template = f.read()
    
    with open(from_path, 'r') as f:
        content = f.read()
    
    # Replace placeholders
    html = template.replace("{{ Content }}", content)
    html = html.replace("{{ Title }}", "My Static Site")
    
    # Replace relative paths with basepath
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')
    
    # Write the final HTML
    with open(dest_path, 'w') as f:
        f.write(html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    # Ensure destination directory exists
    os.makedirs(dest_dir_path, exist_ok=True)
    
    # Process each file in the content directory
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        
        if os.path.isfile(from_path):
            if filename.endswith('.html'):
                # Generate HTML page
                generate_page(from_path, template_path, dest_path, basepath)
            else:
                # Copy other files as-is
                shutil.copy(from_path, dest_path)
        elif os.path.isdir(from_path):
            # Recursively process subdirectories
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

def main():
    # Get basepath from command line argument or default to "/"
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    
    # Define paths
    content_dir = "content"
    template_path = "template.html"
    docs_dir = "docs"
    
    # Clean the docs directory
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    
    # Generate the site
    generate_pages_recursive(content_dir, template_path, docs_dir, basepath)
    
    print(f"Site built successfully in {docs_dir} directory with basepath: {basepath}")

if __name__ == "__main__":
    main()
