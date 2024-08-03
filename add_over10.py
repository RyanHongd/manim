from manim import *

class Add5And4dot(Scene):
    def construct(self):
        # 創建題目(使用者輸入的問題)
        n1 = 31
        n2 = 54
        s1 = f"小明有{n1}個糖果, 媽媽拿走他{n2}個, 現在共有幾個?"
        s2 = f"首先我們有{n1}顆糖果"
        s3 = f"媽媽再給我們{n2}顆"
        s4 = f"我們可以把{n1}的十位數跟個位數分開"
        s4 = f"因此我們最後剩下{n1-n2}顆"
        title = Text(s1, font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
        exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=RED).move_to(LEFT * 4 + UP * 0)
        exp_2 = Text(s3, font="Noto Sans CJK", font_size=30, color=BLUE).move_to(LEFT * 4 + DOWN * 1)
        ans = Text(s4, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)
        dots1 = []
        # 使用迴圈創建多個點並將它們添加到列表中
        for i in range(n1):
            dot = Dot(point=(i-1, 0, 0), color=RED)
            dots1.append(dot)
        
        #影片流程
        self.play(Write(title))
        self.wait(1)
        self.play(Write(exp_1))
        # 顯示所有點
        for dot in dots1:
            self.play(FadeIn(dot))

        self.wait(1)
        self.play(Write(exp_2))
        selected_dots = dots1[:n2]
        i = n1
        for dot in selected_dots:
            dot.set_color(BLUE)
            self.play(dot.animate.move_to(RIGHT * (i-n1) + DOWN * 1), run_time=0.5)
            i += 1


        self.play(FadeOut(exp_1), FadeOut(exp_2))
        i=n1
        dots1 = [dot for dot in dots1 if dot not in selected_dots]
        for dot in dots1:
            dot.set_color(GREEN)
            self.play(dot.animate.move_to(LEFT * (i - 5) + DOWN * 2), run_time=0.5)
            i -= 1
        for dot in selected_dots:
            self.remove(dot)
        self.play(Write(ans))
        self.wait(2)
        # 移動點表示加法過程
        #self.play(dot2.animate.move_to(number_line.n2p(9)), run_time=2)
        #self.play(line2.animate.move_to(number_line.n2p(7)), run_time=2)
        #self.play(Transform(dot_label2, Text("9", font_size=36, color=RED).next_to(dot2, DOWN)))
        #self.wait(2)