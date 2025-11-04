from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode, ParentNode
from text_processing import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

def main():
    print("Markdown Image and Link Extraction Examples:")
    
    # Test cases for image extraction
    image_test_cases = [
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        "No images here",
        "![single image](https://example.com/img.jpg)",
        "Mixed content with ![image1](img1.png) and [link1](link1.com) and ![image2](img2.png)"
    ]
    
    print("\nImage Extraction:")
    for i, text in enumerate(image_test_cases, 1):
        images = extract_markdown_images(text)
        print(f"{i}. '{text}' -> {images}")
    
    # Test cases for link extraction  
    link_test_cases = [
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        "No links here",
        "[single link](https://example.com)",
        "Mixed content with ![image1](img1.png) and [link1](link1.com) and [link2](link2.com)",
        "Empty cases: []() and [test]()"
    ]
    
    print("\nLink Extraction:")
    for i, text in enumerate(link_test_cases, 1):
        links = extract_markdown_links(text)
        print(f"{i}. '{text}' -> {links}")
    
    # Complex example showing both
    print("\n" + "="*60)
    print("Complex Example - Mixed Images and Links:")
    complex_text = """
    Welcome to my page! Here's an image: ![cat](https://example.com/cat.jpg)
    And here's a link: [visit here](https://example.com)
    Another image: ![dog](https://example.com/dog.png)
    And another link: [click me](https://boot.dev)
    """
    
    print("Text:", complex_text.strip())
    images = extract_markdown_images(complex_text)
    links = extract_markdown_links(complex_text)
    
    print("Extracted images:", images)
    print("Extracted links:", links)

if __name__ == "__main__":
    main()
