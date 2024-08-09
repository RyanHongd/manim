from manim import *

class Add3And4Dot(Scene):
    def construct(self):
        # 题目信息
        n1 = 24
        n2 = 13
        n3 = 8
        s1 = f"小名有{n1}块钱，妈妈再给他{n2}块钱，晓华又拿走他{n3}块钱，"
        s2 = f"请问小名最后有几块钱?"
        s3 = f"首先我们有{n1}块钱"
        s4 = f"妈妈再给我们{n2}块"
        s5 = f"{n1}可以被分成{n1 // 10}个10跟{n1 % 10}个1"
        s6 = f"{n2}可以被分成{n2 // 10}个10跟{n2 % 10}个1"
        s7 = f"把所有的1加起来, 再把所有的10加起来"
        s8 = f"现在我们有{n1 + n2}块"
        s9 = f"接着晓华拿走了{n3}块"
        s10 = f"我们把{n3}块分开成{n3 // 10}个10和{n3 % 10}个1"
        s11 = f"因此小名最后有{n1 + n2 - n3}块钱"

        # 题目显示
        title1 = Text(s1, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(UP)
        title2 = Text(s2, font="Noto Sans CJK", font_size=30, color=YELLOW).next_to(title1, DOWN)
        exp_1 = Text(s3, font="Noto Sans CJK", font_size=28, color=RED).move_to(LEFT * 4 + UP * 2)
        exp_2 = Text(s4, font="Noto Sans CJK", font_size=28, color=BLUE).move_to(UP * 2)
        exp_3 = Text(s5, font="Noto Sans CJK", font_size=28, color=GREEN).move_to(LEFT * 4 + UP * 1)
        exp_4 = Text(s6, font="Noto Sans CJK", font_size=28, color=GREEN).move_to(LEFT * 4)
        exp_5 = Text(s7, font="Noto Sans CJK", font_size=28, color=WHITE).move_to(LEFT * 2 + UP * 2)
        exp_6 = Text(s8, font="Noto Sans CJK", font_size=28, color=YELLOW).move_to(UP * 1)
        exp_7 = Text(s9, font="Noto Sans CJK", font_size=28, color=RED).move_to(LEFT * 4 + UP * 1)
        exp_8 = Text(s10, font="Noto Sans CJK", font_size=28, color=GREEN).move_to(LEFT * 4)
        exp_9 = Text(s11, font="Noto Sans CJK", font_size=28, color=YELLOW).to_edge(DOWN)

        # 创建点和圆圈
        units1 = n1 % 10
        tens1 = n1 // 10
        units2 = n2 % 10
        tens2 = n2 // 10
        units3 = n3 % 10
        tens3 = n3 // 10

        unit_dots1 = []
        ten_circles1 = []
        unit_dots2 = []
        ten_circles2 = []

        # 第一部分：n1 的点和圆圈
        for j in range(units1):
            dot = Dot(point=(j * 0.3 - 0.65, 0.5, 0), color=RED)
            unit_dots1.append(dot)
        
        for i in range(tens1):
            circle = Circle(radius=0.3, color=RED).move_to((i * 0.6 - 0.65, 0, 0))
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            ten_circles1.append(VGroup(circle, text))

        # 第二部分：n2 的点和圆圈
        for i in range(units2):
            dot = Dot(point=(i * 0.3 - 0.65, -1, 0), color=BLUE)
            unit_dots2.append(dot)
        
        for i in range(tens2):
            circle = Circle(radius=0.3, color=BLUE).move_to((i * 0.6 - 0.65, -1.5, 0))
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            ten_circles2.append(VGroup(circle, text))
        
        # 显示题目和初始点
        self.play(Write(title1))
        self.play(Write(title2))
        self.wait(1)
        self.play(Write(exp_1))
        self.wait(1)
        self.play(Write(exp_2))
        self.wait(1)
        self.play(Write(exp_3))
        self.wait(1)

        # 显示所有 n1 的点和圆圈
        for dot in unit_dots1:
            self.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles1:
            self.play(FadeIn(circle), run_time=0.1)
        self.wait(1)

        # 显示 n2 的点和圆圈
        self.play(Write(exp_4))
        self.wait(1)
        for dot in unit_dots2:
            self.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles2:
            self.play(FadeIn(circle), run_time=0.1)
        self.wait(1)
        
        # 移动点和圆圈，显示加法结果
        self.play(FadeOut(exp_1), FadeOut(exp_2), FadeOut(exp_3), FadeOut(exp_4))
        self.play(Write(exp_5))
        all_dots = unit_dots1 + unit_dots2
        digits = units1 + units2
        all_circles = ten_circles1 + ten_circles2
        tens_digits = tens1 + tens2

        i = digits
        for dot in all_dots:
            dot.set_color(GREEN)
            self.play(dot.animate.move_to(RIGHT * (((digits) // 2 - i) * 0.5) + UP * 1), run_time=0.5)
            i -= 1

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
            self.play(circle.animate.move_to(RIGHT * ((tens_digits) // 2 - i) + DOWN * 1), run_time=0.5)
            i -= 1

        self.wait(1)
        self.play(FadeOut(exp_5))
        self.play(Write(exp_6))
        self.wait(1)

        # 显示减法部分
        self.play(Write(exp_7))
        self.wait(1)
        self.play(Write(exp_8))

        if digits < units3:
            tens_digits -= 1
            digits += 10
            self.play(all_circles[-1].animate.move_to(DOWN * 1.5))
            for j in range(j + 10):
                dot = Dot(point=((j + 1) * 0.3 - 0.65, 0.5, 0), color=YELLOW)
                self.play(FadeIn(dot), run_time=0.1)
                all_dots.append(dot)
            self.wait(2)

        selected_dots = all_dots[:units3]
        selected_circles = all_circles[:tens3]

        for dot in selected_dots:
            dot.set_color(BLUE)
            self.play(dot.animate.move_to(RIGHT * (all_dots.index(dot) * 0.3 - 0.65) + UP * 2), run_time=0.5)

        for circle in selected_circles:
            self.play(circle.animate.move_to(UP * 2))

        self.play(FadeOut(exp_7), FadeOut(exp_8))
        self.play(Write(exp_9))
        self.wait(2)











