from manim import *

class Add3And4Dot(Scene):
    def construct(self):
        # 問題描述
        title = Text("小名有24塊錢，媽媽再給他13塊錢，曉華又拿走他8塊錢，請問小名最後有幾塊錢?", font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
        
        # 加法部分
        n1 = 24
        n2 = 13
        s1 = f"小名有{n1}塊錢，媽媽再給他{n2}塊錢，現在共有多少塊錢？"
        s2 = f"首先我們有{n1}塊錢"
        s3 = f"媽媽再給我們{n2}塊錢"
        s4 = f"我們可以把十位數跟個位數分開"
        s5 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        s6 = f"{n2}可以被分成{n2 // 10}個10跟{n2 % 10}個1"
        s7 = f"把所有的1加起來, 再把所有的10加起來"
        s8 = f"最後再把十位數和個位數加起來"
        s9 = f"因此我們最後共有{n1 + n2}塊錢"
        
        exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=RED).move_to(LEFT * 4 + UP * 2)
        exp_2 = Text(s3, font="Noto Sans CJK", font_size=30, color=BLUE).move_to(UP * 2)
        exp_3 = Text(s4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        exp_4 = Text(s5, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4)
        exp_5 = Text(s6, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 1)
        exp_6 = Text(s7, font="Noto Sans CJK", font_size=30, color=WHITE).move_to(LEFT * 2 + UP * 2)
        exp_7 = Text(s8, font="Noto Sans CJK", font_size=30, color=WHITE).move_to(LEFT * 2 + UP * 2)
        ans = Text(s9, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)
        
        # 顯示問題
        self.play(Write(title))
        self.wait(1)

        # 顯示加法過程
        self.play(Write(exp_1))
        self.wait(1)
        self.play(Write(exp_2))
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
        self.wait(1)
        self.play(Write(ans))
        self.wait(2)

        # 減法部分
        n1 = 37
        n2 = 8
        s1 = f"小名有{n1}塊錢, 曉華拿走了{n2}塊錢, 現在剩下多少塊錢?"
        s2 = f"首先我們有{n1}塊錢"
        s3 = f"曉華拿走了{n2}塊錢"
        s4 = f"要從{n1}拿出{n2}塊錢"
        s5 = f"把要給的1拿出, 再把要給的10拿出"
        s6 = f"最後再把剩下的錢加起來"
        s7 = f"因此我們最後剩下{n1 - n2}塊錢"

        exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=RED).move_to(LEFT * 4 + UP * 2)
        exp_2 = Text(s3, font="Noto Sans CJK", font_size=30, color=BLUE).move_to(UP * 2)
        exp_3 = Text(s4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        exp_4 = Text(s5, font="Noto Sans CJK", font_size=30, color=WHITE).move_to(LEFT * 3 + UP * 2)
        ans = Text(s7, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)
        
        # 顯示減法過程
        self.play(Write(exp_1))
        self.wait(1)
        self.play(Write(exp_2))
        self.wait(1)
        self.play(Write(exp_3))
        self.wait(1)
        self.play(Write(exp_4))
        self.wait(1)
        self.play(Write(ans))
        self.wait(2)















