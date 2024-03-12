import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        print("\nStarting TestHtmlNode...")
        node = HTMLNode(tag="a",props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(tag=None,value="hello this is plain text")
        node3 = HTMLNode(tag="p",value="Hello paragraph")
        node4 = HTMLNode(tag="a",props={"href": "https://www.google.com", "target": "_blank"})
        print(f"Props to HTML:\n{node.props_to_html()}")
        print(f"Print node:\n{node}")
        print("TestHMTLNode finished.")

class TestLeafNode(unittest.TestCase):
    def test(self):
        print("\nStarting TestLeafNode...")
        node = LeafNode(tag="p",value="Some text")
        node2 = LeafNode(tag="p", value="This is a paragraph of text.")
        node3 = LeafNode(tag="a",value="Click me!",props={"href": "https://www.google.com"})

        print(f"Print nodes:\n{node}\n{node2}\n{node3}")
        print(node.to_html())
        print(node2.to_html())
        print(node3.to_html())
        print("TestLeafNode finished.")
class TestParentNode(unittest.TestCase):
    def test_eq(self):
        print("\nStarting TestParentNode...")
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        print(f"Print node:\n{node}")
        print(f"TO_HTML:\n{node.to_html()}")
        print("TestParentNode finished.")

if __name__ == "__main__":
    unittest.main()