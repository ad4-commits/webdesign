from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode, ParentNode
from text_processing import split_nodes_delimiter

def main():
    print("TextNode Delimiter Splitting Examples:")
    
    # Test cases for delimiter splitting
    test_cases = [
        (
            "Basic code",
            TextNode("This is text with a `code block` word", TextType.TEXT),
            "`",
            TextType.CODE
        ),
        (
            "Bold text",
            TextNode("This is **bold text** in the middle", TextType.TEXT),
            "**",
            TextType.BOLD
        ),
        (
            "Italic text", 
            TextNode("This has _italic text_ here", TextType.TEXT),
            "_",
            TextType.ITALIC
        ),
        (
            "Multiple code blocks",
            TextNode("This has `code1` and `code2` words", TextType.TEXT),
            "`",
            TextType.CODE
        ),
    ]
    
    for description, node, delimiter, text_type in test_cases:
        print(f"\n{description}:")
        print(f"Input: {node}")
        try:
            result = split_nodes_delimiter([node], delimiter, text_type)
            print(f"Output: {result}")
            
            # Convert to HTML to show the final result
            html_nodes = [text_node_to_html_node(n) for n in result]
            html_result = "".join([n.to_html() for n in html_nodes])
            print(f"HTML: {html_result}")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Complex example with multiple delimiter types
    print("\n" + "="*50)
    print("Complex Example - Multiple Delimiter Types:")
    complex_node = TextNode(
        "Start with **bold**, then `code`, and _italic_ text. Also **more bold**!",
        TextType.TEXT
    )
    print(f"Input: {complex_node}")
    
    # Process in the correct order (most specific first)
    result = split_nodes_delimiter([complex_node], "`", TextType.CODE)
    result = split_nodes_delimiter(result, "**", TextType.BOLD) 
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    print(f"Split nodes: {result}")
    
    # Convert to final HTML
    html_nodes = [text_node_to_html_node(n) for n in result]
    html_result = "".join([n.to_html() for n in html_nodes])
    print(f"Final HTML: {html_result}")

if __name__ == "__main__":
    main()
