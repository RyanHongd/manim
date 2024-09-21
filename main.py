import os
from manim import *
import subprocess
import platform
from add import add
from minus import minus
from multiplication import multiplication
from division import division
from write import write_text

class MainScene2(Scene):
    def construct(self):
        add_value1, add_value2, add_pos = 6, 2, 1  # 媽媽給他15塊錢
        min_value1, min_value2, min_pos = 0, 0, 0
        mup_value1, mup_value2, mup_pos = 0, 0, 0
        div_value1, div_value2, div_pos = 8, 4, 2

        title = f"現在有6個男生，2個女生，要把他們每4人分一組，請問可以分成幾組?"
        title_pos = UP
        title_width = 14

        answer = f"因此答案是2組"
        answer_pos = DOWN
        answer_width = 4

        title = write_text(title,title_pos,title_width)
        # 創建 add_over10 和 minus_over10 的實例
        add_scene = add(add_value1, add_value2, add_pos)
        #minus_scene = minus(min_value1, min_value2, min_pos)
        #multiplication_scene = multiplication(mup_value1, mup_value2, mup_pos)
        division_scene = division(div_value1, div_value2, div_pos)
        answer = write_text(answer,answer_pos,answer_width)

        # 執行動畫
        title.animation(self)
        add_scene.animation(self)
        #minus_scene.animation(self)
        #multiplication_scene.animation(self)
        division_scene.animation(self)
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
