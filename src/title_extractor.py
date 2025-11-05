def extract_title(markdown):
    """
    Extract the h1 header from markdown content.
    
    Args:
        markdown: Raw markdown string
        
    Returns:
        String containing the h1 header text
        
    Raises:
        Exception: If no h1 header is found
    """
    lines = markdown.split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('# ') and len(stripped_line) > 2:
            # Found h1 header, return the text without the # and any extra whitespace
            return stripped_line[1:].strip()
    
    raise Exception("No h1 header found in markdown")


if __name__ == "__main__":
    # Simple test
    test_markdown = "# Hello World\nThis is some content"
    print(f"Extracted title: '{extract_title(test_markdown)}'")
