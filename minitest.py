from manim import *

class AlignText(Scene):
    def construct(self):
        n1 = 37
        n2 = 8
        
        s2 = f"小明現在有{n1}顆糖果"
        s3 = f"他給了小红{n2}顆"
        s4 = f"我們可以把十位數跟個位數分開"
        s5 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        s6 = f"要從{n1}拿出{n2}個"
        s7 = f"把要給的1拿出, 再把要給的10拿出"
        s8 = f"數數看剩下共有幾個點" 
        s9 = f"因此我們最後剩下{n1 - n2}顆"
        
        # 創建文字物件
        exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_2 = Text(s3, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_3 = Text(s4, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_4 = Text(s5, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_5 = Text(s6, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_6 = Text(s7, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_7 = Text(s8, font="Noto Sans CJK", font_size=24, color=GREEN)
        self.ans = Text(s9, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)

        # 將文字物件放入 VGroup 並排列
        exp_group_1 = VGroup(exp_1, exp_2, exp_3, exp_4,exp_5, exp_6, exp_7).arrange(DOWN, aligned_edge=LEFT, buff=0.5)


        # 移動到左側
        exp_group_1.move_to(LEFT * 4)

        
        # 使用 Succession 逐一顯示每組文本
        self.play(Succession(*[Write(text) for text in exp_group_1], lag_ratio=1))
        self.play(FadeOut(exp_group_1))

        self.wait(2)






        # 定義函式來創建文字動畫
        '''
        def create_text_animations():
            text1 = Text("這是第一行", color=BLUE).move_to(UP * 2)
            text2 = Text("這是第二行", color=BLUE).move_to(UP)
            text3 = Text("這是第三行", color=BLUE).move_to(DOWN)
            return [
                FadeIn(text1),
                FadeIn(text2),
                FadeIn(text3)
            ]
        
        # 定義函式來創建點的動畫
        def create_dot_animations():
            dot1 = Dot(color=RED).move_to(LEFT * 3 + DOWN * 2)
            dot2 = Dot(color=GREEN).move_to(DOWN * 2)
            dot3 = Dot(color=YELLOW).move_to(RIGHT * 3 + DOWN * 2)
            return [
                FadeIn(dot1),
                FadeIn(dot2),
                FadeIn(dot3)
            ]
        
        # 使用函式創建動畫對象
        text_animations = create_text_animations()
        dot_animations = create_dot_animations()

        # 播放所有動畫，同時運行
        self.play(
            AnimationGroup(*text_animations, lag_ratio=0.5),
            AnimationGroup(*dot_animations, lag_ratio=0.5),
            lag_ratio=0.5  # 此值設置兩組動畫之間的延遲
        )
        
        self.wait(2)  # 等待以查看動畫結果

        '''





