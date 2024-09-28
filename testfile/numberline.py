from manim import *

class Add5And4NumberLine(Scene):
    def construct(self):
        # 創建題目
        title = Text("小明有5個糖果, 媽媽再給他4個, 現在共有幾個?", font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)

        # 創建數線
        number_line = NumberLine(
            x_range=[0, 10, 1],
            length=10,
            color=WHITE,
            include_numbers=True,
            label_direction=UP,
        ).shift(DOWN)

        # 創建標記點
        dot1 = Dot(color=RED).move_to(number_line.n2p(5))
        dot_label1 = Text("5", font_size=36, color=RED).next_to(dot1, DOWN)

        dot2 = Dot(color=RED).move_to(number_line.n2p(4))
        dot_label2 = Text("4", font_size=36, color=RED).next_to(dot2, DOWN)

        line1 = Line(start=number_line.n2p(0), end=number_line.n2p(5), color=BLUE)
        line2 = Line(start=number_line.n2p(0), end=number_line.n2p(4), color=GREEN)
        # 動畫效果
        self.play(Write(title))
        self.wait(1)
        self.play(Create(number_line))
        self.play(FadeIn(dot1, dot_label1))
        self.play(FadeIn(line1))
        self.wait(1)
        self.play(FadeIn(dot2, dot_label2))
        self.play(FadeIn(line2))
        self.wait(1)

        # 移動點表示加法過程
        self.play(dot2.animate.move_to(number_line.n2p(9)), run_time=2)
        self.play(line2.animate.move_to(number_line.n2p(7)), run_time=2)
        self.play(Transform(dot_label2, Text("9", font_size=36, color=RED).next_to(dot2, DOWN)))
        self.wait(2)