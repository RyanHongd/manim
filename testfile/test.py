import os
from manim import *
import subprocess
import platform
import math

class column_method(Scene):
    def construct(self):
        n1 = 36
        n2 = 25
        self.cal_method = 1

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

        self.create_base()
        self.method()
    
    def create_base(self):
        line = Line(start=LEFT * 2 + DOWN * 1, end=RIGHT * 4 + DOWN * 1, color=WHITE)
        # 顯示直線
        self.play(Create(line))

    def method(self):
        match self.cal_method:
            case 1:
                ans = self.n1 + self.n2
                carry = 0  # 記錄進位

                # 顯示加號
                opr_method = Text("+", font="Noto Sans CJK", font_size=24).move_to(LEFT * 1.75 + DOWN * 0.5)
                self.play(FadeIn(opr_method))
                self.wait(2)

                printlist1 = []
                printlist2 = []
                printlist3 = []
                carry_texts = []  # 存儲進位顯示物件

                # 顯示被加數
                for i in range(self.t1):
                    num = Text(f"{self.list1[i]}", font="Noto Sans CJK", font_size=24).move_to(((i * -0.5) + 3.5, 0, 0))
                    printlist1.append(num)
                
                for num in printlist1:
                    self.play(FadeIn(num), run_time=0.1)
                self.wait(2)

                # 顯示加數
                for i in range(self.t2):
                    num = Text(f"{self.list2[i]}", font="Noto Sans CJK", font_size=24).move_to(((i * -0.5) + 3.5, -0.5, 0))
                    printlist2.append(num)
                
                for num in printlist2:
                    self.play(FadeIn(num), run_time=0.1)
                self.wait(2)

                # 計算答案並處理進位
                self.t3 = max(self.t1, self.t2)  # 取位數最大值
                for i in range(self.t3):    
                    # 加數、被加數以及進位的計算
                    sum_val = (self.list1[i] if i < self.t1 else 0) + (self.list2[i] if i < self.t2 else 0) + carry
                    carry = sum_val // 10  # 判斷進位
                    digit = sum_val % 10

                    # 顯示當前位數的結果
                    num = Text(f"{digit}", font="Noto Sans CJK", font_size=24).move_to(((i * -0.5) + 3.5, -1.5, 0))
                    printlist3.append(num)   

                    # 若進位存在，顯示進位1
                    if carry > 0:
                        carry_text = Text("1", font="Noto Sans CJK", font_size=24, color=YELLOW).move_to(((i * -0.5) + 3.0, -1, 0))
                        carry_texts.append(carry_text)
                        self.play(FadeIn(carry_text), run_time=0.5)

                # 顯示計算結果數字
                for num in printlist3:
                    self.play(FadeIn(num), run_time=0.1)
                self.wait(2)

                # 隱藏進位顯示
                for carry_text in carry_texts:
                    self.play(FadeOut(carry_text), run_time=0.5)



# 下面的內容固定，不會影響影片的內容
if __name__ == "__main__":
    config.media_dir = "./test_media"
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



























