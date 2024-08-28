from manim import *

class AddAndSubtract(Scene):
    def construct(self):
        # 加法部分
        n1 = 24
        n2 = 13
        s1 = f"小名有{n1}塊錢, 媽媽再給他{n2}塊錢, 現在共有多少塊?"
        s2 = f"首先我們有{n1}塊錢"
        s3 = f"媽媽再給我們{n2}塊"
        s4 = f"我們可以把十位數跟個位數分開"
        s5 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        s6 = f"{n2}可以被分成{n2 // 10}個10跟{n2 % 10}個1"
        s7 = f"把所有的1加起來, 再把所有的10加起來"
        s8 = f"最後再把十位數和個位數加起來"
        s9 = f"因此我們最後共有{n1 + n2}塊"

        title = Text(s1, font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
        exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=RED).move_to(LEFT * 4 + UP * 2)
        exp_2 = Text(s3, font="Noto Sans CJK", font_size=30, color=BLUE).move_to(UP * 2)
        exp_3 = Text(s4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        exp_4 = Text(s5, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4)
        exp_5 = Text(s6, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 1)
        exp_6 = Text(s7, font="Noto Sans CJK", font_size=30, color=WHITE).move_to(LEFT * 2 + UP * 2)
        exp_7 = Text(s8, font="Noto Sans CJK", font_size=30, color=WHITE).move_to(LEFT * 2 + UP * 2)
        ans = Text(s9, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)

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

        # 創建點
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

        # 打印點
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

        # 移動個位數的點
        all_dots = unit_dots1 + unit_dots2
        digits = units1 + units2
        all_circles = ten_circles1 + ten_circles2
        tens_digits = tens1 + tens2
        sum = n1 + n2
        i = digits

        self.wait(1)
        self.play(FadeOut(exp_1), FadeOut(exp_2), FadeOut(exp_3), FadeOut(exp_4), FadeOut(exp_5))
        self.play(Write(exp_6))
        for dot in all_dots:
            dot.set_color(GREEN)
            self.play(dot.animate.move_to(RIGHT * (((digits) // 2 - i) * 0.5) + UP * 1), run_time=0.5)
            i -= 1

        # 進位時創建框
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

        # 移動十位數的點
        i = tens_digits
        for circle in all_circles:
            circle[0].set_color(GREEN)
            circle[1].set_color(WHITE)
            self.play(circle.animate.move_to(RIGHT * ((tens_digits) // 2 - i) + DOWN * 1), run_time=0.5)
            i -= 1

        # 把答案顯示
        self.wait(1)
        self.play(FadeOut(exp_6))
        self.wait(1)
        self.play(Write(exp_7))
        digits_text = Text(str(digits), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + UP * 1)
        add_text = Text("+", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6)
        tens_digits_text = Text(str(tens_digits * 10), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + DOWN * 1)
        equal_text = Text("=", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 2.5)
        sum_text = Text(str(sum), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 3)
        self.play(Write(digits_text))
        self.play(Write(add_text))
        self.play(Write(tens_digits_text))
        self.wait(1)
        self.play(digits_text.animate.move_to(LEFT * 2 + DOWN * 2))
        self.play(add_text.animate.move_to(LEFT * 1 + DOWN * 2))
        self.play(tens_digits_text.animate.move_to(DOWN * 2))
        self.wait(1)
        self.play(equal_text.animate.move_to(RIGHT * 1 + DOWN * 2))
        self.play(sum_text.animate.move_to(RIGHT * 2 + DOWN * 2))
        self.wait(1)
        self.play(FadeOut(exp_7))

        self.play(Write(ans))
        self.wait(2)

        # 清除多餘內容
        self.play(FadeOut(title), FadeOut(ans), FadeOut(digits_text), FadeOut(add_text), FadeOut(tens_digits_text), FadeOut(equal_text), FadeOut(sum_text))
        for circle in all_circles:
            self.remove(circle)
        for dot in all_dots:
            self.remove(dot)

        # 減法部分
        n3 = 25
        n4 = 12
        s1 = f"小名有{n3}塊錢, 他買了一支{n4}塊錢的筆, 請問他還剩下多少塊?"
        s2 = f"首先我們有{n3}塊錢"
        s3 = f"這一次我們需要扣掉{n4}塊錢"
        s4 = f"{n3}可以被分成{n3 // 10}個10跟{n3 % 10}個1"
        s5 = f"我們將需要減掉{n4 // 10}個10和{n4 % 10}個1"
        s6 = f"最後再把十位數和個位數的結果加起來"
        s7 = f"因此我們最後還有{n3 - n4}塊"

        title = Text(s1, font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
        exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=RED).move_to(LEFT * 4 + UP * 2)
        exp_2 = Text(s3, font="Noto Sans CJK", font_size=30, color=BLUE).move_to(UP * 2)
        exp_3 = Text(s4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        exp_4 = Text(s5, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4)
        exp_5 = Text(s6, font="Noto Sans CJK", font_size=30, color=WHITE).move_to(LEFT * 2 + UP * 2)
        ans = Text(s7, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)

        # 打印文字
        self.play(Write(title))
        self.wait(1)
        self.play(Write(exp_1))
        self.wait(1)

        # 創建點
        units1 = n3 % 10
        tens1 = n3 // 10
        units2 = n4 % 10
        tens2 = n4 // 10

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

        # 打印點
        for dot in unit_dots1:
            self.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles1:
            self.play(FadeIn(circle), run_time=0.1)
        self.wait(1)

        self.play(Write(exp_3))
        self.wait(1)

        # 進行借位
        if units1 < units2:
            self.play(FadeOut(unit_dots1[-1]))
            circle = Circle(radius=0.3, color=RED).move_to((units1 * 0.3 - 0.65, 0.5, 0))
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            self.play(FadeIn(circle, text))
            unit_dots1.append(Dot(point=((units1 + 9) * 0.3 - 0.65, 0.5, 0), color=RED))

        # 扣減
        for i in range(units2):
            self.play(FadeOut(unit_dots1[-(i + 1)]), run_time=0.5)
        for i in range(tens2):
            self.play(FadeOut(ten_circles1[-(i + 1)]), run_time=0.5)

        self.play(Write(exp_4))
        self.wait(1)
        self.play(Write(exp_5))
        self.wait(1)

        # 將剩餘的點移到新的位置
        remaining_unit_dots = unit_dots1[:-units2]
        remaining_ten_circles = ten_circles1[:-tens2]

        for i, dot in enumerate(remaining_unit_dots):
            self.play(dot.animate.move_to(RIGHT * (((len(remaining_unit_dots)) // 2 - i) * 0.5) + UP * 1), run_time=0.5)

        for i, circle in enumerate(remaining_ten_circles):
            self.play(circle.animate.move_to(RIGHT * (((len(remaining_ten_circles)) // 2 - i) * 0.5) + DOWN * 1), run_time=0.5)

        # 把答案顯示
        self.wait(1)
        self.play(FadeOut(exp_4))
        self.wait(1)
        self.play(Write(exp_6))
        remaining_digits = len(remaining_unit_dots)
        remaining_tens_digits = len(remaining_ten_circles)

        digits_text = Text(str(remaining_digits), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + UP * 1)
        add_text = Text("-", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6)
        tens_digits_text = Text(str(remaining_tens_digits * 10), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + DOWN * 1)
        equal_text = Text("=", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 2.5)
        sum_text = Text(str(n3 - n4), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 3)
        self.play(Write(digits_text))
        self.play(Write(add_text))
        self.play(Write(tens_digits_text))
        self.wait(1)
        self.play(digits_text.animate.move_to(LEFT * 2 + DOWN * 2))
        self.play(add_text.animate.move_to(LEFT * 1 + DOWN * 2))
        self.play(tens_digits_text.animate.move_to(DOWN * 2))
        self.wait(1)
        self.play(equal_text.animate.move_to(RIGHT * 1 + DOWN * 2))
        self.play(sum_text.animate.move_to(RIGHT * 2 + DOWN * 2))
        self.wait(1)

        self.play(FadeOut(exp_6))
        self.play(Write(ans))
        self.wait(2)



