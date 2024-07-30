from manim import *

class Add5And4dot(Scene):
    def construct(self):
        # 創建題目
        title = Text("小明有5個糖果, 媽媽再給他4個, 現在共有幾個?", font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)

        dots1 = []
        dots2 = []
        # 使用迴圈創建多個點並將它們添加到列表中
        for i in range(5):
            dot = Dot(point=(i-3, 0, 0), color=RED)
            dots1.append(dot)
        # 使用迴圈創建多個點並將它們添加到列表中
        for i in range(4):
            dot = Dot(point=(i-3, -1, 0), color=BLUE)
            dots2.append(dot)
        
        
        self.play(Write(title))
        self.wait(1)
        # 顯示所有點
        for dot in dots1:
            self.play(FadeIn(dot))

        self.wait(2)
        
        for dot in dots2:
            self.play(FadeIn(dot))
        

        # 移動點表示加法過程
        #self.play(dot2.animate.move_to(number_line.n2p(9)), run_time=2)
        #self.play(line2.animate.move_to(number_line.n2p(7)), run_time=2)
        #self.play(Transform(dot_label2, Text("9", font_size=36, color=RED).next_to(dot2, DOWN)))
        #self.wait(2)