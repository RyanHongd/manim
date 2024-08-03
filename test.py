from manim import *

class Add3And4dot(Scene):
    def construct(self):
        # 創建題目(使用者輸入的問題)
        n1 = 3
        n2 = 4
        s1 = f"曉華現在有{n1}塊錢, 爸爸再給他{n2}塊錢, 請問他現在有幾塊錢?"
        s2 = f"首先我們有{n1}塊錢"
        s3 = f"爸爸多給我們{n2}塊錢"
        s4 = f"因此我們最後有{n1+n2}塊錢"
        title = Text(s1, font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
        exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=RED).move_to(LEFT * 3 + UP * 0)
        exp_2 = Text(s3, font="Noto Sans CJK", font_size=30, color=BLUE).move_to(LEFT * 3 + DOWN * 1)
        ans = Text(s4, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)
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
        
        i = n1 + n2
        for dot in dots1:
            self.play(dot.animate.move_to(LEFT * (i - 4) + DOWN * 2), run_time=0.5)
            i -= 1
        
        for dot in dots2:
            self.play(dot.animate.move_to(LEFT * (i - 4) + DOWN * 2), run_time=0.5)
            i -= 1
        
        self.play(FadeOut(exp_1), FadeOut(exp_2))
        
        for dot in dots1 + dots2:
            dot.set_color(GREEN)
        
        self.play(Write(ans))
        self.wait(2)
