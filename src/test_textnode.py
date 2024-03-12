import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("\nStarting TestTextNode...")
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        print(f"Node1:\n{node}\nNode2:\n{node2}")
        print("TestTextNode finished.")


if __name__ == "__main__":
    unittest.main()
