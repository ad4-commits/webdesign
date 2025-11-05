import os
from markdown_converter import markdown_to_html_node
from title_extractor import extract_title


def generate_page(from_path, template_path, dest_path):
    """
    Generate an HTML page from markdown using a template.
    
    Args:
        from_path: Path to the markdown file
        template_path: Path to the HTML template file
        dest_path: Path where the generated HTML should be saved
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read markdown file
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Read template file
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Extract title
    title = extract_title(markdown_content)
    
    # Replace placeholders in template
    final_html = template_content.replace('{{ Title }}', title)
    final_html = final_html.replace('{{ Content }}', html_content)
    
    # Create destination directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the final HTML file
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"✓ Page generated successfully: {dest_path}")


if __name__ == "__main__":
    # Test the function
    try:
        generate_page(
            "../content/index.md",
            "../templates/template.html", 
            "../public/test_output.html"
        )
    except Exception as e:
        print(f"Error: {e}")
