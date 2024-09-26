import os
from manim import *
import subprocess
import platform
from minus import minus
from division import division
from write import write_text

class MainScene2(Scene):
    def construct(self):
        # 載入不同函式運算時使用的參數，pos是運算的順序
        min_value1, min_value2, min_pos = 30, 8, 1  # 30 - 8
        div_value1, div_value2, div_pos = 22, 2, 2  # 剩下的錢除以2元一張紙
        div2_value1, div2_value2, div2_pos = 11, 3, 3  # 最後每人分3份紙

        # 標題的內容
        title = f"小名有30塊錢，曉華拿走他8塊，剩下的錢去買一張2元的紙，分給3個人，每個人拿到多少紙?"
        title_pos = UP
        title_width = 14

        # 答案的內容
        answer = f"因此每個人可以拿到3張紙"
        answer_pos = DOWN
        answer_width = 4

        # 創建需要的場景
        title = write_text(title, title_pos, title_width)
        minus_scene = minus(min_value1, min_value2, min_pos)
        division_scene = division(div_value1, div_value2, div_pos)
        division_scene2 = division(div2_value1, div2_value2, div2_pos)
        answer = write_text(answer, answer_pos, answer_width)

        # 執行動畫
        title.animation(self)
        minus_scene.animation(self)
        division_scene.animation(self)
        division_scene2.animation(self)
        answer.animation(self)


# 下面的內容固定，不會影響影片的內容
if __name__ == "__main__":
    config.media_dir = "./test_media"
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 60

    # 渲染影片
    scene = MainScene2()
    scene.render()

    # 找到生成的影片路徑
    output_video_path = os.path.join(config.media_dir, "videos", "1080p60", "MainScene2.mp4")
    
    # 自動打開影片
    if platform.system() == "Windows":
        os.startfile(output_video_path)  # Windows 自動打開影片
    elif platform.system() == "Darwin":  # MacOS
        subprocess.run(["open", output_video_path])
    elif platform.system() == "Linux":  # Linux
        subprocess.run(["xdg-open", output_video_path])



























