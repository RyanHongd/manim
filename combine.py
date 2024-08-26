from manim import *

class Add31And54Dot(Scene):
    def construct(self):
        # 創建文字（解釋）
        n1 = 39
        n2 = 59
        n3 = 29

        a1 = f"小明有{n1}個糖果, 媽媽給他{n2}個, 小華再拿走{n3}個, 現在共有幾個?"
        a2 = f"我們先算加法"
        a3 = f"首先小明有{n1}顆糖果"
        a4 = f"媽媽再給小明{n2}顆"
        a5 = f"我們可以把十位數跟個位數分開"
        a6 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        a7 = f"{n2}可以被分成{n2 // 10}個10跟{n2 % 10}個1"
        a8 = f"數一數共有多少個1跟10"
        a9 = f"因此我們共有{n1 + n2}顆"

        m1 = f"算完加法後接著算減法"
        m2 = f"小明現在有{n1}顆糖果"
        m3 = f"他給了小華{n2}顆"
        m4 = f"我們可以把十位數跟個位數分開"
        m5 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        m6 = f"要從{n1}拿出{n2}個"
        m7 = f"把要給的1拿出, 再把要給的10拿出"
        m8 = f"因此我們最後剩下{n1 - n2}顆"
        
        title = Text(a1, font="Noto Sans CJK", font_size=33, color=YELLOW).to_edge(UP)
        exp_1 = Text(a2, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 2)
        exp_2 = Text(a3, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        exp_3 = Text(a4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 )
        exp_4 = Text(a5, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 1)
        exp_5 = Text(a6, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 2)
        exp_6 = Text(a7, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        exp_7 = Text(a8, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 1)
        sum = Text(a9, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)

        title = Text(m1, font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
        exp_1 = Text(m2, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 2)
        exp_2 = Text(m3, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        exp_3 = Text(m4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4)
        exp_4 = Text(m5, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 1)
        exp_5 = Text(m6, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 2)
        exp_6 = Text(m7, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        ans = Text(m8, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)

        #打印文字
        self.play(Write(title))
        self.wait(1)
        self.play(Write(exp_1))
        self.wait(1)
        self.play(Write(exp_2))
        self.wait(1)
        self.play(Write(exp_3))
        self.wait(1)
        self.play(Write(exp_4))
        self.wait(1) 

        # 創建點
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
        
        self.play(Write(exp_5))
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
        self.play(FadeOut(exp_1), FadeOut(exp_2), FadeOut(exp_3), FadeOut(exp_4), FadeOut(exp_5))
        self.play(Write(exp_6))
        for dot in all_dots:
            dot.set_color(GREEN)
            if i>digits-10:
                self.play(dot.animate.move_to(RIGHT * ((digits-i)*0.5+1) + UP *1), run_time=0.5)
            else:
                self.play(dot.animate.move_to(RIGHT * ((digits-(i+10))*0.5+1)), run_time=0.5)
            i-=1

        #進位時創建框
        if digits>10:
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

        #把答案顯示
        self.wait(1)
        self.play(FadeOut(exp_6))
        self.wait(1)
        self.play(Write(exp_7))
        digits_text = Text(str(digits), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + UP *1)
        add_text = Text("+", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6)
        tens_digits_text = Text(str(tens_digits*10), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + DOWN * 1)
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
        self.play(FadeOut(exp_7))
        
        self.play(Write(sum))
        self.wait(2)


        # 創建題目（使用者輸入的問題）
        n1 = sum
        n2 = n3
        
        
        

        # 打印文字
        self.play(Write(title))
        self.wait(1)
        self.play(Write(exp_1))
        self.wait(1)
        self.play(Write(exp_2))
        self.wait(1)
        self.play(Write(exp_3))
        self.wait(1)
        self.play(Write(exp_4))

        #創建點
        units1 = n1 % 10
        tens1 = n1 // 10
        units2 = n2 % 10
        tens2 = n2 // 10
        
        unit_dots1 = []
        ten_circles1 = []
        
        for j in range(units1):
            dot = Dot(point=(j * 0.3 - 0.65, 0.5, 0), color=RED)
            unit_dots1.append(dot)
        
        for i in range(tens1):
            circle = Circle(radius=0.3, color=RED).move_to((i * 0.6 - 0.65, 0, 0))
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            ten_circles1.append(VGroup(circle, text))

        # 打印所有點
        for dot in unit_dots1:
            self.play(FadeIn(dot), run_time=0.05)
        for circle in ten_circles1:
            self.play(FadeIn(circle), run_time=0.1)
        pre_num = Text(str(n1), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6)
        self.play(FadeIn(pre_num))
        
        self.wait(1)
        self.play(FadeOut(exp_1), FadeOut(exp_2), FadeOut(exp_3), FadeOut(exp_4))
        self.play(Write(exp_5))
        self.wait(1)
        self.play(Write(exp_6))

        #借位
        if units1<units2:
            tens1-=1
            units1+=10
            text1 =  Text(f"因為個位數不夠減", font="Noto Sans CJK", font_size=24).move_to(LEFT * 4)
            text2 =  Text(f"我們必須把一個10拆開變成10個1", font="Noto Sans CJK", font_size=24).move_to(LEFT * 4 + DOWN * 1)
            self.play(FadeIn(text1), FadeIn(text2))
            self.play(ten_circles1[tens1].animate.move_to(DOWN * 1.5))
            for j in range(j+10):
                dot = Dot(point=((j+1) * 0.3 - 0.65,0.5, 0), color=YELLOW)
                self.play(FadeIn(dot), run_time=0.1)
                unit_dots1.append(dot)
            self.wait(2)
            self.remove(ten_circles1[tens1])
            ten_circles1.remove(ten_circles1[tens1])


        #把要提出的點拿出
        selected_dots = unit_dots1[:units2]
        selected_circles = ten_circles1[:tens2]
        
        for dot in selected_dots:
            dot.set_color(BLUE)
            self.play(dot.animate.move_to(RIGHT * ((unit_dots1.index(dot) - units2/2)*0.5+2) + DOWN * 1), run_time=0.5)
        
        for circle in selected_circles:
            circle[0].set_color(BLUE)
            circle[1].set_color(WHITE)
            self.play(circle.animate.move_to(RIGHT * ((ten_circles1.index(circle) - tens2/2)*0.5+2) + DOWN * 1.5), run_time=0.5)
        minus =Text("-", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + DOWN * 1) 
        lat_num = Text(str(n2), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + DOWN * 2)
        self.play(FadeIn(minus),FadeIn(lat_num),FadeOut(exp_5), FadeOut(exp_6),FadeOut(text1),FadeOut(text2))
        self.wait(2)
        for dot in selected_dots:
            self.remove(dot)
        for circle in selected_circles:
            self.remove(circle)

        self.play(pre_num.animate.move_to(LEFT * 2 + DOWN * 2))
        self.play(minus.animate.move_to(LEFT * 1 + DOWN * 2))
        self.play(lat_num.animate.move_to(DOWN * 2))

        #計算剩下的點
        remaining_dots = [dot for dot in unit_dots1 if dot not in selected_dots]
        remaining_circles = [circle for circle in ten_circles1 if circle not in selected_circles]
        
        text = Text("數數看剩下共有幾個點", font="Noto Sans CJK", font_size=24).move_to(LEFT * 4 + UP * 2)
        self.play(FadeIn(text))
        for dot in remaining_dots:
            dot.set_color(GREEN)
            self.play(dot.animate.move_to(RIGHT * (remaining_dots.index(dot) )*0.5 + UP * 1), run_time=0.5)
        
        for circle in remaining_circles:
            circle[0].set_color(GREEN)
            circle[1].set_color(WHITE)
            self.play(circle.animate.move_to(RIGHT * (remaining_circles.index(circle) )), run_time=0.5)
        self.wait(1)

        #打印答案
        ans_text = Text(str(n1-n2), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6)
        equal_text = Text("=", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 2.5)

        self.play(FadeOut(text),FadeIn(ans_text))
        self.wait(1)
        self.play(equal_text.animate.move_to(RIGHT * 1 + DOWN * 2))
        self.play(ans_text.animate.move_to(RIGHT * 2 + DOWN * 2))
        self.play(Write(ans))
        self.wait(2)