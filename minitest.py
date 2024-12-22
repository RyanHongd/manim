import os
from manim import *
import subprocess
import platform
from division import division
from write import write_text
from column_method import column_method

class MainScene2(Scene):
    def construct(self):
        # 載入不同函式運算時使用的參數，pos是運算的順序
        div_pos, column_pos = 0, 0

        # 把要運算的數字填入，因為我們只需要除法，所以只填入除法的參數
        div_value1, div_value2 = 1500, 4

        # 判斷是否需要使用column_method
        if div_value1 > 10 or div_value2 > 10:
            column_value1, column_value2, cal_method = div_value1, div_value2, 4
        else:
            column_value1, column_value2, cal_method = 0, 0, 0

        # 標題的內容，描述題目
        title = f"小名有30個50塊，要把這些錢分給4個人，每個人可以拿到幾塊錢?"
        title_pos = UP
        title_width = 14

        # 答案的內容，計算後的結果
        answer = f"375塊"
        answer_pos = DOWN
        answer_width = 4

        # 創建需要的場景，把需要的運算方式留著就好，剩餘的刪掉
        title = write_text(title, title_pos, title_width)
        division_scene = division(div_value1, div_value2, div_pos)
        column_scene = column_method(column_value1, column_value2, cal_method, column_pos)
        answer = write_text(answer, answer_pos, answer_width)

        # 執行動畫
        title.animation(self)
        column_scene.animation(self)  # 因為1500大於10，使用column method
        division_scene.animation(self)
        answer.animation(self)


# 下面的內容固定，不會影響影片的內容
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





