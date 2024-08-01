from manim import *

class Add5And4dot(Scene):
    def construct(self):
        # 創建題目(使用者輸入的問題)
        n1 = 5
        n2 = 4
        title = Text(f"小明有{n1}個糖果, 媽媽再給他{n2}個, 現在共有幾個?", font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
        exp_1 = Text(f"首先我們有{n1}顆糖果", font="Noto Sans CJK", font_size=30, color=RED).move_to(LEFT * 3 + UP * 0)
        exp_2 = Text(f"媽媽多給我們{n2}顆", font="Noto Sans CJK", font_size=30, color=BLUE).move_to(LEFT * 3 + DOWN * 1)
        ans = Text(f"因此我們最後有{n1+n2}顆", font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)
        dots1 = []
        dots2 = []
        # 使用迴圈創建多個點並將它們添加到列表中
        for i in range(n1):
            dot = Dot(point=(i, 0, 0), color=RED)
            dots1.append(dot)
        # 使用迴圈創建多個點並將它們添加到列表中
        for i in range(n2):
            dot = Dot(point=(i, -1, 0), color=BLUE)
            dots2.append(dot)
        
        
        self.play(Write(title))
        self.wait(1)
        self.play(Write(exp_1))
        # 顯示所有點
        for dot in dots1:
            self.play(FadeIn(dot))

        self.wait(1)
        self.play(Write(exp_2))
        for dot in dots2:
            self.play(FadeIn(dot))
        self.play(Write(ans))
        self.wait(2)
        # 移動點表示加法過程
        #self.play(dot2.animate.move_to(number_line.n2p(9)), run_time=2)
        #self.play(line2.animate.move_to(number_line.n2p(7)), run_time=2)
        #self.play(Transform(dot_label2, Text("9", font_size=36, color=RED).next_to(dot2, DOWN)))
        #self.wait(2)