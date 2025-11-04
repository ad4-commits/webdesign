from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode, ParentNode
from text_processing import (split_nodes_delimiter, extract_markdown_images, 
                           extract_markdown_links, split_nodes_image, split_nodes_link)

def main():
    print("Advanced TextNode Splitting Examples:")
    
    # Test cases for image splitting
    print("\n" + "="*50)
    print("Image Splitting Examples:")
    
    image_cases = [
        TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        ),
        TextNode(
            "![first](img1.png) middle ![second](img2.png) end",
            TextType.TEXT,
        ),
        TextNode(
            "No images here",
            TextType.TEXT,
        ),
    ]
    
    for i, node in enumerate(image_cases, 1):
        print(f"\nImage Case {i}:")
        print(f"Input:  {node}")
        result = split_nodes_image([node])
        print(f"Output: {result}")
        
        # Convert to HTML to show final result
        html_nodes = [text_node_to_html_node(n) for n in result]
        html_result = "".join([n.to_html() for n in html_nodes])
        print(f"HTML:   {html_result}")
    
    # Test cases for link splitting
    print("\n" + "="*50)
    print("Link Splitting Examples:")
    
    link_cases = [
        TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        ),
        TextNode(
            "[start](1.com) middle [end](2.com)",
            TextType.TEXT,
        ),
        TextNode(
            "Text with [a link](example.com) in the middle",
            TextType.TEXT,
        ),
    ]
    
    for i, node in enumerate(link_cases, 1):
        print(f"\nLink Case {i}:")
        print(f"Input:  {node}")
        result = split_nodes_link([node])
        print(f"Output: {result}")
        
        # Convert to HTML to show final result
        html_nodes = [text_node_to_html_node(n) for n in result]
        html_result = "".join([n.to_html() for n in html_nodes])
        print(f"HTML:   {html_result}")
    
    # Complex example showing the full processing pipeline
    print("\n" + "="*50)
    print("Full Processing Pipeline Example:")
    
    complex_text = TextNode(
        "Welcome! This is **bold** text with `code` and _italic_. "
        "Also ![an image](https://example.com/img.png) and "
        "[a link](https://example.com). More **bold** here!",
        TextType.TEXT
    )
    
    print(f"Original: {complex_text}")
    
    # Processing order: images -> links -> bold -> italic -> code
    nodes = [complex_text]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes) 
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    print(f"After processing: {nodes}")
    
    # Convert to final HTML
    html_nodes = [text_node_to_html_node(n) for n in nodes]
    html_result = "".join([n.to_html() for n in html_nodes])
    print(f"Final HTML: {html_result}")

if __name__ == "__main__":
    main()
