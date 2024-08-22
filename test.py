from manim import *

class Add3And4Dot(Scene):
    def construct(self):
        # 創建文字（使用者輸入的問題）
        n1 = 24
        n2 = 13
        n3 = 8
        s1 = f"小名有{n1}塊錢，媽媽再給他{n2}塊錢，曉華又拿走他{n3}塊錢，請問小名最後有幾塊錢?"
        s2 = f"首先小名有{n1}塊錢"
        s3 = f"媽媽再給他{n2}塊錢"
        s4 = f"我們可以把十位數跟個位數分開"
        s5 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        s6 = f"{n2}可以被分成{n2 // 10}個10跟{n2 % 10}個1"
        s7 = f"把所有的1加起來，再把所有的10加起來"
        s8 = f"小名現在總共有{n1 + n2}塊錢"
        s9 = f"但是曉華拿走了{n3}塊錢"
        s10 = f"我們需要從{n1 + n2}中拿走{n3}個"
        s11 = f"因此小名最後剩下{n1 + n2 - n3}塊錢"
        
        title = Text(s1, font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
        exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=RED).move_to(LEFT * 4 + UP * 2)
        exp_2 = Text(s3, font="Noto Sans CJK", font_size=30, color=BLUE).move_to(UP * 2)
        exp_3 = Text(s4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        exp_4 = Text(s5, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4)
        exp_5 = Text(s6, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 1)
        exp_6 = Text(s7, font="Noto Sans CJK", font_size=30, color=WHITE).move_to(LEFT * 2 + UP * 2)
        exp_7 = Text(s8, font="Noto Sans CJK", font_size=30, color=YELLOW).move_to(LEFT * 4 + UP * 2)
        exp_8 = Text(s9, font="Noto Sans CJK", font_size=30, color=ORANGE).move_to(UP * 2)
        exp_9 = Text(s10, font="Noto Sans CJK", font_size=30, color=WHITE).move_to(LEFT * 3 + UP * 2)
        ans = Text(s11, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)

        # 打印文字
        self.play(Write(title))
        self.wait(1)
        self.play(Write(exp_1))
        self.wait(1)
        self.play(Write(exp_2))
        self.wait(1)
        self.play(Write(exp_3))
        self.wait(1)
        self.play(Write(exp_4))
        self.wait(1)
        self.play(Write(exp_5))
        self.wait(1)

        # 創建點和圈（錢）
        units1 = n1 % 10
        tens1 = n1 // 10
        units2 = n2 % 10
        tens2 = n2 // 10
        
        unit_dots1 = []
        ten_circles1 = []
        unit_dots2 = []
        ten_circles2 = []
        
        for i in range(units1):
            dot = Dot(point=(i * 0.3 - 0.65, 0.5, 0), color=RED)
            unit_dots1.append(dot)
        
        for i in range(tens1):
            circle = Circle(radius=0.3, color=RED).move_to((i * 0.6 - 0.65, 0, 0))
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            ten_circles1.append(VGroup(circle, text))
        
        for i in range(units2):
            dot = Dot(point=(i * 0.3 - 0.65, -1, 0), color=BLUE)
            unit_dots2.append(dot)
        
        for i in range(tens2):
            circle = Circle(radius=0.3, color=BLUE).move_to((i * 0.6 - 0.65, -1.5, 0))
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            ten_circles2.append(VGroup(circle, text))
        
        # 打印點和圈     
        for dot in unit_dots1 + unit_dots2:
            self.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles1 + ten_circles2:
            self.play(FadeIn(circle), run_time=0.1)
        self.wait(1)

        # 加法部分
        self.play(FadeOut(exp_1), FadeOut(exp_2), FadeOut(exp_3), FadeOut(exp_4), FadeOut(exp_5))
        self.play(Write(exp_6))
        
        all_dots = unit_dots1 + unit_dots2
        all_circles = ten_circles1 + ten_circles2
        
        for i, dot in enumerate(all_dots):
            dot.set_color(GREEN)
            self.play(dot.animate.move_to(RIGHT * ((len(all_dots)//2-i)*0.5) + UP *1), run_time=0.1)

        for i, circle in enumerate(all_circles):
            circle[0].set_color(GREEN)
            circle[1].set_color(WHITE)
            self.play(circle.animate.move_to(RIGHT * ((len(all_circles)//2-i)) + DOWN * 1), run_time=0.1)

        self.wait(1)
        self.play(FadeOut(exp_6))
        self.play(Write(exp_7))
        self.wait(1)

        # 減法部分
        self.play(FadeOut(exp_7))
        self.play(Write(exp_8))
        self.wait(1)
        self.play(Write(exp_9))
        self.wait(1)

        # 移除曉華拿走的錢
        removed_dots = all_dots[-n3:]
        for dot in removed_dots:
            dot.set_color(ORANGE)
            self.play(dot.animate.move_to(DOWN * 2), run_time=0.1)
            self.play(FadeOut(dot), run_time=0.1)

        # 重新排列剩下的錢
        remaining_dots = all_dots[:-n3]
        for i, dot in enumerate(remaining_dots):
            self.play(dot.animate.move_to(RIGHT * ((len(remaining_dots)//2-i)*0.5) + UP *1), run_time=0.1)

        self.play(Write(ans))
        self.wait(2)
















