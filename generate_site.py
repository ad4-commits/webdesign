#!/usr/bin/env python3
import os
import shutil

def copy_static_files():
    """Copy static files to public directory"""
    source = "static"
    destination = "public"
    
    if not os.path.exists(source):
        print(f"Error: Source directory '{source}' does not exist")
        return False
    
    # Clean destination
    if os.path.exists(destination):
        print(f"Cleaning {destination} directory...")
        shutil.rmtree(destination)
    
    # Copy files
    print(f"Copying {source} to {destination}...")
    shutil.copytree(source, destination)
    print("✓ Files copied successfully!")
    return True

def create_simple_html():
    """Create a simple HTML file"""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Static Site</title>
    <link rel="stylesheet" href="index.css">
</head>
<body>
    <header>
        <h1>Welcome to My Static Site</h1>
        <p>Generated with our static site generator</p>
    </header>
    <main>
        <h2>About This Site</h2>
        <p>This site was automatically generated and includes:</p>
        <ul>
            <li>Static file copying</li>
            <li>CSS styling</li>
            <li>Clean HTML structure</li>
        </ul>
        <p>Check the <code>public</code> directory for the generated files!</p>
    </main>
</body>
</html>"""
    
    with open("public/index.html", "w") as f:
        f.write(html_content)
    print("✓ HTML file created!")

def main():
    print("Simple Static Site Generator")
    print("=" * 40)
    
    if copy_static_files():
        create_simple_html()
        print("\n✓ Site generation complete!")
        print("Serve with: cd public && python3 -m http.server 8888")
    else:
        print("\n✗ Site generation failed!")

if __name__ == "__main__":
    main()
