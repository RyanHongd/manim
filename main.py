import os
from manim import *
import subprocess
import platform
from add_over10 import add_over10
from minus_over10 import minus_over10

class MainScene2(Scene):
    def construct(self):
        # 創建 add_over10 和 minus_over10 的實例
        add_scene = add_over10()
        minus_scene = minus_over10()

        # 執行 add_over10 的動畫
        add_scene.animation(self)

        # 執行 minus_over10 的動畫
        minus_scene.animation(self)
        




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
