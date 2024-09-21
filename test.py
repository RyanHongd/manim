import os
from manim import *
import subprocess
import platform
from add import add_over10
from minus import minus_over10
from write import write_text

class MainScene2(Scene):
    def construct(self):
        # 題目參數設置
        initial_value = 30  # 小名有30塊錢
        minus_value = 8     # 曉華拿走他8塊錢
        add_value = 15      # 媽媽再給他15塊錢
        
        # 題目文字
        title = f"小名有30塊錢, 曉華拿走他8塊錢, 媽媽再給他15塊錢，現在共有幾塊錢?"
        title_pos = UP
        title_width = 14

        # 計算結果的文字
        answer = f"因此答案是37塊錢"
        answer_pos = DOWN
        answer_width = 4

        # 顯示題目
        title = write_text(title, title_pos, title_width)

        # 執行減法運算（30 - 8 = 22）
        minus_scene = minus_over10(initial_value, minus_value)
        
        # 執行加法運算（22 + 15 = 37）
        add_scene = add_over10(30 - minus_value, add_value)

        # 顯示答案
        answer = write_text(answer, answer_pos, answer_width)

        # 執行動畫
        title.animation(self)
        minus_scene.animation(self)
        add_scene.animation(self)
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


























