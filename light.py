from color import Color
class Light:
    """Light repreents a point light sourcce of a certain color"""

    def __init__(self, position, color=Color.from_hex("#FFFFFF")):
        self.position=position
        self.color=color
