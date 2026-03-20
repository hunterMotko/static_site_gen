import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode(
            "This is a url text node",
            TextType.LINK,
            "http://localhost:8080"
        )
        node4 = TextNode(
            "This is a url text node",
            TextType.LINK,
            "http://localhost:8080"
        )
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode(
            "This is a url text node",
            TextType.LINK,
            "http://localhost:8080"
        )
        node4 = TextNode(
            "This is a url text node",
            TextType.LINK,
            "http://localhost:8080"
        )
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node4)

    def test_default(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.IMAGE)
        self.assertEqual(node.url, None)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE,
                        "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
