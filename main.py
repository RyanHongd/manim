import os
from manim import *
import subprocess
import platform
from add_over10 import add_over10

class MainScene(Scene):
    def construct(self):
        # 創建 add_over10 的實例並調用它的 construct 方法
        scene = add_over10()
        scene.construct()  # 執行 add_over10 內的動畫邏輯
        
        # 如果你想在 MainScene 中加入更多動畫，則可以在這裡繼續
        # 例如：




if __name__ == "__main__":
    config.media_dir = "./output_media"
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 60

    # 渲染影片
    scene = MainScene()
    scene.render()

    # 找到生成的影片路徑
    output_video_path = os.path.join(config.media_dir, "videos", "1080p60", "MainScene.mp4")
    
    # 自動打開影片
    if platform.system() == "Windows":
        os.startfile(output_video_path)  # Windows 自動打開影片
    elif platform.system() == "Darwin":  # MacOS
        subprocess.run(["open", output_video_path])
    elif platform.system() == "Linux":  # Linux
        subprocess.run(["xdg-open", output_video_path])
