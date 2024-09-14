import os
from manim import *
import subprocess
import platform
from add_over10 import add_over10
from minus_over10 import minus_over10
from write import write_text

class MainScene2(Scene):
    def construct(self):
        # 更新參數
        n1, n2 = 30, 15  # 加法參數
        m1, m2 = 45, 8   # 減法參數 (加法的結果 30 + 15 = 45)

        # 更新標題和答案
        title = f"小名有30塊錢，媽媽再給他15塊錢，曉華又拿走他8塊錢，請問小名最後有幾塊錢?"
        title_pos = UP
        title_width = 14

        answer = f"因此答案是37塊錢"
        answer_pos = DOWN
        answer_width = 4

        # 使用 write_text 函式顯示標題
        title = write_text(title, title_pos, title_width)

        # 創建 add_over10 和 minus_over10 的實例
        add_scene = add_over10(n1, n2)
        minus_scene = minus_over10(m1, m2)

        # 使用 write_text 函式顯示答案
        answer = write_text(answer, answer_pos, answer_width)

        # 執行動畫
        title.animation(self)
        add_scene.animation(self)
        minus_scene.animation(self)
        answer.animation(self)

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
























