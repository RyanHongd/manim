from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key = api_key
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a helpful assistant that only returns Python code."},
        {"role": "user", "content": """我需要生成一個 Python 迴圈，具體要求如下：
        
        1. 現在有題目是:小名有30塊錢，曉華拿走他8塊錢，剩下的錢要分給4個人，每個人可以拿到幾塊錢?
         請你幫我調整參數和函式的順序，以符合題目的要求，其他都不要更改，你只能改MainScen2裡的內容，最後給我一個manim影片的程式碼 
        *write_text處理文字
        *由於這是組合運算，所以之後的運算方式的參數會有一個來自前面運算
        *請你把不需要的運算方式刪掉，同時更改pos，以符合運算順序
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
                #載入不同函式運算時使用的參數，pos是運算的順序
                add_value1, add_value2, add_pos = 16, 17, 1  
                min_value1, min_value2, min_pos = 0, 0, 0
                mup_value1, mup_value2, mup_pos = 0, 0, 0
                div_value1, div_value2, div_pos = 33, 4, 2

                #標題的內容
                title = f"現在有16個男生，17個女生，要把他們每4人分一組，請問可以分成幾組?"
                title_pos = UP
                title_width = 14

                #答案的內容
                answer = f"因此答案是8組，剩下一個人"
                answer_pos = DOWN
                answer_width = 4

                #創建需要的場景
                title = write_text(title,title_pos,title_width)
                add_scene = add(add_value1, add_value2, add_pos)
                minus_scene = minus(min_value1, min_value2, min_pos)
                multiplication_scene = multiplication(mup_value1, mup_value2, mup_pos)
                division_scene = division(div_value1, div_value2, div_pos)
                answer = write_text(answer,answer_pos,answer_width)

                # 執行動畫
                title.animation(self)
                add_scene.animation(self)
                minus_scene.animation(self)
                multiplication_scene.animation(self)
                division_scene.animation(self)
                answer.animation(self)
                


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
                subprocess.run(["xdg-open", output_video_path])

        2. 請注意，回應中僅需包含可執行的程式碼，不要有額外的文字。
                """}
    ]

)

output = response.choices[0].message.content.strip()
output = output[9:-3]

print(output)
try:
    exec(output)
except Exception as e:
    print(f"執行生成的程式碼時發生錯誤: {e}")