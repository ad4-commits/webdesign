from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


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


def block_to_block_type(block):
    """
    Determine the type of a Markdown block.
    
    Args:
        block: A single block of Markdown text (already stripped)
        
    Returns:
        BlockType enum representing the type of block
    """
    lines = block.split('\n')
    
    # Check for heading (1-6 # characters followed by space)
    if len(lines) == 1 and lines[0].startswith('#') and ' ' in lines[0]:
        hash_count = 0
        for char in lines[0]:
            if char == '#':
                hash_count += 1
            else:
                break
        if 1 <= hash_count <= 6 and lines[0][hash_count] == ' ':
            return BlockType.HEADING
    
    # Check for code block (starts and ends with triple backticks)
    if len(lines) >= 1:
        first_line = lines[0].strip()
        last_line = lines[-1].strip()
        if (first_line.startswith('```') and first_line.count('`') >= 3 and 
            last_line.startswith('```') and last_line.count('`') >= 3):
            return BlockType.CODE
    
    # Check for quote block (every line starts with >)
    if all(line.strip().startswith('>') for line in lines if line.strip()):
        return BlockType.QUOTE
    
    # Check for unordered list (every line starts with - followed by space)
    if all(line.strip().startswith('- ') for line in lines if line.strip()):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered list (every line starts with number. followed by space, in order)
    if lines and all(line.strip() for line in lines):  # All lines non-empty
        is_ordered = True
        expected_number = 1
        for line in lines:
            stripped_line = line.strip()
            # Check if line starts with expected_number. followed by space
            if not (stripped_line.startswith(f"{expected_number}. ") and 
                   len(stripped_line) > len(f"{expected_number}. ")):
                is_ordered = False
                break
            expected_number += 1
        
        if is_ordered:
            return BlockType.ORDERED_LIST
    
    # If none of the above, it's a paragraph
    return BlockType.PARAGRAPH
