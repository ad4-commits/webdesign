from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode, ParentNode
from text_processing import text_to_textnodes

def main():
    print("Complete Text Processing Pipeline - text_to_textnodes:")
    
    # Test cases for the complete processing pipeline
    test_cases = [
        (
            "Complex Example",
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        ),
        (
            "Simple Text", 
            "Just plain text without formatting"
        ),
        (
            "Mixed Formatting",
            "**Bold text**, _italic text_, and `code` in one sentence."
        ),
        (
            "Images and Links",
            "Visit my [website](https://example.com) and see this ![photo](photo.jpg)."
        ),
        (
            "Real World Example",
            "**Important**: Please read the _documentation_ and try the `example.py` file. Download the ![logo](logo.png) and visit our [site](https://project.org)."
        ),
    ]
    
    for description, text in test_cases:
        print(f"\n{'='*60}")
        print(f"Test: {description}")
        print(f"Input:  {text}")
        
        # Process the text
        nodes = text_to_textnodes(text)
        print(f"Nodes:  {nodes}")
        
        # Convert to HTML
        html_nodes = [text_node_to_html_node(n) for n in nodes]
        html_result = "".join([n.to_html() for n in html_nodes])
        print(f"HTML:   {html_result}")
        
        # Show the rendered result
        print(f"Rendered: {html_result}")
    
    # Demonstrate the complete pipeline with a complex example
    print(f"\n{'='*60}")
    print("FINAL DEMONSTRATION - Complete Markdown to HTML Conversion")
    print('='*60)
    
    markdown_text = """
# Welcome to My Site

This is a **bold statement** with some _italic emphasis_ and `inline code`.

Check out this image: ![Python Logo](https://example.com/python.png)

Visit my [portfolio](https://myportfolio.com) for more examples.

**Remember**: Always test your _code_ with `python -m unittest`!
"""
    
    # Process each line (in a real implementation, we'd handle blocks)
    lines = [line.strip() for line in markdown_text.split('\n') if line.strip()]
    
    for i, line in enumerate(lines, 1):
        print(f"\nLine {i}: {line}")
        if line.startswith('# '):
            # Simple heading detection (for demonstration)
            content = line[2:]
            print(f"  → <h1>{content}</h1>")
        else:
            nodes = text_to_textnodes(line)
            html_nodes = [text_node_to_html_node(n) for n in nodes]
            html_result = "".join([n.to_html() for n in html_nodes])
            print(f"  → <p>{html_result}</p>")

if __name__ == "__main__":
    main()
