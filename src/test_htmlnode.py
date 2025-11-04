import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_default_values(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

        node2 = HTMLNode(props={})
        self.assertEqual(node2.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
            "class": "link"
        })
        expected = ' href="https://www.google.com" target="_blank" class="link"'
        self.assertEqual(node.props_to_html(), expected)

    def test_repr(self):
        node = HTMLNode("p", "Hello world", None, {"class": "text"})
        expected = "HTMLNode(tag=p, value=Hello world, children=None, props={'class': 'text'})"
        self.assertEqual(repr(node), expected)

    def test_to_html_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_with_children(self):
        child1 = HTMLNode("span", "child1")
        child2 = HTMLNode("span", "child2")
        parent = HTMLNode("div", None, [child1, child2])
        self.assertEqual(parent.children, [child1, child2])
        self.assertIsNone(parent.value)

    def test_with_value_and_no_children(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertIsNone(node.children)

    def test_props_with_special_characters(self):
        node = HTMLNode(props={
            "data-value": "test&value",
            "onclick": "alert('hello')"
        })
        expected = ' data-value="test&value" onclick="alert(\'hello\')"'
        self.assertEqual(node.props_to_html(), expected)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Raw text content")
        self.assertEqual(node.to_html(), "Raw text content")

    def test_leaf_to_html_self_closing_tags(self):
        node = LeafNode("br", "")
        self.assertEqual(node.to_html(), "<br></br>")

    def test_leaf_to_html_heading(self):
        node = LeafNode("h1", "Main Title")
        self.assertEqual(node.to_html(), "<h1>Main Title</h1>")

    def test_leaf_to_html_span_with_class(self):
        node = LeafNode("span", "Highlighted text", {"class": "highlight"})
        self.assertEqual(node.to_html(), '<span class="highlight">Highlighted text</span>')

    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("button", "Submit", {
            "type": "submit", 
            "class": "btn btn-primary",
            "id": "submit-btn"
        })
        expected = '<button type="submit" class="btn btn-primary" id="submit-btn">Submit</button>'
        self.assertEqual(node.to_html(), expected)

    def test_leaf_no_value_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_children_none(self):
        node = LeafNode("p", "Test")
        self.assertIsNone(node.children)

    def test_leaf_repr(self):
        node = LeafNode("a", "Link", {"href": "https://example.com"})
        expected = "LeafNode(tag=a, value=Link, props={'href': 'https://example.com'})"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()
