from manim import *

class AlignText(Scene):
    def construct(self):
        def text_animation():
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
            
            title = Text(a1, font="Noto Sans CJK", font_size=33, color=YELLOW).to_edge(UP)
            exp_1 = Text(a2, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 2)
            exp_2 = Text(a3, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
            exp_3 = Text(a4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4)
            exp_4 = Text(a5, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 1)
            exp_5 = Text(a6, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 2)
            exp_6 = Text(a7, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
            ans = Text(a8, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)

            # 創建單獨的動畫
            animations = [
                Write(title),
                Wait(1),
                Write(exp_1),
                Wait(1),
                Write(exp_2),
                Wait(1),
                Write(exp_3),
                Wait(1),
                Write(exp_4),
                Wait(1),
                Write(exp_5),
                AnimationGroup(
                    FadeOut(exp_1),
                    FadeOut(exp_2),
                    FadeOut(exp_3),
                    FadeOut(exp_4),
                    FadeOut(exp_5),
                    lag_ratio=0
                ),
                Write(exp_6),
                FadeOut(exp_6),
                Write(ans)
            ]
            
            return AnimationGroup(*animations, lag_ratio=0.5)

        # 獲取組合的動畫
        print_text = text_animation()
        
        # 播放動畫
        self.play(print_text)
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





