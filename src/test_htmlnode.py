import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "id": "main"}
        )
        # Testing multiple props and correct formatting
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" id="main"'
        )

    def test_values(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "What up", None, {"class": "primary"})
        expected = "HTMLNode(p, What up, None, {'class': 'primary'})"
        self.assertEqual(repr(node), expected)

    def test_to_html_error(self):
        node = HTMLNode()
        # This is the correct way to test if a function raises an error
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
