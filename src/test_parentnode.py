import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("span", "hello")],
            {"class": "container", "id": "main"},
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container" id="main"><span>hello</span></div>'
        )

    def test_to_html_very_deep_nesting(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "nav",
                    [
                        ParentNode(
                            "ul",
                            [LeafNode("li", "item 1"),
                             LeafNode("li", "item 2")]
                        )
                    ]
                )
            ]
        )
        expected = "<div><nav><ul><li>item 1</li><li>item 2</li></ul></nav></div>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("b", "bold")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()
