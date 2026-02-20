import unittest

from main import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_title_with_leading_trailing_whitespace(self):
        self.assertEqual(extract_title("#   Hello World  "), "Hello World")

    def test_title_not_first_line(self):
        md = "Some text\n\n# My Title\n\nMore text"
        self.assertEqual(extract_title(md), "My Title")

    def test_no_h1_raises(self):
        with self.assertRaises(ValueError):
            extract_title("## Not an h1\n\nSome paragraph")

    def test_h2_not_matched_as_title(self):
        with self.assertRaises(ValueError):
            extract_title("## Heading Two")

    def test_empty_markdown_raises(self):
        with self.assertRaises(ValueError):
            extract_title("")

    def test_title_with_inline_formatting(self):
        self.assertEqual(extract_title("# Hello **World**"), "Hello **World**")


if __name__ == "__main__":
    unittest.main()
