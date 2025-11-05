import unittest
import os
import tempfile
import shutil
from page_generator import generate_page


class TestGeneratePage(unittest.TestCase):
    def setUp(self):
        # Create temporary directories for testing
        self.test_dir = tempfile.mkdtemp()
        self.content_dir = os.path.join(self.test_dir, "content")
        self.template_dir = os.path.join(self.test_dir, "templates")
        self.output_dir = os.path.join(self.test_dir, "output")
        
        os.makedirs(self.content_dir)
        os.makedirs(self.template_dir)
        os.makedirs(self.output_dir)
        
        # Create test markdown file
        self.test_markdown = """# Test Page Title

This is **bold** and _italic_ text.

- List item 1
- List item 2
"""
        
        with open(os.path.join(self.content_dir, "test.md"), "w") as f:
            f.write(self.test_markdown)
        
        # Create test template
        self.test_template = """<!DOCTYPE html>
<html>
<head>
    <title>{{ Title }}</title>
</head>
<body>
    <article>{{ Content }}</article>
</body>
</html>"""
        
        with open(os.path.join(self.template_dir, "template.html"), "w") as f:
            f.write(self.test_template)

    def tearDown(self):
        # Clean up temporary directories
        shutil.rmtree(self.test_dir)

    def test_generate_page_basic(self):
        from_path = os.path.join(self.content_dir, "test.md")
        template_path = os.path.join(self.template_dir, "template.html")
        dest_path = os.path.join(self.output_dir, "output.html")
        
        generate_page(from_path, template_path, dest_path)
        
        # Verify the file was created
        self.assertTrue(os.path.exists(dest_path))
        
        # Read and verify the content
        with open(dest_path, 'r') as f:
            content = f.read()
        
        self.assertIn("<title>Test Page Title</title>", content)
        self.assertIn("<article>", content)
        self.assertIn("</article>", content)
        self.assertIn("<b>bold</b>", content)
        self.assertIn("<i>italic</i>", content)

    def test_generate_page_creates_directories(self):
        from_path = os.path.join(self.content_dir, "test.md")
        template_path = os.path.join(self.template_dir, "template.html")
        dest_path = os.path.join(self.output_dir, "nested", "deep", "output.html")
        
        generate_page(from_path, template_path, dest_path)
        
        # Verify the nested directories were created
        self.assertTrue(os.path.exists(dest_path))

    def test_generate_page_missing_markdown(self):
        from_path = os.path.join(self.content_dir, "nonexistent.md")
        template_path = os.path.join(self.template_dir, "template.html")
        dest_path = os.path.join(self.output_dir, "output.html")
        
        with self.assertRaises(FileNotFoundError):
            generate_page(from_path, template_path, dest_path)

    def test_generate_page_missing_template(self):
        from_path = os.path.join(self.content_dir, "test.md")
        template_path = os.path.join(self.template_dir, "nonexistent.html")
        dest_path = os.path.join(self.output_dir, "output.html")
        
        with self.assertRaises(FileNotFoundError):
            generate_page(from_path, template_path, dest_path)


if __name__ == "__main__":
    unittest.main()
