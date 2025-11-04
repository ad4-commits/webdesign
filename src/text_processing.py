from textnode import TextNode, TextType


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
