from light_element_node import LightElementNode
from light_text_node import LightTextNode

def main():
    # Create elements
    root = LightElementNode("div", "block", "double")
    root.css_classes.append("container")

    header = LightElementNode("h1", "block", "double")
    header.add_child(LightTextNode("Welcome to LightHTML!"))

    paragraph = LightElementNode("p", "block", "double")
    paragraph.add_child(LightTextNode("This is an example paragraph."))

    image = LightElementNode("img", "inline", "single")

    # Build the hierarchy
    root.add_child(header)
    root.add_child(paragraph)
    root.add_child(image)

    # Render the outer HTML
    print(root.outer_html())

if __name__ == "__main__":
    main()
