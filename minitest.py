import os
from manim import *
import platform
from manim import *

class division:
    def __init__(self, n1, n2, pos):
        self.n1 = n1
        self.n2 = n2
        self.remainder = n1 % n2
        self.quotient = (n1-self.remainder) / n2
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
        m4 = f"數數看最後有多少框"
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
        n1 = self.n1
        n2 = self.n2
        unit_dots1 = []
        unit_circles = []
        
        for i in range(n1):
            dot = Dot(point=(i * 0.3 - 0.65, 0.5, 0), color=RED)
            unit_dots1.append(dot)
        
        for i in range(self.quotient):
            selected_dots = unit_dots1[:n2]
            dots_group = VGroup(*selected_dots)
            rect = SurroundingRectangle(dots_group, color=BLUE, buff=0.3)
            scene.play(Create(rect))
            scene.wait(2)
            for dot in selected_dots:
                scene.remove(dot)
            circle = Circle(radius=0.3, color=RED).move_to(rect.get_center())
            text = Text(f"{n2}", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            circle_group = VGroup(circle, text)
            scene.play(FadeIn(circle, text))
            unit_circles.append(circle_group)
            scene.wait(1)
            scene.play(FadeOut(rect))
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

class DevisionScene(Scene):
    def construct(self):
        # 創建4 x 8的乘法動畫
        mul_anim = division(4, 8, 3)
        mul_anim.animation(self)


if __name__ == "__main__":     
    config.media_dir = "./test_media"
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 60

    # 渲染影片
    scene = DevisionScene()
    scene.render()

    # 找到生成的影片路徑
    output_video_path = os.path.join(config.media_dir, "videos", "1080p60", "DevisionScene.mp4")
    
    # 自動打開影片
    if platform.system() == "Windows":
        os.startfile(output_video_path)  # Windows 自動打開影片





