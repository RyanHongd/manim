import os
from manim import *
import subprocess
import platform

class column_method(Scene):
    def construct(self):
        n1=100
        n2=21
        self.n1 = n1
        self.n2 = n2
        self.cal_method = 3

        self.create_base()
        self.method()
    
    def create_base(self):
        line = Line(start = LEFT * 2 + DOWN*1, end = RIGHT * 2 + DOWN*1, color=WHITE)

        # 顯示直線
        self.play(Create(line))
        

    def method(self):
        match self.cal_method:
            case 1:
                self.ans = self.n1 + self.n2

                opr_method = Text(f"+", font="Noto Sans CJK", font_size=24).move_to(LEFT * 1.75 + DOWN*0.5)
                scene.play(FadeIn(opr_method))
                self.wait(2)
            case 2:
                self.ans = self.n1 - self.n2

                opr_method = Text(f"-", font="Noto Sans CJK", font_size=24).move_to(LEFT * 1.75 + DOWN*0.5)
                scene.play(FadeIn(opr_method))
                self.wait(2)
            case 3:
                self.ans = self.n1 * self.n2

                opr_method = Text(f"x", font="Noto Sans CJK", font_size=24).move_to(LEFT * 1.75 + DOWN*0.5)
                scene.play(FadeIn(opr_method))
                self.wait(2)
            case 4:
                self.ans = self.n1 / self.n2

                opr_method = Text(f"÷", font="Noto Sans CJK", font_size=24).move_to(LEFT * 1.75 + DOWN*0.5)
                scene.play(FadeIn(opr_method))
                self.wait(2)
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