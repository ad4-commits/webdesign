from textnode import TextNode, TextType
from htmlnode import LeafNode

def main():
    # Original TextNode demonstration
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print("TextNode:", text_node)
    
    # New LeafNode demonstrations
    print("\nLeafNode Examples:")
    
    # Paragraph
    paragraph = LeafNode("p", "This is a paragraph of text.")
    print("Paragraph:", paragraph.to_html())
    
    # Link with props
    link = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print("Link:", link.to_html())
    
    # Raw text (no tag)
    raw_text = LeafNode(None, "This is just raw text")
    print("Raw text:", raw_text.to_html())
    
    # Heading with class
    heading = LeafNode("h1", "Welcome to my site", {"class": "title"})
    print("Heading:", heading.to_html())

if __name__ == "__main__":
    main()
