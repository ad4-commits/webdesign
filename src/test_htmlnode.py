import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()
