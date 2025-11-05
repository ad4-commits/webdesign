import unittest
from title_extractor import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_extract_title_with_whitespace(self):
        markdown = "   #   Hello World   "
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_extract_title_in_content(self):
        markdown = """# Main Title

This is some content with **bold** text.

## Subheading

More content here.
"""
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_extract_title_multiple_headings(self):
        markdown = """# First Title
## Second Title
### Third Title"""
        self.assertEqual(extract_title(markdown), "First Title")

    def test_extract_title_no_h1(self):
        markdown = """## This is not an h1
This is just regular text.
### Another heading"""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertIn("No h1 header found", str(context.exception))

    def test_extract_title_empty_string(self):
        markdown = ""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertIn("No h1 header found", str(context.exception))

    def test_extract_title_only_whitespace(self):
        markdown = "   \n   \n   "
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertIn("No h1 header found", str(context.exception))

    def test_extract_title_h2_not_h1(self):
        markdown = "## This is h2, not h1"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertIn("No h1 header found", str(context.exception))

    def test_extract_title_complex_markdown(self):
        markdown = """# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.
"""
        self.assertEqual(extract_title(markdown), "Tolkien Fan Club")


if __name__ == "__main__":
    unittest.main()
