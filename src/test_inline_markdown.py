import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" in the middle", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode("This is text with a **bolded phrase** and **another**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic phrase* in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic phrase", TextType.ITALIC),
                TextNode(" in the middle", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![first image](https://example.com/img1.gif) and ![second image](https://example.com/img2.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("first image", "https://example.com/img1.gif"),
                ("second image", "https://example.com/img2.jpeg"),
            ],
            matches,
        )

    def test_extract_markdown_images_empty(self):
        text = "This is text with no images"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to example](https://www.example.com) and [to docs](https://docs.example.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to example", "https://www.example.com"),
                ("to docs", "https://docs.example.com"),
            ],
            matches,
        )

    def test_extract_markdown_links_single(self):
        text = "Check out [this link](https://example.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("this link", "https://example.com")], matches)

    def test_extract_markdown_links_empty(self):
        text = "This is text with no links"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_links_no_images(self):
        text = "This has a ![image](https://example.com/img.png) but no links"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_mixed(self):
        text = "This has a [link](https://example.com) and an ![image](https://example.com/img.png)"
        links = extract_markdown_links(text)
        images = extract_markdown_images(text)
        self.assertListEqual([("link", "https://example.com")], links)
        self.assertListEqual([("image", "https://example.com/img.png")], images)

if __name__ == "__main__":
    unittest.main()