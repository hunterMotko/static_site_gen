import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
