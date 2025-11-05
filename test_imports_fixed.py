#!/usr/bin/env python3
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from text_processing import text_to_textnodes
    print("✓ Successfully imported text_to_textnodes from text_processing")
    
    from markdown_converter import markdown_to_html_node
    print("✓ Successfully imported markdown_to_html_node from markdown_converter")
    
    from file_utils import copy_directory_contents
    print("✓ Successfully imported copy_directory_contents from file_utils")
    
    from textnode import TextNode, TextType
    print("✓ Successfully imported TextNode and TextType from textnode")
    
    from htmlnode import HTMLNode, LeafNode, ParentNode
    print("✓ Successfully imported HTMLNode classes from htmlnode")
    
    print("All imports working correctly!")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("Current Python path:", sys.path)
    
except Exception as e:
    print(f"✗ Other error: {e}")
