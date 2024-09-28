from manim import *

class Test(Scene):
    def construct(self):
        # 請求用戶輸入 n 的值
        n = input("請輸入 n 的值: ")

        # 使用 f-string 動態生成文字
        text = Text(
            f"因此我們最後有 {n} 顆",
            font="Noto Sans CJK",
            font_size=30,
            color=YELLOW
        ).to_edge(DOWN)

        self.play(Write(text))
        self.wait(2)

# 在腳本執行時運行該場景
if __name__ == "__main__":
    from manim import config
    config.media_width = "75%"
    scene = Test()
    scene.render()