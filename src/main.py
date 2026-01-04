from textnode import TextNode, TextType

def main():
    dummy_node = TextNode("This is a text node", TextType.BOLD, "https://www.github.com")
    print(dummy_node)

if __name__ == "__main__":
    main()