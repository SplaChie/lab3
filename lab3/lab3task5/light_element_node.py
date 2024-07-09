from light_node import LightNode


class LightElementNode(LightNode):
    def __init__(self, tag_name, display_type, closing_type):
        self.tag_name = tag_name
        self.display_type = display_type
        self.closing_type = closing_type
        self.css_classes = []
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        opening_tag = f"<{self.tag_name} class='{' '.join(self.css_classes)}'>"
        closing_tag = f"</{self.tag_name}>"
        inner_html = "".join([child.render() for child in self.children])

        if self.closing_type == "single":
            return f"<{self.tag_name}/>"
        else:
            return f"{opening_tag}{inner_html}{closing_tag}"

    def outer_html(self):
        return self.render()

    def inner_html(self):
        return "".join([child.render() for child in self.children])
