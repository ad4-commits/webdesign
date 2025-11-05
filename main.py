kimport os
import shutil
import sys
from pathlib import Path

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path="/"):
    """
    Recursively crawl through content directory and generate HTML pages
    from all markdown files found.
    """
    # Ensure destination directory exists
    Path(dest_dir_path).mkdir(parents=True, exist_ok=True)

    # Walk through all files and directories in content path
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                # Get full path to the markdown file
                md_path = os.path.join(root, file)

                # Calculate relative path from content directory
                relative_path = os.path.relpath(root, dir_path_content)
                if relative_path == '.':
                    relative_path = ''

                # Determine output HTML filename and path
                html_filename = file.replace('.md', '.html')
                html_output_path = os.path.join(dest_dir_path, relative_path, html_filename)

                # Ensure the output directory exists
                os.makedirs(os.path.dirname(html_output_path), exist_ok=True)

                # Generate the HTML page
                generate_page(md_path, template_path, html_output_path, base_path)
                print(f"Generated: {html_output_path}")

def generate_page(from_path, template_path, dest_path, base_path="/"):
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
    
    # Replace base path in href and src attributes
    final_html = final_html.replace('href="/', f'href="{base_path}')
    final_html = final_html.replace('src="/', f'src="{base_path}')
    
    # Write the final HTML file
    with open(dest_path, 'w') as html_file:
        html_file.write(final_html)

# ... (keep all your other functions the same: copy_dir, markdown_to_html, extract_title)

def main():
    # Get base path from command line argument or default to "/"
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    
    # Use docs directory instead of public for GitHub Pages
    output_dir = "docs"
    
    # Clear and recreate output directory
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.mkdir(output_dir)
    
    # Copy static assets
    copy_dir("static", output_dir)
    
    # Generate pages recursively from all markdown files in content directory
    generate_pages_recursive("content", "template.html", output_dir, base_path)

if __name__ == "__main__":
    main()
