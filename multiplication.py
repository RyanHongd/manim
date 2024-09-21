from manim import *

class multiplication:
    def __init__(self, n1, n2, pos):
        self.n1 = n1
        self.n2 = n2
        self.product = n1 * n2
        self.pos = pos
    def animation(self, scene):
        # 創建文字
        self.create_texts3(scene)

        # 創建點和圈
        self.multiplication_dots(scene)

        # 顯示答案
        self.show_answer3(scene)
    def create_texts3(self,scene):
        n1 = self.n1
        n2 = self.n2

        m1 = f"首先我們有{n1}個點為一組"
        m2 = f"我們有{n2}組這樣的點"
        m3 = f"把這些組全部加起來"
        m4 = f"數數看最後有多少個"
        m5 = f"因此我們共有{self.product}個點"

        exp_1 = Text(m1, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_2 = Text(m2, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_3 = Text(m3, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_4 = Text(m4, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_5 = Text(m5, font="Noto Sans CJK", font_size=30, color=GREEN)

        self.exp_g3 = VGroup(exp_1, exp_2, exp_3, exp_4, exp_5)
        self.exp_g3.arrange(DOWN, aligned_edge=LEFT, buff=0.5)  # 垂直間隔0.5個單位
        self.exp_g3.scale_to_fit_width(3)
        self.exp_g3.move_to(LEFT * 5)

        scene.play(Succession(*[Write(text) for text in self.exp_g3]))
        scene.wait(3)
        scene.play(FadeOut(self.exp_g3))

    def multiplication_dots(self,scene):
        n1 = self.n1
        n2 = self.n2
        self.product = n1 * n2
        unit_circles1 = []
        
        for i in range(n2):
            circle = Circle(radius=0.3, color=RED).move_to((i * 0.6 - 0.65, 0, 0))
            text = Text(f"{n1}", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            unit_circles1.append(VGroup(circle, text))
        
        for circle in unit_circles1:
            scene.play(FadeIn(circle), run_time=0.5)
        scene.wait(3)

        scene.play(FadeOut(VGroup(*unit_circles1)))


    def show_answer3(self,scene):
        ans_text = Text(f"{self.n1} x {self.n2} = {self.product}", font="Noto Sans CJK", font_size=24).move_to(DOWN * ((self.pos*0.5)+1.5))
        
        # 顯示文字
        scene.play(FadeIn(ans_text))
        
        scene.wait(3)