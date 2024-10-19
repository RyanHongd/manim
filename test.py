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
        # 由於這是組合運算，所以第二個運算方式的參數會有一個來自前面運算
        min_value1, min_value2, min_pos = 30, 8, 1
        div_value1, div_value2, div_pos = 22, 4, 2  # 第一個運算結果22是min_value1-min_value2的結果

        # 標題的內容
        title = "小明原有30塊，曉華拿走8塊，剩下的錢分給4人"
        title_pos = UP
        title_width = 14

        # 答案的內容
        answer = "每個人可以得到5.5塊錢"
        answer_pos = DOWN
        answer_width = 14

        # 創建需要的場景
        title_scene = write_text(title, title_pos, title_width)
        minus_scene = minus(min_value1, min_value2, min_pos)
        division_scene = division(div_value1, div_value2, div_pos)
        answer_scene = write_text(answer, answer_pos, answer_width)

        # 執行動畫
        self.play(Create(title_scene))
        self.play(minus_scene.animation(self))
        self.play(division_scene.animation(self))
        self.play(Create(answer_scene))


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



























