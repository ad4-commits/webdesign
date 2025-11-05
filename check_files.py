#!/usr/bin/env python3
import os

PROJECT_ROOT = "/home/eda/public/webdesign"

required_files = [
    "content/index.md",
    "templates/template.html", 
    "static/index.css",
    "static/images/tolkien.png"
]

print("Checking required files...")
all_exist = True

for file_path in required_files:
    full_path = os.path.join(PROJECT_ROOT, file_path)
    exists = os.path.exists(full_path)
    status = "✓" if exists else "✗"
    print(f"{status} {file_path}: {exists}")
    if not exists:
        all_exist = False

if all_exist:
    print("\nAll files exist! You can run ./main.sh")
else:
    print("\nSome files are missing. Let me create them...")
    
    # Create missing files
    if not os.path.exists(os.path.join(PROJECT_ROOT, "content/index.md")):
        os.makedirs(os.path.join(PROJECT_ROOT, "content"), exist_ok=True)
        with open(os.path.join(PROJECT_ROOT, "content/index.md"), "w") as f:
            f.write("# Test Page\nThis is a test.")
    
    if not os.path.exists(os.path.join(PROJECT_ROOT, "templates/template.html")):
        os.makedirs(os.path.join(PROJECT_ROOT, "templates"), exist_ok=True)
        with open(os.path.join(PROJECT_ROOT, "templates/template.html"), "w") as f:
            f.write("<html><title>{{ Title }}</title><body>{{ Content }}</body></html>")
    
    if not os.path.exists(os.path.join(PROJECT_ROOT, "static/index.css")):
        os.makedirs(os.path.join(PROJECT_ROOT, "static"), exist_ok=True)
        with open(os.path.join(PROJECT_ROOT, "static/index.css"), "w") as f:
            f.write("body { margin: 0; }")
    
    if not os.path.exists(os.path.join(PROJECT_ROOT, "static/images/tolkien.png")):
        os.makedirs(os.path.join(PROJECT_ROOT, "static/images"), exist_ok=True)
        with open(os.path.join(PROJECT_ROOT, "static/images/tolkien.png"), "w") as f:
            f.write("placeholder")
    
    print("Missing files created!")
