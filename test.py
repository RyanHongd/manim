from manim import *

class Subtract_Function(Scene):
    def construct(self):
        # 創建文字（使用者輸入的問題）
        self.create_texts()

        # 創建點和圈
        self.create_dots_and_circles()

        # 顯示答案
        self.show_answer()

    def create_texts(self):
        # 定義問題和步驟文字
        n1 = 39
        n2 = 59
        a1 = f"小明有{n1}個糖果, 媽媽再給他{n2}個, 現在共有幾個?"
        a2 = f"首先我們有{n1}顆糖果"
        a3 = f"媽媽再給我們{n2}顆"
        a4 = f"我們可以把十位數跟個位數分開"
        a5 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        a6 = f"{n2}可以被分成{n2 // 10}個10跟{n2 % 10}個1"
        a7 = f"數一數共有多少個1跟10"
        a8 = f"因此我們最後共有{n1 + n2}顆"

        # 創建文字物件
        self.title = Text(a1, font="Noto Sans CJK", font_size=33, color=YELLOW).to_edge(UP)
        self.exp_1 = Text(a2, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 2)
        self.exp_2 = Text(a3, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        self.exp_3 = Text(a4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4)
        self.exp_4 = Text(a5, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 1)
        self.exp_5 = Text(a6, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 2)
        self.exp_6 = Text(a7, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        self.ans = Text(a8, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)

        # 顯示文字
        self.play(Write(self.title))
        self.wait(1)
        self.play(Write(self.exp_1))
        self.wait(1)
        self.play(Write(self.exp_2))
        self.wait(1)
        self.play(Write(self.exp_3))
        self.wait(1)
        self.play(Write(self.exp_4))
        self.wait(1)
        self.play(Write(self.exp_5))
        self.play(FadeOut(self.exp_1), FadeOut(self.exp_2), FadeOut(self.exp_3), FadeOut(self.exp_4), FadeOut(self.exp_5))
        self.play(Write(self.exp_6))
        self.wait(1)

    def create_dots_and_circles(self):
        # 創建點和圈
        n1 = 39
        n2 = 59
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
        
        
        for dot in unit_dots2:
            self.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles2:
            self.play(FadeIn(circle), run_time=0.1)
        
        
        

        #移動個位數的點
        all_dots = unit_dots1 + unit_dots2
        digits = units1+units2
        all_circles = ten_circles1 + ten_circles2
        tens_digits = tens1+tens2
        sum= n1+n2
        i = digits

        self.wait(1)
        
        for dot in all_dots:
            dot.set_color(GREEN)
            if i>digits-10:
                self.play(dot.animate.move_to(RIGHT * ((digits-i)*0.5+1) + UP *1), run_time=0.5)
            else:
                self.play(dot.animate.move_to(RIGHT * ((digits-(i+10))*0.5+1)), run_time=0.5)
            i-=1

        #進位時創建框
        if digits>=10:
            digits-=10
            tens_digits+=1 
            selected_dots = all_dots[:10]
            dots_group = VGroup(*selected_dots)
            rect = SurroundingRectangle(dots_group, color=BLUE, buff=0.3)
            self.play(Create(rect))
            self.wait(2)
            for dot in selected_dots:
                self.remove(dot)
            circle = Circle(radius=0.3, color=RED).move_to(rect.get_center())
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
            self.play(circle.animate.move_to(RIGHT * ((digits-i)*0.5+1)+ DOWN * 1), run_time=0.5)
            i-=1

    def show_answer(self):
        # 顯示答案
        n1 = 39
        n2 = 59
        sum = n1 + n2
        digits = n1 % 10 + n2 % 10
        tens_digits = n1 // 10 + n2 // 10
        if digits>=10:
            digits-=10
            tens_digits+=1

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
        self.play(FadeOut(self.exp_6))
        self.play(Write(self.ans))
        self.wait(2)





















