from manim import *
import os
import subprocess
import platform
import math
from manim import *

class LongDivision(Scene):
    def construct(self):
        n1 = 58   # 被除數
        n2 = 3    # 除數
        self.ans = n1 // n2
        self.remainder = n1 % n2

        # 根號符號
        arc = Arc(radius=0.4, angle=PI / 2.8, start_angle=-0.7, color=WHITE).shift(LEFT * 1.5 + UP * 1)
        line = Line(start=arc.get_end(), end=arc.get_end() + RIGHT * 2, color=WHITE)

        # 顯示根號符號
        self.play(Create(arc), Create(line))
        self.wait(1)

        # 被除數和除數
        self.list1 = [int(d) for d in str(n1)]  # 被除數的每一位
        self.list2 = [int(d) for d in str(n2)]  # 除數（假設只有一位數）

        # 顯示被除數
        printlist1 = []
        for i, digit in enumerate(self.list1):
            num = Text(f"{digit}", font="Noto Sans CJK", font_size=24).move_to(((i * 0.5) - 0.5, 0.9, 0))
            printlist1.append(num)
        
        for num in printlist1:
            self.play(FadeIn(num), run_time=0.1)

        # 顯示除數
        num_divisor = Text(f"{self.list2[0]}", font="Noto Sans CJK", font_size=24).move_to(LEFT * 2 + UP * 0.9)
        self.play(FadeIn(num_divisor))
        self.wait(1)

        # 顯示商（計算過程）
        quotient = n1 // n2
        quotient_digits = [int(d) for d in str(quotient)]
        printlist3 = []
        for i, digit in enumerate(quotient_digits):
            num = Text(f"{digit}", font="Noto Sans CJK", font_size=24).move_to((i * 0.5, -0.5, 0))
            printlist3.append(num)

        # 顯示商
        for num in printlist3:
            self.play(FadeIn(num), run_time=0.1)
        self.wait(1)

        # 開始逐步除法過程，包含進位和減法
        position_x = -0.5  # 用來追踪當前除法位置
        current_number = 0  # 當前運算的數

        for i, digit in enumerate(self.list1):
            # 加入下一位數進行除法
            current_number = current_number * 10 + digit
            num_text = Text(f"{current_number}", font="Noto Sans CJK", font_size=24).move_to((position_x, 0.5, 0))
            self.play(FadeIn(num_text))
            self.wait(0.5)

            # 計算當前位的商
            if current_number >= n2:
                current_quotient = current_number // n2
                current_remainder = current_number % n2

                # 顯示當前的商
                quotient_text = Text(f"{current_quotient}", font="Noto Sans CJK", font_size=24).move_to((position_x, -0.5, 0))
                self.play(FadeIn(quotient_text))
                self.wait(0.5)

                # 計算並顯示減法結果
                subtract_text = Text(f"-{current_quotient * n2}", font="Noto Sans CJK", font_size=24).move_to((position_x, 0.2, 0))
                self.play(FadeIn(subtract_text))
                self.wait(0.5)

                # 顯示減法後的餘數
                remainder_text = Text(f"{current_remainder}", font="Noto Sans CJK", font_size=24).move_to((position_x, -0.2, 0))
                self.play(FadeIn(remainder_text))
                self.wait(0.5)

                # 更新 current_number 為餘數，用於下一位計算
                current_number = current_remainder

            # 移動到下一位數的計算位置
            position_x += 0.5

        self.wait(2)



if __name__ == "__main__":
    config.media_dir = "./test_media"
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 60

    # 渲染影片
    scene = LongDivision()
    scene.render()

    # 找到生成的影片路徑
    output_video_path = os.path.join(config.media_dir, "videos", "1080p60", "LongDivision.mp4")
    
    # 自動打開影片
    if platform.system() == "Windows":
        os.startfile(output_video_path)  # Windows 自動打開影片
    elif platform.system() == "Darwin":  # MacOS
        subprocess.run(["open", output_video_path])
    elif platform.system() == "Linux":  # Linux
        subprocess.run(["xdg-open", output_video_path])






