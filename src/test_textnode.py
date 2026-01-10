import unittest

from htmlnode import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_urlnoteqNone(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        node2 = TextNode("This is a different text node", TextType.ITALIC)
        self.assertNotEqual(node,node2)

    def test_urlnoteq(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        node2 = TextNode("This is a text node", TextType.BOLD,"https://github.com")
        self.assertNotEqual(node,node2)
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.google.com/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.google.com/", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
if __name__ == "__main__":
    unittest.main()