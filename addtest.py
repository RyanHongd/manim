from manim import *


class Test(Scene):
    def construct(self):
        # 創建數字
        five = Text("3", font_size=96, color=BLUE)
        plus = Text("+", font_size=96)
        four = Text("9", font_size=96, color=GREEN)
        equals = Text("=", font_size=96)
        nine = Text("12", font_size=96, color=RED)

        # 設置位置
        five.shift(LEFT * 3)
        plus.next_to(five, RIGHT)
        four.next_to(plus, RIGHT)
        equals.next_to(four, RIGHT)
        nine.next_to(equals, RIGHT)

        # 動畫效果
        self.play(Write(five))
        self.play(Write(plus))
        self.play(Write(four))
        self.play(Write(equals))
        #self.play(TransformFromCopy(five, nine))
        #self.play(TransformFromCopy(four, nine))
        self.play(Write(nine))

        # 停留一會兒
        self.wait(2)

# To render the video, run:
