from manim import *

class Combine(Scene):
    def construct(self):
        # 創建文字（使用者輸入的問題）
        
        self.create_title()

        self.create_texts1()

        # 創建點和圈
        self.add_dots()

        # 顯示答案
        self.show_answer1()

        self.create_texts2()

        self.minus_dots()

        self.show_answer2()
    
    def create_title(self):
        self.n1=24
        self.n2=13
        self.n3=8
        
        title = f"小明有{self.n1}個糖果, 媽媽給他{self.n2}個,小紅又拿走他{self.n3}塊錢 現在共有幾個?"
        self.title = Text(title, font="Noto Sans CJK", font_size=33, color=YELLOW).to_edge(UP)
        self.title.scale_to_fit_width(14)
        self.play(Write(self.title))

    def create_texts1(self):
        # 定義問題和步驟文字
        n1 = self.n1
        n2 = self.n2
        
        a2 = f"首先我們有{n1}顆糖果"
        a3 = f"媽媽再給我們{n2}顆"
        a4 = f"我們可以把十位數跟個位數分開"
        a5 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        a6 = f"{n2}可以被分成{n2 // 10}個10跟{n2 % 10}個1"
        a7 = f"最後數一數共有多少個1跟10"
        a8 = f"因此我們共有{n1 + n2}顆"

        # 創建文字物件
        exp_1 = Text(a2, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_2 = Text(a3, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_3 = Text(a4, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_4 = Text(a5, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_5 = Text(a6, font="Noto Sans CJK", font_size=30, color=GREEN)
        exp_6 = Text(a7, font="Noto Sans CJK", font_size=30, color=GREEN)
        self.ans = Text(a8, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)

        # 創建 VGroup 並設置排列
        self.exp_g1 = VGroup(exp_1, exp_2, exp_3, exp_4, exp_5, exp_6)
        self.exp_g1.arrange(DOWN, aligned_edge=LEFT, buff=0.5)  # 垂直間隔0.5個單位
        self.exp_g1.scale_to_fit_width(4)
        self.exp_g1.move_to(LEFT * 4)
        
        # 顯示文字
        self.play(Succession(*[Write(text) for text in self.exp_g1]))
        self.wait(3)
        self.play(FadeOut(self.exp_g1))



    def add_dots(self):
        # 創建點和圈
        n1 = self.n1
        n2 = self.n2
        units1 = n1 % 10
        tens1 = n1 // 10
        units2 = n2 % 10
        tens2 = n2 // 10
        self.sum= n1+n2
        
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
        
        
        for dot in unit_dots2:
            self.play(FadeIn(dot), run_time=0.1)
        for circle in ten_circles2:
            self.play(FadeIn(circle), run_time=0.1)
        
        
        

        #移動個位數的點
        self.all_dots = unit_dots1 + unit_dots2
        digits = units1+units2
        self.all_circles = ten_circles1 + ten_circles2
        tens_digits = tens1+tens2
        
        i = digits

        self.wait(1)
        
        for dot in self.all_dots:
            dot.set_color(GREEN)
            if i>digits-10:
                self.play(dot.animate.move_to(RIGHT * ((digits-i)*0.5+1) + UP *1), run_time=0.5)
            else:
                self.play(dot.animate.move_to(RIGHT * ((digits-(i+10))*0.5+1)), run_time=0.5)
            i-=1

        #進位時創建框
        if digits>=10:
            digits-=10
            tens_digits+=1 
            selected_dots = self.all_dots[:10]
            dots_group = VGroup(*selected_dots)
            rect = SurroundingRectangle(dots_group, color=BLUE, buff=0.3)
            self.play(Create(rect))
            self.wait(2)
            for dot in selected_dots:
                self.remove(dot)
            circle = Circle(radius=0.3, color=RED).move_to(rect.get_center())
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            self.play(FadeIn(circle, text))
            self.all_circles.append(VGroup(circle, text))
            self.wait(1)
            self.play(FadeOut(rect))

        #移動十位數的點
        i = tens_digits
        for circle in self.all_circles:
            circle[0].set_color(GREEN)
            circle[1].set_color(WHITE)
            self.play(circle.animate.move_to(RIGHT * ((digits-i)*0.5+1)+ DOWN * 1), run_time=0.5)
            i-=1

    def show_answer1(self):
        # 顯示答案
        n1 = self.n1
        n2 = self.n2
        sum = n1 + n2
        digits = n1 % 10 + n2 % 10
        tens_digits = n1 // 10 + n2 // 10
        if digits>=10:
            digits-=10
            tens_digits+=1

        digits_text = Text(str(digits), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + UP * 1)
        add_text = Text("+", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6)
        tens_digits_text = Text(str(tens_digits * 10), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + DOWN * 1)
        equal_text = Text("=", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 2.5)
        sum_text = Text(str(sum), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 3)
        
        self.play(Write(digits_text))
        self.play(Write(add_text))
        self.play(Write(tens_digits_text))
        self.wait(1)
        self.ans1 = VGroup(digits_text, add_text, tens_digits_text, equal_text, sum_text)
        self.ans1.arrange(RIGHT,buff=0.5)  # 垂直間隔0.5個單位
        self.ans1.scale_to_fit_width(4)
        self.ans1.move_to(DOWN * 2)
        
        # 顯示文字
        self.play(Succession(*[Write(text) for text in self.ans1]))
        self.wait(3)


    def create_texts2(self):
        n1 = self.n2
        n2 = self.n3
        

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
        self.exp_g2= VGroup(exp_1, exp_2, exp_3, exp_4,exp_5, exp_6, exp_7).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.exp_g2.scale_to_fit_width(4)
        self.exp_g2.move_to(LEFT * 4)
        
        # 使用 Succession 逐一顯示每組文本
        self.play(Succession(*[Write(text) for text in self.exp_g2], lag_ratio=1))
        self.wait(5)
        self.play(FadeOut(self.exp_g2))
        self.wait(2)

        #借位時的文字解釋
        if n1 % 10< n2 % 10:
            self.text1 =  Text(f"因為個位數不夠減", font="Noto Sans CJK", font_size=24).next_to(self.exp_g2, DOWN, buff=0.5)
            self.text2 =  Text(f"我們必須把一個10拆開變成10個1", font="Noto Sans CJK", font_size=24).next_to(self.text1, DOWN, buff=0.5)
            self.play(FadeIn(self.text1), FadeIn(self.text2))
            self.wait(2)
            self.play(FadeOut(self.text1), FadeOut(self.text2))

    def minus_dots(self):

        #創建點
        n1=self.sum
        n2=self.n3
        units1 = n1 % 10
        tens1 = n1 // 10
        units2 = n2 % 10
        tens2 = n2 // 10
        
        unit_dots1 = self.all_dots
        ten_circles1 = self.all_circles

        dot_group = VGroup(*unit_dots1)
        last_dot_position = dot_group[0].get_center()

        '''
        for j in range(units1):
            dot = Dot(point=(j * 0.3 - 0.5, 0.5, 0), color=RED)
            unit_dots1.append(dot)
        
        for i in range(tens1):
            circle = Circle(radius=0.3, color=RED).move_to((i * 0.6 - 0.5, 0, 0))
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            ten_circles1.append(VGroup(circle, text))

        # 打印所有點
        for dot in unit_dots1:
            self.play(FadeIn(dot), run_time=0.05)
        for circle in ten_circles1:
            self.play(FadeIn(circle), run_time=0.1)
        
        '''
        self.pre_num = Text(str(n1), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6)
        self.play(FadeIn(self.pre_num))

        #借位
        if units1<units2:
            tens1-=1
            units1+=10
            self.play(ten_circles1[tens1].animate.move_to(DOWN * 1.5))
            for i in range(10):
                dot = Dot(color=YELLOW).move_to(last_dot_position + RIGHT * (i*0.5) + DOWN * 1)
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
        self.minus =Text("-", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + DOWN * 1) 
        self.lat_num = Text(str(n2), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + DOWN * 2)
        self.play(FadeIn(self.minus),FadeIn(self.lat_num))
        self.wait(2)
        for dot in selected_dots:
            self.remove(dot)
        for circle in selected_circles:
            self.remove(circle)

        

        #計算剩下的點
        remaining_dots = [dot for dot in unit_dots1 if dot not in selected_dots]
        remaining_circles = [circle for circle in ten_circles1 if circle not in selected_circles]
        
        
        for dot in remaining_dots:
            dot.set_color(GREEN)
            self.play(dot.animate.move_to(RIGHT * (remaining_dots.index(dot) )*0.5 + UP * 1), run_time=0.5)
        
        for circle in remaining_circles:
            circle[0].set_color(GREEN)
            circle[1].set_color(WHITE)
            self.play(circle.animate.move_to(RIGHT * (remaining_circles.index(circle) )), run_time=0.5)
        self.wait(1)

        #打印答案
    
    def show_answer2(self): 
        n1=self.sum
        n2=self.n3   
        ans_text = Text(str(n1-n2), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6)
        equal_text = Text("=", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 2.5)

        self.ans2 = VGroup(self.pre_num,self.minus,self.lat_num,equal_text,ans_text)
        self.ans2.arrange(RIGHT,buff=0.5)  # 垂直間隔0.5個單位
        self.ans2.scale_to_fit_width(4)
        self.ans2.move_to(DOWN * 2.5)

        self.play(Succession(*[Write(text) for text in self.ans2]))
        self.wait(3)
        self.play(Write(self.ans))
        self.wait(2)