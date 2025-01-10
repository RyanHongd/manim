import os
from manim import *
import subprocess
import platform
from add import add
from minus import minus
from multiplication import multiplication
from division import division
from write import write_text
from column_method import column_method

class MainScene2(Scene):
    def construct(self):
        #載入不同函式運算時使用的參數，pos是運算的順序
        add_pos, min_pos, mup_pos, div_pos,column_pos = 1, 0, 1, 0,2
        add_value1, add_value2= 16, 17  
        min_value1, min_value2= 0, 0
        mup_value1, mup_value2 = 0, 0
        div_value1, div_value2= 33, 4
        column_value1,column_value2,cal_method = 110,4,4
        #標題的內容
        title = f"放入題目"
        title_pos = UP
        title_width = 14

        #答案的內容
        answer = f"放入答案"
        answer_pos = DOWN
        answer_width = 4

        #創建需要的場景
        #title = write_text(title,title_pos,title_width)
        #add_scene = add(add_value1, add_value2, add_pos)
        #minus_scene = minus(min_value1, min_value2, min_pos)
        multiplication_scene =  multiplication(mup_value1, mup_value2, mup_pos)
        #division_scene = division(div_value1, div_value2, div_pos)
        #colume_scene = column_method(column_value1,column_value2,cal_method,column_pos)
        #answer = write_text(answer,answer_pos,answer_width)

        # 執行動畫
        #title.animation(self)
        #add_scene.animation(self)
        #minus_scene.animation(self)
        multiplication_scene.animation(self)
        #division_scene.animation(self)
        #colume_scene.animation(self)
        #answer.animation(self)
        


#下面的內容固定，不會影響影片的內容
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
