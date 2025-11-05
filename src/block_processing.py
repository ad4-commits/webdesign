def markdown_to_blocks(markdown):
    """
    Split a Markdown document into blocks separated by double newlines.
    
    Args:
        markdown: Raw Markdown string representing a full document
        
    Returns:
        List of block strings with leading/trailing whitespace removed
    """
    # Split by double newlines to get blocks
    blocks = markdown.split('\n\n')
    
    # Process each block: strip whitespace and filter out empty blocks
    processed_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block:  # Only include non-empty blocks
            processed_blocks.append(stripped_block)
    
    return processed_blocks
