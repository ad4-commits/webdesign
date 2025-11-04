from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode

def main():
    # Original TextNode demonstration
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print("TextNode:", text_node)
    
    # New ParentNode demonstrations
    print("\nParentNode Examples:")
    
    # Simple parent with children
    simple_parent = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print("Simple Parent:", simple_parent.to_html())
    
    # Nested parent structure
    nested_parent = ParentNode(
        "div",
        [
            LeafNode("h1", "Main Title"),
            ParentNode(
                "ul",
                [
                    LeafNode("li", "Item 1"),
                    LeafNode("li", "Item 2"),
                    ParentNode(
                        "li",
                        [
                            LeafNode("b", "Important"),
                            LeafNode(None, " item")
                        ]
                    )
                ]
            )
        ],
        {"class": "container"}
    )
    print("Nested Parent:", nested_parent.to_html())

if __name__ == "__main__":
    main()
