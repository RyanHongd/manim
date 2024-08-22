from manim import *

class CombinedAddSubtractDot(Scene):
    def construct(self):
        # 創建題目（使用者輸入的問題）
        initial_money = 24
        received_money = 13
        spent_money = 8
        final_amount = initial_money + received_money - spent_money

        s1 = f"小名有{initial_money}塊錢，媽媽再給他{received_money}塊錢，曉華又拿走他{spent_money}塊錢，請問小名最後有幾塊錢?"
        s2 = f"首先我們有{initial_money}塊錢"
        s3 = f"媽媽再給我們{received_money}塊錢"
        s4 = f"曉華拿走了{spent_money}塊錢"
        s5 = f"我們可以把所有的數字分開處理"
        s6 = f"{initial_money}可以被分成{initial_money // 10}個10塊錢跟{initial_money % 10}塊錢"
        s7 = f"{received_money}可以被分成{received_money // 10}個10塊錢跟{received_money % 10}塊錢"
        s8 = f"{spent_money}可以被分成{spent_money // 10}個10塊錢跟{spent_money % 10}塊錢"
        s9 = f"首先加上媽媽給的錢，然後再減去曉華拿走的錢"
        s10 = f"因此我們最後有{final_amount}塊錢"

        title = Text(s1, font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
        exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=RED).move_to(LEFT * 4 + UP * 2)
        exp_2 = Text(s3, font="Noto Sans CJK", font_size=30, color=BLUE).move_to(UP * 2)
        exp_3 = Text(s4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        exp_4 = Text(s5, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4)
        exp_5 = Text(s6, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 1)
        exp_6 = Text(s7, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 2)
        exp_7 = Text(s8, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 3)
        exp_8 = Text(s9, font="Noto Sans CJK", font_size=30, color=WHITE).move_to(LEFT * 2 + UP * 2)
        ans = Text(s10, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)

        # 題目流程
        self.play(Write(title))
        self.wait(1)
        self.play(Write(exp_1))
        self.wait(1)
        self.play(Write(exp_2))
        self.wait(1)
        self.play(Write(exp_3))
        self.wait(1)
        
        units1 = initial_money % 10
        tens1 = initial_money // 10
        units2 = received_money % 10
        tens2 = received_money // 10
        units3 = spent_money % 10
        tens3 = spent_money // 10

        unit_dots1 = []
        ten_circles1 = []
        unit_dots2 = []
        ten_circles2 = []
        unit_dots3 = []
        ten_circles3 = []

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
        
        for i in range(units3):
            dot = Dot(point=(i * 0.3 - 0.65, -3, 0), color=GREEN)
            unit_dots3.append(dot)
        
        for i in range(tens3):
            circle = Circle(radius=0.3, color=GREEN).move_to((i * 0.6 - 0.65, -3.5, 0))
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            ten_circles3.append(VGroup(circle, text))
        


        # 顯示所有點
        self.play(Write(exp_4))
        self.wait(1)        
        for dot in unit_dots1:
            self.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles1:
            self.play(FadeIn(circle), run_time=0.1)
        self.wait(1)
        
        self.play(Write(exp_5))
        self.wait(1)
        for dot in unit_dots2:
            self.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles2:
            self.play(FadeIn(circle), run_time=0.1)
        
        self.play(Write(exp_6))
        self.wait(1)
        for dot in unit_dots3:
            self.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles3:
            self.play(FadeIn(circle), run_time=0.1)

        #顯示文字
        all_dots = unit_dots1 + unit_dots2 + unit_dots3
        all_circles = ten_circles1 + ten_circles2 + ten_circles3
        sum_dots = units1 + units2 - units3
        sum_circles = tens1 + tens2 - tens3
        
        self.wait(1)
        self.play(FadeOut(exp_1), FadeOut(exp_2), FadeOut(exp_3), FadeOut(exp_4), FadeOut(exp_5), FadeOut(exp_6))
        
        #加法
        self.play(Write(exp_8))
        digits = sum_dots
        tens_digits = sum_circles

        #移動個位數的點
        i = digits
        for dot in all_dots:
            dot.set_color(GREEN)
            self.play(dot.animate.move_to(RIGHT * (((digits)//2-i)*0.5) + UP *1), run_time=0.5)
            i -= 1
        
        #創建框
        if digits > 10:
            digits -= 10
            tens_digits += 1
            selected_dots = all_dots[:10]
            dots_group = VGroup(*selected_dots)
            rect = SurroundingRectangle(dots_group, color=BLUE, buff=0.3)
            self.play(Create(rect))
            self.wait(2)
            for dot in selected_dots:
                self.remove(dot)
            circle = Circle(radius=0.3, color=RED).move_to((-2, 1, 0))
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            self.play(FadeIn(circle, text))
            all_circles.append(VGroup(circle, text))
            self.wait(1)
            self.play(FadeOut(rect))
        
        #移動十位數的點
        i = tens_digits
        for circle in all_circles:
            circle[0].set_color(GREEN)
            circle[1].set_color(WHITE)
            self.play(circle.animate.move_to(RIGHT * ((tens_digits)//2-i)+ DOWN * 1), run_time=0.5)
            i -= 1
        
        self.wait(1)
        self.play(FadeOut(exp_8))
        self.play(Write(ans))
        self.wait(2)

