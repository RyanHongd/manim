from manim import *

class add:
    def __init__(self, n1, n2, pos):
        self.n1 = n1
        self.n2 = n2
        self.sum = n1 + n2
        self.pos = pos
    def animation(self, scene):
        # 創建文字
        self.create_texts1(scene)

        # 創建點和圈
        self.add_dots(scene)

        # 顯示答案
        self.show_answer1(scene)

    def create_texts1(self, scene):
        # 定義問題和步驟文字
        n1 = self.n1
        n2 = self.n2
        
        a2 = f"我們有{n1}個"
        a3 = f"再給我們{n2}個"
        a4 = f"我們可以把十位數跟個位數分開"
        a5 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        a6 = f"{n2}可以被分成{n2 // 10}個10跟{n2 % 10}個1"
        a7 = f"加起來數一數共有多少個1跟10"


        # 創建文字物件
        exp_1 = Text(a2, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_2 = Text(a3, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_3 = Text(a4, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_4 = Text(a5, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_5 = Text(a6, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_6 = Text(a7, font="Noto Sans CJK", font_size=30, color=GREEN)


        # 創建 VGroup 並設置排列
        self.exp_g1 = VGroup(exp_1, exp_2, exp_3, exp_4, exp_5, exp_6)
        self.exp_g1.arrange(DOWN, aligned_edge=LEFT, buff=0.5)  # 垂直間隔0.5個單位
        self.exp_g1.scale_to_fit_width(5)
        self.exp_g1.move_to(LEFT * 4)
        
        # 顯示文字
        scene.play(Succession(*[Write(text) for text in self.exp_g1]))
        scene.wait(3)
        scene.play(FadeOut(self.exp_g1))

    def add_dots(self, scene):
        # 創建點和圈
        n1 = self.n1
        n2 = self.n2
        units1 = n1 % 10
        tens1 = n1 // 10
        units2 = n2 % 10
        tens2 = n2 // 10
        self.sum = n1 + n2
        
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
        
        # 顯示點和圈
        for dot in unit_dots1:
            scene.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles1:
            scene.play(FadeIn(circle), run_time=0.1)
        scene.wait(1)
        
        for dot in unit_dots2:
            scene.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles2:
            scene.play(FadeIn(circle), run_time=0.1)
        
        # 移動個位數的點
        self.all_dots = unit_dots1 + unit_dots2
        digits = units1 + units2
        self.all_circles = ten_circles1 + ten_circles2
        tens_digits = tens1 + tens2
        
        i = digits

        scene.wait(1)
        
        for dot in self.all_dots:
            dot.set_color(GREEN)
            if i > digits - 10:
                scene.play(dot.animate.move_to(RIGHT * ((digits - i) * 0.5 + 1) + UP * 1), run_time=0.5)
            else:
                scene.play(dot.animate.move_to(RIGHT * ((digits - (i + 10)) * 0.5 + 1)), run_time=0.5)
            i -= 1

        # 進位時創建框
        if digits >= 10:
            digits -= 10
            tens_digits += 1 
            selected_dots = self.all_dots[:10]
            dots_group = VGroup(*selected_dots)
            rect = SurroundingRectangle(dots_group, color=BLUE, buff=0.3)
            scene.play(Create(rect))
            scene.wait(2)
            for dot in selected_dots:
                scene.remove(dot)
            circle = Circle(radius=0.3, color=RED).move_to(rect.get_center())
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            scene.play(FadeIn(circle, text))
            self.all_circles.append(VGroup(circle, text))
            scene.wait(1)
            scene.play(FadeOut(rect))

        # 移動十位數的點
        i = tens_digits
        for circle in self.all_circles:
            circle[0].set_color(GREEN)
            circle[1].set_color(WHITE)
            scene.play(circle.animate.move_to(RIGHT * ((digits - i) * 0.5 + 1) + DOWN * 1), run_time=0.5)
            i -= 1
        scene.wait(3)
        scene.play(FadeOut(VGroup(*self.all_dots)))
        scene.play(FadeOut(VGroup(*self.all_circles)))

    def show_answer1(self, scene):
        # 顯示答案
        ans_text = Text(f"{self.n1} + {self.n2} = {self.sum}", font="Noto Sans CJK", font_size=24).move_to(DOWN * ((self.pos*0.5)+1.5))
        
        # 顯示文字
        scene.play(FadeIn(ans_text))
        
        scene.wait(3)


        