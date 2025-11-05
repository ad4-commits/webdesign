#!/usr/bin/env python3
import os
import shutil

def copy_static_to_public():
    """Reliably copy static files to public directory"""
    
    # Define source and destination
    static_dir = "static"
    public_dir = "public"
    
    # Check if static directory exists
    if not os.path.exists(static_dir):
        print(f"Error: {static_dir} directory does not exist!")
        return False
    
    # Check if static has the required files
    required_files = ["index.css", "images/tolkien.png"]
    missing_files = []
    
    for file_path in required_files:
        full_path = os.path.join(static_dir, file_path)
        if not os.path.exists(full_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"Error: Missing files in static directory: {missing_files}")
        return False
    
    # Clean public directory if it exists
    if os.path.exists(public_dir):
        print(f"Removing existing {public_dir} directory...")
        shutil.rmtree(public_dir)
    
    # Create public directory
    os.makedirs(public_dir, exist_ok=True)
    print(f"Created {public_dir} directory")
    
    # Copy all files from static to public
    print("Copying files...")
    for item in os.listdir(static_dir):
        source_path = os.path.join(static_dir, item)
        dest_path = os.path.join(public_dir, item)
        
        if os.path.isfile(source_path):
            shutil.copy2(source_path, dest_path)
            print(f"  Copied: {item}")
        elif os.path.isdir(source_path):
            shutil.copytree(source_path, dest_path)
            print(f"  Copied directory: {item}/")
    
    print("✓ All files copied successfully!")
    
    # Verify the copy
    print("\nVerifying copy...")
    for file_path in required_files:
        full_path = os.path.join(public_dir, file_path)
        if os.path.exists(full_path):
            print(f"  ✓ {file_path} exists")
        else:
            print(f"  ✗ {file_path} missing!")
            return False
    
    return True

if __name__ == "__main__":
    print("Static File Copy Utility")
    print("=" * 40)
    
    if copy_static_to_public():
        print("\n✓ SUCCESS: Files copied to public directory!")
        print("You can now serve the site with: cd public && python3 -m http.server 8888")
    else:
        print("\n✗ FAILED: Could not copy files")
