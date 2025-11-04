import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a link", TextType.LINK, "https://boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("This is text", TextType.TEXT)
        node2 = TextNode("This is different text", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_text_type(self):
        node = TextNode("This is bold", TextType.BOLD)
        node2 = TextNode("This is bold", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a link", TextType.LINK, "https://example.com")
        self.assertNotEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("This is text", TextType.TEXT)
        node2 = TextNode("This is text", TextType.TEXT, None)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Test text", TextType.CODE, "https://example.com")
        expected = "TextNode(Test text, code, https://example.com)"
        self.assertEqual(repr(node), expected)

    def test_repr_no_url(self):
        node = TextNode("Test text", TextType.ITALIC)
        expected = "TextNode(Test text, italic, None)"
        self.assertEqual(repr(node), expected)

    def test_image_type(self):
        node = TextNode("alt text", TextType.IMAGE, "https://example.com/image.png")
        node2 = TextNode("alt text", TextType.IMAGE, "https://example.com/image.png")
        self.assertEqual(node, node2)

    def test_not_eq_image_vs_link(self):
        node = TextNode("alt text", TextType.IMAGE, "https://example.com/image.png")
        node2 = TextNode("alt text", TextType.LINK, "https://example.com/image.png")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
