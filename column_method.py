import os
from manim import *
import subprocess
import platform
import math

STD_FONT = {'font': "Noto Sans CJK", 'font_size': 24}

class column_method(Scene):
    def construct(self):
        n1 = 27
        n2 = 9
        self.cal_method = 4

        self.n1 = n1
        self.n2 = n2
        self.list1 = []
        self.list2 = []
        self.list3 = []

        # 分解位數
        self.t1 = math.floor(math.log10(abs(n1))) + 1
        for i in range(self.t1):
            digit = (n1 // (10 ** i)) % 10
            self.list1.append(digit)

        self.t2 = math.floor(math.log10(abs(n2))) + 1
        for i in range(self.t2):
            digit = (n2 // (10 ** i)) % 10
            self.list2.append(digit)

        
        self.method()
    
    def create_base(self):
        line = Line(start=LEFT * 2 , end=RIGHT * 4 , color=WHITE)
        # 顯示直線
        self.play(Create(line))

    def method(self):
        match self.cal_method:
            #加法
            case 1:
                self.create_base()
                ans = self.n1 + self.n2
                carry = 0  # 記錄進位

                # 顯示加號
                opr_method = Text("+", **STD_FONT).move_to(LEFT * 1.75 + DOWN * -0.5)
                self.play(FadeIn(opr_method))
                self.wait(2)

                printlist1 = []
                printlist2 = []
                printlist3 = []
                carry_texts = []  # 存儲進位顯示物件

                # 顯示被加數
                for i in range(self.t1):
                    num = Text(f"{self.list1[i]}", **STD_FONT).move_to(((i * -0.5) + 3.5, 1, 0))
                    printlist1.append(num)
                
                for num in printlist1:
                    self.play(FadeIn(num), run_time=0.1)

                # 顯示加數
                for i in range(self.t2):
                    num = Text(f"{self.list2[i]}", **STD_FONT).move_to(((i * -0.5) + 3.5, 0.5, 0))
                    printlist2.append(num)
                
                for num in printlist2:
                    self.play(FadeIn(num), run_time=0.1)
                self.wait(2)

                # 計算答案並處理進位
                self.t3 =  math.floor(math.log10(abs(ans))) + 1  
                for i in range(self.t3):    
                    # 加數、被加數以及進位的計算
                    sum_val = (self.list1[i] if i < self.t1 else 0) + (self.list2[i] if i < self.t2 else 0) + carry
                    carry = sum_val // 10  # 判斷進位
                    digit = sum_val % 10

                    # 顯示當前位數的結果
                    num = Text(f"{digit}", **STD_FONT).move_to(((i * -0.5) + 3.5, -0.5, 0))
                    printlist3.append(num)   

                    # 若進位存在，顯示進位1
                    if carry > 0:
                        carry_text = Text("1", font="Noto Sans CJK", font_size=20, color=YELLOW).move_to(((i * -0.5) + 3.0, 1.5, 0))
                        carry_texts.append(carry_text)
                        self.play(FadeIn(carry_text), run_time=0.5)
                
                
                # 顯示計算結果數字
                for num in printlist3:
                    self.play(FadeIn(num), run_time=0.1)
                self.wait(2)

                # 隱藏進位顯示
                for carry_text in carry_texts:
                    self.play(FadeOut(carry_text), run_time=0.5)
                self.wait(2)
            
            #減法
            case 2:
                self.create_base()
                ans = self.n1 - self.n2
                opr_method = Text("-", font="Noto Sans CJK", font_size=30).move_to(LEFT * 1.75 + DOWN * -0.5)
                self.play(FadeIn(opr_method))
                self.wait(2)

                printlist1 = []
                printlist2 = []
                printlist3 = []
                borrow_texts = []  # 存儲退位顯示物件

                # 顯示被減數
                for i in range(self.t1):
                    num = Text(f"{self.list1[i]}", **STD_FONT).move_to(((i * -0.5) + 3.5, 1, 0))
                    printlist1.append(num)
                
                for num in printlist1:
                    self.play(FadeIn(num), run_time=0.1)

                # 顯示減數
                for i in range(self.t2):
                    num = Text(f"{self.list2[i]}", **STD_FONT).move_to(((i * -0.5) + 3.5, 0.5, 0))
                    printlist2.append(num)
                
                for num in printlist2:
                    self.play(FadeIn(num), run_time=0.1)
                self.wait(2)


                # 計算答案並處理退位
                self.t3 =  math.floor(math.log10(abs(ans))) + 1  
                for i in range(self.t3):
                    digit = (ans // (10 ** i)) % 10
                    self.list3.append(digit)

                cal_time = self.t2
                for i in range(cal_time):
                    if self.list1[i] < self.list2[i] :
                        #退位且前一位數大於0   
                        if self.list1[i+1] > 0:
                            #斜線
                            num_pos = printlist1[i+1]
                            line_start = num_pos.get_corner(UP + LEFT)  # 左上角
                            line_end = num_pos.get_corner(DOWN + RIGHT)  # 右下角
                            strike_through = Line(line_start, line_end, color=RED, stroke_width=5)
                            crossed_number = VGroup(num_pos, strike_through)
                            self.play(FadeIn(crossed_number))
                            
                            borrow_text = Text("10", font="Noto Sans CJK", font_size=18, color=YELLOW).move_to((((i-1) * -0.5) + 3.0, 1.5, 0))
                            borrow_texts.append(borrow_text)
                            self.play(FadeIn(borrow_text), run_time=0.5)

                            self.play(FadeOut(crossed_number))
                            replace_num = Text(f"{self.list1[i+1]-1}", **STD_FONT).move_to(num_pos)
                            self.play(FadeIn(replace_num))
                        
                        else:
                            #找大於0的位數並記錄
                            tag = 0
                            for j in range(self.t1):
                                if self.list1[j+i+1] != 0:
                                    tag = j
                                    break

                            #從此位數往回退位
                            while  tag >= 0:
                                
                                num_pos = printlist1[tag+i+1]
                                if self.list1[tag+i+1] > 0:
                                    line_start = num_pos.get_corner(UP + LEFT)  # 左上角
                                    line_end = num_pos.get_corner(DOWN + RIGHT)  # 右下角
                                    strike_through = Line(line_start, line_end, color=RED, stroke_width=5)
                                    crossed_number = VGroup(num_pos, strike_through)
                                    self.play(FadeIn(crossed_number))
                                    self.wait(1)
                                    self.play(FadeOut(crossed_number))
                                    replace_num = Text(f"{self.list1[tag+i+1]-1}", **STD_FONT).move_to(num_pos)
                                    self.play(FadeIn(replace_num))
                                
                                    borrow_text = Text("10", font="Noto Sans CJK", font_size=18, color=YELLOW).move_to((num_pos))
                                    borrow_texts.append(borrow_text)
                                    self.play(borrow_text.animate.shift(RIGHT * 0.5 + UP * 0.5))
                                
                                
                                #當下一位數為0繼續退位，從以退位的10再提出1給下一位數
                                else:
                                    
                                    line_start = borrow_texts[-1].get_left() + LEFT * 0.1 + UP * 0.1  # 左上角
                                    line_end = borrow_texts[-1].get_right() + RIGHT * 0.1 + DOWN * 0.1  # 右下角
                                    strike_through = Line(line_start, line_end, color=RED, stroke_width=5)
                                    crossed_number = VGroup(borrow_texts[-1], strike_through)
                                    self.play(FadeIn(crossed_number))
                                    self.wait(1)
                                    self.play(FadeOut(crossed_number))
                                    replace_num = Text("9", font="Noto Sans CJK", font_size=18, color=YELLOW).move_to(borrow_texts[-1])
                                    self.play(FadeIn(replace_num))
                                    self.list1[tag+i+1]=9

                                    borrow_text = Text("10", font="Noto Sans CJK", font_size=18, color=YELLOW).move_to((borrow_texts[-1]))
                                    borrow_texts.append(borrow_text)
                                    self.play(borrow_text.animate.shift(RIGHT * 0.5))
                                    self.wait(1)

                                tag-=1
                    
                self.wait(1)
                # 顯示計算結果數字
                for i in range(self.t3):
                    num = Text(f"{self.list3[i]}", **STD_FONT).move_to(((i * -0.5) + 3.5, -0.5, 0))
                    printlist3.append(num)
                
                for num in printlist3:
                    self.play(FadeIn(num), run_time=0.1)
                self.wait(2)

                # 隱藏退位顯示
                for borrow_text in borrow_texts:
                    self.play(FadeOut(borrow_text), run_time=0.5)
                    
            case 3:
                self.create_base()
                ans = self.n1 * self.n2
                carry = 0
                sum_num = 0

                opr_method = Text(f"x", **STD_FONT).move_to(LEFT * 1.75 + DOWN * -0.5)
                scene.play(FadeIn(opr_method))
                self.wait(2)

                printlist1 = []
                printlist2 = []
                printlist3 = []
                carry_texts = [] 

                for i in range(self.t1):
                    num = Text(f"{self.list1[i]}", **STD_FONT).move_to(((i * -0.5) + 3.5, 1, 0))
                    printlist1.append(num)
                
                for num in printlist1:
                    self.play(FadeIn(num), run_time=0.1)

                # 顯示減數
                for i in range(self.t2):
                    num = Text(f"{self.list2[i]}", **STD_FONT).move_to(((i * -0.5) + 3.5, 0.5, 0))
                    printlist2.append(num)
                
                for num in printlist2:
                    self.play(FadeIn(num), run_time=0.1)
                self.wait(2)

                self.t3 =  math.floor(math.log10(abs(ans))) + 1  
                for i in range(self.t2):
                    for j in range(self.t1):    
                        # 加數、被加數以及進位的計算
                        sum_val = (self.list1[j] if j < self.t1 else 0) * (self.list2[i] if i < self.t2 else 0) + carry
                        carry = sum_val // 10  # 判斷進位
                        digit = sum_val % 10

                        

                        
                        # 若進位存在，顯示進位1
                        if carry > 0:
                            carry_text = Text(f"{carry}", font="Noto Sans CJK", font_size=20, color=YELLOW).move_to((((i+j) * -0.5) + 3.0, 1.5, 0))
                            carry_texts.append(carry_text)
                            self.play(FadeIn(carry_text), run_time=0.5)
                        self.wait(1)

                        
                    nnow = self.list2[i] * self.n1
                    
                    if nnow!=0:
                        self.sum_t =  math.floor(math.log10(abs(nnow))) + 1
                    else:
                        self.sum_t =1
                    for k in range(self.sum_t):
                        digit = (nnow // (10 ** k)) % 10
                        self.list3.append(digit)
                    
                    for k in range(self.sum_t):
                        num = Text(f"{self.list3[k]}", **STD_FONT).move_to((((k+i) * -0.5) + 3.5,(i * -0.5)-0.5, 0))
                        printlist3.append(num)
                    
                    for num in printlist3:
                        self.play(FadeIn(num), run_time=0.1)

                    self.wait(1)
                    self.list3.clear()
                    printlist3.clear()
                    for carry_t in carry_texts:
                        self.play(FadeOut(carry_t), run_time=0.1)
                    
                    carry_texts.clear()
                    

                for i in range(self.t3):
                    digit = (ans // (10 ** i)) % 10
                    self.list3.append(digit)

                for i in range(self.t3):
                    num = Text(f"{self.list3[i]}", **STD_FONT).move_to(((i * -0.5) + 3.5, -2, 0))
                    printlist3.append(num)

                line2 = Line(start=LEFT * 2 + DOWN * 1.5, end=RIGHT * 4 + DOWN * 1.5, color=WHITE)
                #顯示直線
                self.play(Create(line2))
                for num in printlist3:
                    self.play(FadeIn(num), run_time=0.1)
                self.wait(2)

                

            case 4:
                ans = int(self.n1 / self.n2)
                

                #創建除法的框線
                arc = Arc(radius=0.4, angle=PI / 2.8, start_angle=-0.7, color=WHITE).shift(LEFT * 2 + UP * 1)
                line = Line(
                    start=arc.get_end(), 
                    end=arc.get_end() + RIGHT * 2, 
                    color=WHITE
                )

                self.play(Create(arc), Create(line))
                self.wait(2)

                self.list4 = []
                self.list5 = []
                printlist1 = []
                printlist2 = []
                printlist3 = []
                remainlist = []
                carry_texts = []  # 存儲進位顯示物件
                remain_num = self.n1

                # 顯示被除數
                for i in range(self.t1):
                    num = Text(f"{self.list1[i]}", **STD_FONT).move_to(((i * -0.5), 0.9, 0))
                    printlist1.append(num)
                
                for num in printlist1:
                    self.play(FadeIn(num), run_time=0.1)

                # 顯示除數
                for i in range(self.t2):
                    num = Text(f"{self.list2[i]}", **STD_FONT).move_to(((i * -0.5)-1.85, 0.9, 0))
                    printlist2.append(num)
                
                for num in printlist2:
                    self.play(FadeIn(num), run_time=0.1)
                self.wait(2)

                self.t3 =  math.floor(math.log10(abs(ans))) + 1
                for i in range(self.t3):
                    digit = (ans // (10 ** i)) % 10
                    self.list3.append(digit)

                for idx, value in enumerate(reversed(self.list3)):
                    for i in range(self.t1):
                        num = Text(f"{self.n1 // (10 ** (self.t1-i-1))}", **STD_FONT, color=BLUE).move_to((3,0, 0))
                        self.play(FadeIn(num), run_time=0.1)
                        self.wait(1)
                        '''
                        if self.n2 * value <= self.n1 // (10 ** (self.t1-i-1)):
                            
                            idx+=i
                        '''

                    
                    # 顯示反向排列的 `self.list3` 值
                    printans = Text(f"{value}", **STD_FONT).move_to(((idx * 0.5)-0.5, 1.5, 0))
                    self.play(FadeIn(printans), run_time=0.1)
                    self.wait(1)
                    if self.n2 * value==0:
                        nt=1
                    else:
                        nt =  math.floor(math.log10(abs(self.n2 * value))) + 1
                    
                    for i in range(nt):
                        digit = (self.n2 * value // (10 ** i)) % 10
                        self.list4.append(digit)
                        num = Text(f"{self.list4[-i]}", **STD_FONT, color=BLUE).move_to(((idx * 0.5)+(i * -0.5), (idx * -0.8)+0.4, 0))
                        self.play(FadeIn(num), run_time=0.1)
                        self.wait(1)
                    
                    line = Line(start=LEFT * 1.6 + DOWN * (idx* 0.8-0.2) , end=RIGHT * 1.6 + DOWN * (idx* 0.8-0.2), color=WHITE)
                    # 顯示直線
                    self.play(Create(line))
                    self.list4.clear()

                    remain_num =  remain_num - self.n2 * value * (10 ** (nt-idx))
                    if remain_num==0:
                        nt2=1
                    else:
                        nt2 =  math.floor(math.log10(abs(remain_num))) + 1
                    
                    if idx!=self.t3-1:
                        for i in range(nt2):
                            digit = int((remain_num // (10 ** i)) % 10)
                            self.list5.append(digit)
                            num = Text(f"{self.list5[-i]}", **STD_FONT, color=RED).move_to(((idx * 0.5)+(i * -0.5), (idx * -0.8), 0))
                            self.play(FadeIn(num), run_time=0.1)
                            self.wait(1)
                    
                    self.list5.clear()
                    #reversed_list1 = self.list1[::-1]
                    #if reversed_list1[i] != self.n2 * value
                remain_num = self.n1 % self.n2
                num = Text(f"{remain_num}", **STD_FONT, color=RED).move_to(((idx * 0.5)+((i+1) * -0.5), (idx * -0.8), 0))
                self.play(FadeIn(num), run_time=0.1)
                self.wait(1)

                
                self.wait(2)

                
if __name__ == "__main__":
    config.media_dir = "./output_media"
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 60

    # 渲染影片
    scene = column_method()
    scene.render()

    # 找到生成的影片路徑
    output_video_path = os.path.join(config.media_dir, "videos", "1080p60", "column_method.mp4")
    
    # 自動打開影片
    if platform.system() == "Windows":
        os.startfile(output_video_path)  # Windows 自動打開影片
    elif platform.system() == "Darwin":  # MacOS
        subprocess.run(["open", output_video_path])
    elif platform.system() == "Linux":  # Linux
        subprocess.run(["xdg-open", output_video_path])