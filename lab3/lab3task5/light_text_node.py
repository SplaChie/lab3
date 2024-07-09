from light_node import LightNode

class LightTextNode(LightNode):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text
