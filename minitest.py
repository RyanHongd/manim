from manim import *

class AlignText(Scene):
    def construct(self):
        # 创建一行文字
        text_left = Text("靠左对齐的文字", font="Noto Sans CJK", font_size=36, color=BLUE)

        # 将文字靠左对齐到屏幕的左边缘
        text_left.align_to(LEFT, LEFT)

        # 在场景中添加并显示文字
        self.add(text_left)
        self.play(FadeIn(text_left))
        self.wait(2)
