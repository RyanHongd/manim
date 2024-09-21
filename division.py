from manim import *

class division:
    def __init__(self, n1, n2, pos):
        self.n1 = n1
        self.n2 = n2
        self.remainder = n1 % n2
        self.quotient = int((n1-self.remainder) / n2)
        self.pos = pos
    def animation(self, scene):
        # 創建文字
        self.create_texts4(scene)

        # 創建點和圈
        self.division_dots(scene)

        # 顯示答案
        self.show_answer4(scene)
    def create_texts4(self,scene):
        n1 = self.n1
        n2 = self.n2

        m1 = f"首先我們有{n1}個點"
        m2 = f"{n2}個要分成一組"
        m3 = f"每{n2}個框起來"
        m4 = f"數數看最後有多少個圈"
        m5 = f"因此我們有{self.quotient}組"

        exp_1 = Text(m1, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_2 = Text(m2, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_3 = Text(m3, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_4 = Text(m4, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_5 = Text(m5, font="Noto Sans CJK", font_size=30, color=GREEN)

        self.exp_g4 = VGroup(exp_1, exp_2, exp_3, exp_4, exp_5)
        self.exp_g4.arrange(DOWN, aligned_edge=LEFT, buff=0.5)  # 垂直間隔0.5個單位
        self.exp_g4.scale_to_fit_width(3)
        self.exp_g4.move_to(LEFT * 5)

        scene.play(Succession(*[Write(text) for text in self.exp_g4]))
        scene.wait(3)
        scene.play(FadeOut(self.exp_g4))

        if self.remainder != 0:
            text1 = Text(f"有{self.remainder}個不夠分", font="Noto Sans CJK", font_size=24).next_to(self.exp_g4, DOWN, buff=0.5)
            text2 = Text(f"這些剩下的就是餘數", font="Noto Sans CJK", font_size=24).next_to(text1, DOWN, buff=0.5)
            scene.play(FadeIn(text1), FadeIn(text2))
            scene.wait(2)
            scene.play(FadeOut(text1), FadeOut(text2))

    def division_dots(self,scene):
        n1 = self.n1  # 總點數
        n2 = self.n2  # 每組點數
        unit_dots1 = []
        unit_circles = []

        # 創建點
        for i in range(n1):
            dot = Dot(point=(i * 0.3 - 0.65, 0.5, 0), color=RED)
            unit_dots1.append(dot)

        # 顯示所有點
        for dot in unit_dots1:
            scene.play(FadeIn(dot), run_time=0.1)

        # 將點分組並框起來
        for i in range(self.quotient):
            # 修正索引範圍，從 n2 * i 開始，到 n2 * (i+1) 結束
            start_idx = n2 * i
            end_idx = n2 * (i + 1)
            
            # 防止索引超出範圍
            if end_idx > len(unit_dots1):
                end_idx = len(unit_dots1)

            # 取得每一組的點
            selected_dots = unit_dots1[start_idx:end_idx]

            # 用框框框起來
            dots_group = VGroup(*selected_dots)
            rect = SurroundingRectangle(dots_group, color=BLUE, buff=0.2)
            scene.play(Create(rect))
            scene.wait(2)

            # 移除點並用圓圈替換
            for dot in selected_dots:
                scene.remove(dot)

            circle = Circle(radius=0.3, color=RED).move_to(rect.get_center())
            text = Text(f"{n2}", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            circle_group = VGroup(circle, text)

            # 顯示圓圈與數字
            scene.play(FadeIn(circle_group))
            unit_circles.append(circle_group)
            scene.wait(1)
            
            # 移動圓圈到指定位置
            scene.play(FadeOut(rect))
            scene.wait(1)
            scene.play(circle_group.animate.move_to(RIGHT * (i * 0.5 + 1) + DOWN * 1), run_time=0.5)

        scene.wait(3)
        scene.play(FadeOut(VGroup(*unit_dots1)))



    def show_answer4(self,scene):
        if self.remainder != 0:
            ans_text = Text(f"{self.n1} ÷ {self.n2} = {self.quotient} ... {self.remainder}", font="Noto Sans CJK", font_size=24).move_to(DOWN * ((self.pos*0.5)+1.5))
        else:
            ans_text = Text(f"{self.n1} ÷ {self.n2} = {self.quotient}", font="Noto Sans CJK", font_size=24).move_to(DOWN * ((self.pos*0.5)+1.5))
        # 顯示文字
        scene.play(FadeIn(ans_text))
        
        scene.wait(3)