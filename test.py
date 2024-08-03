from manim import *

class Add31And54Dot(Scene):
    def construct(self):
        # 创建题目（使用者输入的问题）
        n1 = 31
        n2 = 54
        s1 = f"小明有{n1}個糖果, 媽媽再給他{n2}個, 現在共有幾個?"
        s2 = f"首先我們有{n1}顆糖果"
        s3 = f"媽媽再給我們{n2}顆"
        s4 = f"我們可以把{n1}的十位數跟個位數分開"
        s5 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        s6 = f"{n2}可以被分成{n2 // 10}個10跟{n2 % 10}個1"
        s7 = f"把所有的10加起來, 再把所有的1加起來"
        s8 = f"最後再把十位數和個位數加起來"
        s9 = f"因此我們最後共有{n1 + n2}顆"
        
        title = Text(s1, font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
        exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=RED).move_to(LEFT * 4 + UP * 2)
        exp_2 = Text(s3, font="Noto Sans CJK", font_size=30, color=BLUE).move_to(LEFT * 4 + UP * 1)
        exp_3 = Text(s4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 0)
        exp_4 = Text(s5, font="Noto Sans CJK", font_size=30, color=PURPLE).move_to(LEFT * 4 + DOWN * 1)
        exp_5 = Text(s6, font="Noto Sans CJK", font_size=30, color=ORANGE).move_to(LEFT * 4 + DOWN * 2)
        exp_6 = Text(s7, font="Noto Sans CJK", font_size=30, color=TEAL).move_to(LEFT * 4 + DOWN * 3)
        exp_7 = Text(s8, font="Noto Sans CJK", font_size=30, color=PINK).move_to(LEFT * 4 + DOWN * 4)
        ans = Text(s9, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)
        
        units1 = n1 % 10
        tens1 = n1 // 10
        units2 = n2 % 10
        tens2 = n2 // 10
        
        unit_dots1 = []
        ten_circles1 = []
        unit_dots2 = []
        ten_circles2 = []
        
        # 使用循环创建多个点并将它们添加到列表中
        for i in range(units1):
            dot = Dot(point=(i * 0.3 - 4.65, 1, 0), color=RED)
            unit_dots1.append(dot)
        
        for i in range(tens1):
            circle = Circle(radius=0.3, color=BLUE).move_to((i * 0.6 - 4.65, 0.5, 0))
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            ten_circles1.append(VGroup(circle, text))
        
        for i in range(units2):
            dot = Dot(point=(i * 0.3 - 4.65, 0, 0), color=RED)
            unit_dots2.append(dot)
        
        for i in range(tens2):
            circle = Circle(radius=0.3, color=BLUE).move_to((i * 0.6 - 4.65, -0.5, 0))
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            ten_circles2.append(VGroup(circle, text))
        
        # 影片流程
        self.play(Write(title))
        self.wait(1)
        self.play(Write(exp_1))
        
        # 显示所有单位点
        for dot in unit_dots1:
            self.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles1:
            self.play(FadeIn(circle), run_time=0.1)

        self.wait(1)
        self.play(Write(exp_2))
        
        for dot in unit_dots2:
            self.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles2:
            self.play(FadeIn(circle), run_time=0.1)
        
        self.wait(1)
        self.play(Write(exp_3))
        self.wait(1)
        self.play(Write(exp_4))
        self.wait(1)
        self.play(Write(exp_5))
        self.wait(1)
        self.play(Write(exp_6))
        self.wait(1)
        self.play(Write(exp_7))
        
        # 使 exp_1 到 exp_7 消失并更改所有点的颜色为绿色
        self.play(FadeOut(exp_1), FadeOut(exp_2), FadeOut(exp_3), FadeOut(exp_4), FadeOut(exp_5), FadeOut(exp_6), FadeOut(exp_7))
        
        all_dots = unit_dots1 + unit_dots2
        all_circles = ten_circles1 + ten_circles2
        
        for dot in all_dots:
            dot.set_color(GREEN)
        
        for circle in all_circles:
            circle[0].set_color(GREEN)
            circle[1].set_color(WHITE)

        self.play(Write(ans))
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.media_width = "100%"
    config.verbosity = "WARNING"
    scene = Add31And54Dot()
    scene.render()



