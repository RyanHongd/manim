from manim import *

class Combine(Scene):
    def construct(self):
        # 創建文字（使用者輸入的問題）
        self.create_title()

        # 創建文字和點的部分
        self.create_texts1()
        self.add_dots()

        # 顯示第一次加法答案
        self.show_answer1()

        # 創建扣掉的部分
        self.create_texts2()
        self.minus_dots()

        # 顯示最終答案
        self.show_answer2()
    
    def create_title(self):
        self.n1 = 31
        self.n2 = 10
        self.n3 = 8
        
        title = f"小名有{self.n1}塊錢，媽媽再給他{self.n2}塊錢，曉華又拿走他{self.n3}塊錢，請問小名最後有幾塊錢？"
        self.title = Text(title, font="Noto Sans CJK", font_size=33, color=YELLOW).to_edge(UP)
        self.title.scale_to_fit_width(14)
        self.play(Write(self.title))

    def create_texts1(self):
        # 定義問題和步驟文字
        n1 = self.n1
        n2 = self.n2
        
        text1 = f"首先我們有{n1}塊錢"
        text2 = f"媽媽再給我們{n2}塊"
        text3 = f"我們可以把十位數跟個位數分開"
        text4 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        text5 = f"{n2}可以被分成{n2 // 10}個10跟{n2 % 10}個1"
        text6 = f"最後數一數共有多少個1跟10"
        text7 = f"因此我們共有{n1 + n2}塊"

        # 創建文字物件
        steps = [Text(txt, font="Noto Sans CJK", font_size=30, color=GREEN) for txt in [text1, text2, text3, text4, text5, text6]]
        self.answer_text = Text(text7, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)

        # 顯示文字
        self.exp_g1 = VGroup(*steps).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.exp_g1.scale_to_fit_width(4)
        self.exp_g1.move_to(LEFT * 4)
        
        self.play(Succession(*[Write(step) for step in self.exp_g1]))
        self.wait(3)
        self.play(FadeOut(self.exp_g1))

    def add_dots(self):
        n1 = self.n1
        n2 = self.n2
        units1, tens1 = n1 % 10, n1 // 10
        units2, tens2 = n2 % 10, n2 // 10
        self.sum = n1 + n2
        
        # 創建個位數和十位數的點和圈
        unit_dots1 = [Dot(point=(i * 0.3 - 0.65, 0.5, 0), color=RED) for i in range(units1)]
        ten_circles1 = [VGroup(Circle(radius=0.3, color=RED).move_to((i * 0.6 - 0.65, 0, 0)), Text("10", font="Noto Sans CJK", font_size=24).move_to((i * 0.6 - 0.65, 0, 0))) for i in range(tens1)]
        
        unit_dots2 = [Dot(point=(i * 0.3 - 0.65, -1, 0), color=BLUE) for i in range(units2)]
        ten_circles2 = [VGroup(Circle(radius=0.3, color=BLUE).move_to((i * 0.6 - 0.65, -1.5, 0)), Text("10", font="Noto Sans CJK", font_size=24).move_to((i * 0.6 - 0.65, -1.5, 0))) for i in range(tens2)]
        
        # 顯示點
        for dot in unit_dots1 + ten_circles1 + unit_dots2 + ten_circles2:
            self.play(FadeIn(dot), run_time=0.1)

        # 移動個位數的點
        self.all_dots = unit_dots1 + unit_dots2
        self.all_circles = ten_circles1 + ten_circles2
        digits = units1 + units2
        tens_digits = tens1 + tens2
        
        i = digits
        for dot in self.all_dots:
            if i > digits - 10:
                self.play(dot.animate.move_to(RIGHT * ((digits - i) * 0.5 + 1) + UP * 1), run_time=0.5)
            else:
                self.play(dot.animate.move_to(RIGHT * ((digits - (i + 10)) * 0.5 + 1)), run_time=0.5)
            i -= 1

        # 十進位
        if digits >= 10:
            selected_dots = self.all_dots[:10]
            rect = SurroundingRectangle(VGroup(*selected_dots), color=BLUE, buff=0.3)
            self.play(Create(rect))
            for dot in selected_dots:
                self.remove(dot)
            circle = Circle(radius=0.3, color=RED).move_to(rect.get_center())
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            self.play(FadeIn(circle, text))
            self.all_circles.append(VGroup(circle, text))
            self.play(FadeOut(rect))

        # 移動十位數
        i = tens_digits
        for circle in self.all_circles:
            self.play(circle.animate.move_to(RIGHT * ((digits - i) * 0.5 + 1) + DOWN * 1), run_time=0.5)
            i -= 1

    def show_answer1(self):
        n1 = self.n1
        n2 = self.n2
        digits = n1 % 10 + n2 % 10
        tens_digits = n1 // 10 + n2 // 10
        if digits >= 10:
            digits -= 10
            tens_digits += 1

        digits_text = Text(str(digits), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + UP * 1)
        tens_digits_text = Text(str(tens_digits * 10), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + DOWN * 1)
        equal_text = Text("=", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 2.5)
        sum_text = Text(str(self.sum), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 3)

        self.ans1 = VGroup(digits_text, tens_digits_text, equal_text, sum_text).arrange(RIGHT, buff=0.5)
        self.ans1.scale_to_fit_width(4)
        self.ans1.move_to(DOWN * 2)
        
        self.play(Succession(*[Write(text) for text in self.ans1]))
        self.wait(3)

    def create_texts2(self):
        n1 = self.sum
        n2 = self.n3

        s1 = f"小名現在有{n1}塊錢"
        s2 = f"曉華拿走了{n2}塊"
        s3 = f"我們可以把十位數跟個位數分開"
        s4 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        s5 = f"要從{n1}拿出{n2}個"
        s6 = f"把要給的1拿出, 再把要給的10拿出"
        s7 = f"數數看剩下共有多少個"

        steps = [Text(txt, font="Noto Sans CJK", font_size=30, color=GREEN) for txt in [s1, s2, s3, s4, s5, s6]]
        self.exp_g2 = VGroup(*steps).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.exp_g2.scale_to_fit_width(4)
        self.exp_g2.move_to(LEFT * 4)

        self.play(Succession(*[Write(step) for step in self.exp_g2]))
        self.wait(3)
        self.play(FadeOut(self.exp_g2))

    def minus_dots(self):
        n1 = self.sum
        n2 = self.n3
        
        units1, tens1 = n1 % 10, n1 // 10
        units2, tens2 = n2 % 10, n2 // 10

        dots_to_remove = self.all_dots[-units2:]
        for dot in dots_to_remove:
            self.play(FadeOut(dot), run_time=0.1)
        
        for i in range(tens2):
            self.play(FadeOut(self.all_circles[-(i+1)]), run_time=0.1)

        remaining_units = units1 - units2
        remaining_tens = tens1 - tens2

        remaining_units_text = Text(str(remaining_units), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + UP * 1)
        remaining_tens_text = Text(str(remaining_tens * 10), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + DOWN * 1)
        equal_text = Text("=", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 2.5)
        final_sum = Text(str(remaining_tens * 10 + remaining_units), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 3)

        self.ans2 = VGroup(remaining_units_text, remaining_tens_text, equal_text, final_sum).arrange(RIGHT, buff=0.5)
        self.ans2.scale_to_fit_width(4)
        self.ans2.move_to(DOWN * 2)

    def show_answer2(self):
        self.play(Succession(*[Write(text) for text in self.ans2]))
        self.wait(3)























