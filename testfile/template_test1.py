from manim import *

class Add3And4Dot(Scene):
    def construct(self):
        # 故事情節
        n1 = 24
        n2 = 13
        n3 = 8
        s1 = f"小名有{n1}塊錢, 媽媽再給他{n2}塊錢, 現在共有幾塊?"
        s2 = f"首先我們有{n1}塊錢"
        s3 = f"媽媽再給我們{n2}塊"
        s4 = f"我們可以把十位數和個位數分開"
        s5 = f"{n1}可以分成{n1 // 10}個10和{n1 % 10}個1"
        s6 = f"{n2}可以分成{n2 // 10}個10和{n2 % 10}個1"
        s7 = f"把所有的1加起來, 再把所有的10加起來"
        s8 = f"最後再把十位數和個位數加起來"
        s9 = f"現在共有{n1 + n2}塊錢"

        s10 = f"現在曉華拿走{n3}塊錢, 剩下多少塊?"
        s11 = f"我們有{n1 + n2}塊錢"
        s12 = f"曉華拿走了{n3}塊"
        s13 = f"我們可以把剩下的錢分開"
        s14 = f"{n1 + n2}可以分成{(n1 + n2) // 10}個10和{(n1 + n2) % 10}個1"
        s15 = f"我們要從中減去{n3}"
        s16 = f"因此最後剩下{n1 + n2 - n3}塊錢"

        # 題目陳述
        title = Text(s1, font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)

        # 加法部分陳述
        exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=RED).move_to(LEFT * 4 + UP * 2)
        exp_2 = Text(s3, font="Noto Sans CJK", font_size=30, color=BLUE).move_to(UP * 2)
        exp_3 = Text(s4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        exp_4 = Text(s5, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4)
        exp_5 = Text(s6, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 1)
        exp_6 = Text(s7, font="Noto Sans CJK", font_size=30, color=WHITE).move_to(LEFT * 2 + UP * 2)
        exp_7 = Text(s8, font="Noto Sans CJK", font_size=30, color=WHITE).move_to(LEFT * 2 + UP * 2)
        ans = Text(s9, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)
        
        # 數字分解
        units1 = n1 % 10
        tens1 = n1 // 10
        units2 = n2 % 10
        tens2 = n2 // 10
        
        unit_dots1 = []
        ten_circles1 = []
        unit_dots2 = []
        ten_circles2 = []

        # 個位數和十位數的點和圓圈表示
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
        
        # 動畫開始
        self.play(Write(title))
        self.wait(1)
        self.play(Write(exp_1))
        self.wait(1)
        self.play(Write(exp_2))
        self.wait(1)
        self.play(Write(exp_3))
        self.wait(1)

        # 顯示數字的分解
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
        
        # 移動並合併點和圓圈
        all_dots = unit_dots1 + unit_dots2
        digits = units1 + units2
        all_circles = ten_circles1 + ten_circles2
        tens_digits = tens1 + tens2
        sum_value = n1 + n2

        self.wait(1)
        self.play(FadeOut(exp_1), FadeOut(exp_2), FadeOut(exp_3), FadeOut(exp_4), FadeOut(exp_5))

        self.play(Write(exp_6))
        i = digits
        for dot in all_dots:
            dot.set_color(GREEN)
            self.play(dot.animate.move_to(RIGHT * (((digits)//2-i)*0.5) + UP *1), run_time=0.5)
            i -= 1

        # 如果超過10點，進位
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

        i = tens_digits
        for circle in all_circles:
            circle[0].set_color(GREEN)
            circle[1].set_color(WHITE)
            self.play(circle.animate.move_to(RIGHT * ((tens_digits)//2-i)+ DOWN * 1), run_time=0.5)
            i -= 1
        
        self.wait(1)
        self.play(FadeOut(exp_6))
        self.play(Write(exp_7))
        
        # 最後顯示加法結果
        digits_text = Text(str(digits), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + UP *1)
        add_text = Text("+", font="Noto Sans CJK", font_size=40).next_to(digits_text, LEFT)
        tens_digits_text = Text(str(tens_digits)+"0", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6+ DOWN * 1)
        total_text = Text("=", font="Noto Sans CJK", font_size=40).next_to(digits_text, RIGHT)
        sum_text = Text(str(sum_value), font="Noto Sans CJK", font_size=40).next_to(total_text, RIGHT)

        self.play(Write(add_text))
        self.play(Write(digits_text))
        self.play(Write(tens_digits_text))
        self.play(Write(total_text))
        self.play(Write(sum_text))

        self.wait(1)
        self.play(Write(ans))
        self.wait(2)
        
        # 減法部分
        
        # 移除加法圖像
        self.play(FadeOut(VGroup(add_text, digits_text, tens_digits_text, total_text, sum_text, ans)))
        
        title_2 = Text(s10, font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
        ans_2 = Text(s16, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)
        self.play(Write(title_2))
        self.wait(1)

        # 減法步驟
        exp_1 = Text(s11, font="Noto Sans CJK", font_size=30, color=RED).move_to(LEFT * 4 + UP * 2)
        exp_2 = Text(s12, font="Noto Sans CJK", font_size=30, color=BLUE).move_to(UP * 2)
        self.play(Write(exp_1))
        self.wait(1)
        self.play(Write(exp_2))
        self.wait(1)
        remaining_value = sum_value - n3
        remaining_digits = remaining_value % 10
        remaining_tens_digits = remaining_value // 10

        # 顯示剩餘
        remaining_digits_text = Text(str(remaining_digits), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + UP *1)
        subtract_text = Text("-", font="Noto Sans CJK", font_size=40).next_to(remaining_digits_text, LEFT)
        remaining_tens_digits_text = Text(str(remaining_tens_digits)+"0", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6+ DOWN * 1)
        equal_text_2 = Text("=", font="Noto Sans CJK", font_size=40).next_to(remaining_digits_text, RIGHT)
        remaining_sum_text = Text(str(remaining_value), font="Noto Sans CJK", font_size=40).next_to(equal_text_2, RIGHT)

        self.play(Write(subtract_text))
        self.play(Write(remaining_digits_text))
        self.play(Write(remaining_tens_digits_text))
        self.play(Write(equal_text_2))
        self.play(Write(remaining_sum_text))
        self.play(Write(ans_2))
        self.wait(2)














