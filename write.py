from manim import *

class write_text:
    def __init__(self,w,pos,width):
        self.write = Text(w, font="Noto Sans CJK", font_size=33, color=YELLOW).to_edge(pos)
        self.write.scale_to_fit_width(width)
    def animation(self, scene):
        scene.play(Write(self.write))