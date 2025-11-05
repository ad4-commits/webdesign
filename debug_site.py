#!/usr/bin/env python3
import os
import shutil

def debug():
    project_root = "/home/eda/public/webdesign"
    
    print("=== DEBUGGING STATIC SITE GENERATOR ===")
    
    # Check content file
    content_file = os.path.join(project_root, "content", "index.md")
    print(f"1. Content file: {content_file}")
    print(f"   Exists: {os.path.exists(content_file)}")
    
    if os.path.exists(content_file):
        with open(content_file, 'r') as f:
            content = f.read()
        print(f"   First line: {content.split(chr(10))[0]}")
        print(f"   Length: {len(content)} characters")
    
    # Check template file
    template_file = os.path.join(project_root, "templates", "template.html")
    print(f"2. Template file: {template_file}")
    print(f"   Exists: {os.path.exists(template_file)}")
    
    # Check public directory
    public_dir = os.path.join(project_root, "public")
    print(f"3. Public directory: {public_dir}")
    print(f"   Exists: {os.path.exists(public_dir)}")
    
    if os.path.exists(public_dir):
        index_file = os.path.join(public_dir, "index.html")
        print(f"   index.html exists: {os.path.exists(index_file)}")
        if os.path.exists(index_file):
            with open(index_file, 'r') as f:
                html = f.read()
            if "Test Page" in html:
                print("   ⚠️  CONTAINS 'Test Page' - this is the problem!")
            if "Tolkien" in html:
                print("   ✓ Contains 'Tolkien' - good!")
            print(f"   First 200 chars: {html[:200]}...")

if __name__ == "__main__":
    debug()
