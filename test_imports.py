#!/usr/bin/env python3
try:
    from src.text_processing import text_to_textnodes
    print("✓ Successfully imported text_to_textnodes from text_processing")
    
    from src.markdown_converter import markdown_to_html_node
    print("✓ Successfully imported markdown_to_html_node from markdown_converter")
    
    from src.file_utils import copy_directory_contents
    print("✓ Successfully imported copy_directory_contents from file_utils")
    
    print("All imports working correctly!")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    
except Exception as e:
    print(f"✗ Other error: {e}")
