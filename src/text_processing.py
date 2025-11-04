from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        # Only split TEXT nodes, leave other types as-is
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        parts = text.split(delimiter)
        
        # If there's an odd number of parts, the delimiters don't match
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {text}")
        
        # Process each part
        for i, part in enumerate(parts):
            if part == "":  # Skip empty parts
                continue
            if i % 2 == 0:
                # Even index = regular text
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Odd index = delimited text (bold, italic, code, etc.)
                new_nodes.append(TextNode(part, text_type))
    
    return new_nodes


def extract_markdown_images(text):
    """Extract markdown images from text and return list of (alt_text, url) tuples"""
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    """Extract markdown links from text and return list of (anchor_text, url) tuples"""
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"  # Negative lookbehind to exclude images
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes):
    """Split TEXT nodes that contain markdown images into multiple nodes"""
    new_nodes = []
    
    for node in old_nodes:
        # Only split TEXT nodes, leave other types as-is
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        images = extract_markdown_images(text)
        
        # If no images found, keep the node as-is
        if not images:
            new_nodes.append(node)
            continue
        
        current_text = text
        for alt_text, url in images:
            # Find the position of the image markdown in the current text
            markdown = f"![{alt_text}]({url})"
            parts = current_text.split(markdown, 1)  # Split on first occurrence
            
            # Add the text before the image
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            # Update current_text to the remaining part
            current_text = parts[1] if len(parts) > 1 else ""
        
        # Add any remaining text after the last image
        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    
    return new_nodes


def split_nodes_link(old_nodes):
    """Split TEXT nodes that contain markdown links into multiple nodes"""
    new_nodes = []
    
    for node in old_nodes:
        # Only split TEXT nodes, leave other types as-is
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        links = extract_markdown_links(text)
        
        # If no links found, keep the node as-is
        if not links:
            new_nodes.append(node)
            continue
        
        current_text = text
        for anchor_text, url in links:
            # Find the position of the link markdown in the current text
            markdown = f"[{anchor_text}]({url})"
            parts = current_text.split(markdown, 1)  # Split on first occurrence
            
            # Add the text before the link
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            # Add the link node
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            
            # Update current_text to the remaining part
            current_text = parts[1] if len(parts) > 1 else ""
        
        # Add any remaining text after the last link
        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    
    return new_nodes
