import os
from manim import *
import subprocess
import platform
from add_over10 import add_over10
from minus_over10 import minus_over10
from write import write_text

class MainScene2(Scene):
    def construct(self):
        add_value1, add_value2 = 24, 17  # 媽媽給他15塊錢
        minus_value1, minus_value2 = 41, 8
        title = f"小明有24個糖果, 媽媽給他17個,小紅又拿走他8個糖，現在共有幾個?"
        title_pos = UP
        title_width = 14

        answer = f"因此答案是33個"
        answer_pos = DOWN
        answer_width = 4

        title = write_text(title,title_pos,title_width)
        # 創建 add_over10 和 minus_over10 的實例
        add_scene = add_over10(add_value1, add_value2)
        minus_scene = minus_over10(minus_value1, minus_value2)
        answer = write_text(answer,answer_pos,answer_width)

        # 執行動畫
        title.animation(self)
        add_scene.animation(self)
        minus_scene.animation(self)
        answer.animation(self)
        



if __name__ == "__main__":
    config.media_dir = "./output_media"
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
