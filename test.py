from manim import *
Y_offset = [1.5, 1, 0, -0.5, -1.5, -2]
def ans_print(self,s8, s9):
    ans = Text(s8, font="Noto Sans CJK", font_size=36, color=YELLOW).move_to((2, Y_offset[0], 0))
    ans1 = Text(s9, font="Noto Sans CJK", font_size=36).next_to(ans, DOWN)
    self.play(Write(ans))
    self.wait(1)
    self.play(Write(ans1))
    self.wait(1)

def description(self, s1, s2, s3, s4, s5, s6, s7):
    title = Text(s1, font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
    title.scale_to_fit_width(12)
    exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=BLUE).next_to(title, DOWN)
    exp_2 = Text(s3)
    exp_3 = Text(s4)
    exp_4 = Text(s5)
    exp_5 = Text(s6)
    exp_6 = Text(s7)
    expG = VGroup(exp_2, exp_3, exp_4, exp_5, exp_6)
    expG.arrange(DOWN, buff=0.8)
    expG.scale_to_fit_width(4)
    expG.set_color(GREEN)
    expG.set(font_size=30)
    expG.to_edge(LEFT)

    # 打印文字
    self.play(Write(title))
    self.wait(1)
    self.play(Write(exp_1))
    self.wait(1)
    self.play(Write(expG))
    self.wait(1)

def create_dot(self, units1, Pcolor, Y_offset):
    unit_dots1 = []
    for i in range(units1):
        dot = Dot(point=(i * 0.3 - 0.65, Y_offset, 0), color=Pcolor)
        unit_dots1.append(dot)
        self.play(FadeIn(dot), run_time=0.1)
    self.wait(1)
    return unit_dots1

def create_10dot(self, tens1, Pcolor, Y_offset):
    ten_circles1 = []
    for i in range(tens1):
        circle = Circle(radius=0.3, color=Pcolor).move_to((i * 0.6 - 0.65, Y_offset, 0))
        text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
        ten_circles1.append(VGroup(circle, text))
        self.play(FadeIn(ten_circles1[i]), run_time=0.1)
    self.wait(1)
    return ten_circles1

def draw_dot(self, n1, n2):
    units1 = n1 % 10
    tens1 = n1 // 10
    units2 = n2 % 10
    tens2 = n2 // 10


    unit_dots1 = create_dot(self, units1, RED, Y_offset[0])
    ten_circles1 = create_10dot(self, tens1, RED, Y_offset[1])
    unit_dots2 = create_dot(self, units2, BLUE, Y_offset[2])
    ten_circles2 = create_10dot(self, tens2, BLUE, Y_offset[3])

    all_dots = unit_dots1 + unit_dots2
    all_circles = ten_circles1 + ten_circles2
    return all_dots, all_circles

class Add_Function(Scene):
    def construct(self):
        # 创造文字（用户输入的问题）
        add_v1 = 26
        add_v2 = 17
        Add_result = add_v1 + add_v2
        s1 = f"小名有26塊錢，媽媽再給他17塊錢，曉華又拿走他8塊錢，請問小名最後有幾塊錢?"
        s2 = f"首先小名有{add_v1}塊錢 , 媽媽再給我們{add_v2}塊錢"
        s3 = f"我們可以把十位數跟個位數分開"
        s4 = f"{add_v1}可以被分成{add_v1 // 10}個10跟{add_v1 % 10}個1"
        s5 = f"{add_v2}可以被分成{add_v2 // 10}個10跟{add_v2 % 10}個1"
        s6 = f"把所有的1加起來,\n再把所有的10加起來"
        s7 = f"最後再把十位數和個位數加起來"
        s8 = f"因此我們共有{add_v1 + add_v2}塊錢"
        s9 = f"{add_v1} + {add_v2} = {Add_result}"
        # print 題目
        description(self, s1, s2, s3, s4, s5, s6, s7)

        all_dots, all_circles = draw_dot(self, add_v1, add_v2)

        # 移動個位數的點
        i = 0
        for dot in all_dots:
            dot.set_color(GREEN)
            self.play(dot.animate.move_to((i * 0.3 - 0.65, Y_offset[4], 0)), run_time=0.5)
            i += 1
        #移動十位數的點
        i = 0
        for circle in all_circles:
            circle[0].set_color(GREEN)
            circle[1].set_color(WHITE)
            self.play(circle.animate.move_to((i * 0.6 - 0.65, Y_offset[5], 0)), run_time=0.5)
            i += 1

        digits = len(all_dots)
        tens_digits = len(all_circles)
        if digits >= 10:
            digits-=10
            tens_digits+=1 
            selected_dots = all_dots[:10]
            dots_group = VGroup(*selected_dots)
        # 获取前10个dots的坐标
            dot_positions = [dot.get_center() for dot in selected_dots]

            # 创建由前10个dots连接的红线
            red_line = Line(dot_positions[0], dot_positions[-1], color=RED, stroke_width=4)
            for i in range(1, len(dot_positions) - 1):
                red_line.add_points_as_corners([dot_positions[i]])

            self.play(Create(red_line))
            self.wait(2)
            for dot in selected_dots:
                self.remove(dot)
            last_circle_group = all_circles[-1] if all_circles else None
            if last_circle_group:
                circle = Circle(radius=0.3, color=RED).next_to(last_circle_group, RIGHT)
            else:
                # 如果列表为空，直接在初始位置创建circle
                circle = Circle(radius=0.3, color=RED)
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            self.play(FadeIn(circle, text))
            all_circles.append(VGroup(circle, text))
            self.wait(1)

            ans_print(self,s8, s9) 





















