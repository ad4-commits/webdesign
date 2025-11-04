from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode, ParentNode

def main():
    print("TextNode to HTMLNode Conversion Examples:")
    
    # Test all TextType conversions
    text_nodes = [
        TextNode("This is plain text", TextType.TEXT),
        TextNode("This is bold text", TextType.BOLD),
        TextNode("This is italic text", TextType.ITALIC),
        TextNode("print('hello world')", TextType.CODE),
        TextNode("Click here", TextType.LINK, "https://example.com"),
        TextNode("A beautiful sunset", TextType.IMAGE, "https://example.com/sunset.jpg"),
    ]
    
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        print(f"TextNode: {text_node}")
        print(f"HTMLNode: {html_node.to_html()}")
        print()
    
    # Demonstrate using converted nodes in a ParentNode
    print("Complex example with ParentNode:")
    paragraph = ParentNode(
        "p",
        [
            text_node_to_html_node(TextNode("Welcome to ", TextType.TEXT)),
            text_node_to_html_node(TextNode("my website", TextType.BOLD)),
            text_node_to_html_node(TextNode("! You can ", TextType.TEXT)),
            text_node_to_html_node(TextNode("view the code", TextType.CODE)),
            text_node_to_html_node(TextNode(" or ", TextType.TEXT)),
            text_node_to_html_node(TextNode("visit our site", TextType.LINK, "https://example.com")),
        ]
    )
    print(paragraph.to_html())

if __name__ == "__main__":
    main()
