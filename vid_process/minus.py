from manim import *

class minus:
    def __init__(self, n1, n2, pos):
        self.n1 = n1
        self.n2 = n2
        self.dif = n1 - n2
        self.pos = pos
    def animation(self, scene):
        # 創建文字
        self.create_texts2(scene)

        # 創建點和圈
        self.minus_dots(scene)

        # 顯示答案
        self.show_answer2(scene)

    def create_texts2(self, scene):
        n1 = self.n1
        n2 = self.n2

        s2 = f"首先我們有{n1}個"
        s3 = f"要拿走{n2}個"
        s4 = f"我們可以把十位數跟個位數分開"
        s5 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        s6 = f"要從{n1}拿出{n2}個"
        s7 = f"把要給的1拿出, 再把要給的10拿出"
        s8 = f"數數看剩下共有幾個點" 
        s9 = f"因此我們最後剩下{self.dif}"
        
        # 創建文字物件
        exp_1 = Text(s2, font="Noto Sans CJK TC", font_size=30, color=GREEN)
        exp_2 = Text(s3, font="Noto Sans CJK TC", font_size=30, color=GREEN)
        exp_3 = Text(s4, font="Noto Sans CJK TC", font_size=30, color=GREEN)
        exp_4 = Text(s5, font="Noto Sans CJK TC", font_size=30, color=GREEN)
        exp_5 = Text(s6, font="Noto Sans CJK TC", font_size=30, color=GREEN)
        exp_6 = Text(s7, font="Noto Sans CJK TC", font_size=30, color=GREEN)
        exp_7 = Text(s8, font="Noto Sans CJK TC", font_size=24, color=GREEN)
        self.ans = Text(s9, font="Noto Sans CJK TC", font_size=30, color=YELLOW).to_edge(DOWN)

        # 將文字物件放入 VGroup 並排列
        self.exp_g2 = VGroup(exp_1, exp_2, exp_3, exp_4, exp_5, exp_6, exp_7).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.exp_g2.scale_to_fit_width(5)
        self.exp_g2.move_to(LEFT * 4)
        
        # 使用 Succession 逐一顯示每組文本
        scene.play(Succession(*[Write(text) for text in self.exp_g2], lag_ratio=1))
        scene.wait(3)
        scene.play(FadeOut(self.exp_g2))

        # 借位時的文字解釋
        if self.n1 % 10 < self.n2 % 10:
            text1 = Text(f"因為個位數不夠減", font="Noto Sans CJK TC", font_size=24).next_to(self.exp_g2, DOWN, buff=0.5)
            text2 = Text(f"我們必須把一個10拆開變成10個1", font="Noto Sans CJK TC", font_size=24).next_to(text1, DOWN, buff=0.5)
            scene.play(FadeIn(text1), FadeIn(text2))
            scene.wait(2)
            scene.play(FadeOut(text1), FadeOut(text2))

    def minus_dots(self, scene):
        # 創建點和圈
        n1 = self.n1
        n2 = self.n2
        units1 = n1 % 10
        tens1 = n1 // 10
        units2 = n2 % 10
        tens2 = n2 // 10

        unit_dots1 = []
        ten_circles1 = []

        for i in range(units1):
            dot = Dot(point=(i * 0.3 - 0.7, 0.5, 0), color=RED)
            unit_dots1.append(dot)

        for i in range(tens1):
            circle = Circle(radius=0.3, color=RED).move_to((i * 0.6 - 0.65, 0, 0))
            text = Text("10", font="Noto Sans CJK TC", font_size=24).move_to(circle.get_center())
            ten_circles1.append(VGroup(circle, text))

        for dot in unit_dots1:
            scene.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles1:
            scene.play(FadeIn(circle), run_time=0.1)
        scene.wait(1)

        dot_group = VGroup(*unit_dots1)
        if units1!=0:
            last_dot_position = dot_group[0].get_center()
        else:
            last_dot_position = (0,0,0)
        # 借位
        if units1 < units2:
            tens1 -= 1
            units1 += 10
            scene.play(ten_circles1[tens1].animate.move_to(DOWN * 1.5))
            for i in range(10):
                dot = Dot(color=YELLOW).move_to(last_dot_position + RIGHT * (i * 0.5) + DOWN * 1)
                scene.play(FadeIn(dot), run_time=0.1)
                unit_dots1.append(dot)
            scene.wait(2)
            scene.remove(ten_circles1[tens1])
            ten_circles1.remove(ten_circles1[tens1])

        # 把要提出的點拿出
        selected_dots = unit_dots1[:units2]
        selected_circles = ten_circles1[:tens2]

        for dot in selected_dots:
            dot.set_color(BLUE)
            scene.play(dot.animate.move_to(RIGHT * ((unit_dots1.index(dot) - units2 / 2) * 0.5 + 2) + DOWN * 1), run_time=0.5)

        for circle in selected_circles:
            circle[0].set_color(BLUE)
            circle[1].set_color(WHITE)
            scene.play(circle.animate.move_to(RIGHT * ((ten_circles1.index(circle) - tens2 / 2) * 0.5 + 2) + DOWN * 1.5), run_time=0.5)

        scene.wait(2)
        for dot in selected_dots:
            scene.remove(dot)
        for circle in selected_circles:
            scene.remove(circle)

        # 計算剩下的點
        self.remaining_dots = [dot for dot in unit_dots1 if dot not in selected_dots]
        self.remaining_circles = [circle for circle in ten_circles1 if circle not in selected_circles]

        for dot in self.remaining_dots:
            dot.set_color(GREEN)
            scene.play(dot.animate.move_to(RIGHT * (self.remaining_dots.index(dot)) * 0.5 + UP * 1), run_time=0.5)

        for circle in self.remaining_circles:
            circle[0].set_color(GREEN)
            circle[1].set_color(WHITE)
            scene.play(circle.animate.move_to(RIGHT * (self.remaining_circles.index(circle))* 0.75), run_time=0.5)
        scene.wait(3)
        scene.play(FadeOut(VGroup(*self.remaining_dots)))
        scene.play(FadeOut(VGroup(*self.remaining_circles)))

    def show_answer2(self, scene):
        # 顯示答案
        ans_text = Text(f"{self.n1} - {self.n2} = {self.dif}", font="Noto Sans CJK TC", font_size=24).move_to(DOWN * ((self.pos*0.5)+1.5))
        scene.play(FadeIn(ans_text))
        
        scene.wait(2)

     

