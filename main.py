import os
from manim import *
import subprocess
import platform
from add_over10 import add_over10
from minus_over10 import minus_over10
from write import write_text

class MainScene2(Scene):
    def construct(self):
        n1, n2 = 24, 13  
        m1, m2 = 33, 8
        title = f"小明有24個糖果, 媽媽給他17個,小紅又拿走他8個糖，現在共有幾個?"
        pos = UP
        width=14

        text1 = write_text(title,pos,width)
        # 創建 add_over10 和 minus_over10 的實例
        add_scene = add_over10(n1, n2)
        minus_scene = minus_over10(m1, m2)

        # 執行動畫
        text1.animation(self)
        add_scene.animation(self)
        minus_scene.animation(self)
        
    def create_title(self):
        self.n1=24
        self.n2=13
        self.n3=8
        
        title = f"小明有{self.n1}個糖果, 媽媽給他{self.n2}個,小紅又拿走他{self.n3}塊錢 現在共有幾個?"
        self.title = Text(title, font="Noto Sans CJK", font_size=33, color=YELLOW).to_edge(UP)
        self.title.scale_to_fit_width(14)
        self.play(Write(self.title))



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
