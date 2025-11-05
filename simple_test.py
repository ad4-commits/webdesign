#!/usr/bin/env python3
import os
import sys

print("Simple test running...")
print("Current dir:", os.getcwd())
print("Files in current dir:", [f for f in os.listdir('.') if f.endswith('.py')])

# Try basic file operations
if os.path.exists("content"):
    print("Content dir exists")
    md_files = []
    for root, dirs, files in os.walk("content"):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    print("Found markdown files:", md_files)
else:
    print("Content dir does not exist!")

print("Test completed")
