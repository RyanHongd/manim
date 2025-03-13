from openai import OpenAI
import os
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
from manim import UP,DOWN
from manim import *
import subprocess
import platform
'''
from vid_process.add import add
from vid_process.minus import minus
from vid_process.multiplication import multiplication
from vid_process.division import division
from vid_process.write import write_text
from vid_process.column_method import column_method
'''
# 載入 .env 檔案中的 API 金鑰
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 設定 GPT API
client = OpenAI(
    api_key = api_key
)

def read_file():
    try:
        # 開啟文件並讀取內容
        with open('inputtest.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 將內容輸出
        print("文件內容如下：")
        print(content)
        return content
    except FileNotFoundError:
        print("找不到 input.txt 文件，請確認檔案是否存在。")
    except Exception as e:
        print(f"發生錯誤: {e}")

# 調用函數來讀取並輸出文件內容
content=read_file()


# 建立視窗應用程式
def send_to_gpt():
    user_input = user_input_textbox.get("1.0", tk.END).strip()
    combined_input = f"{user_input},{content}"
    if combined_input:
        try:
            # 呼叫 OpenAI GPT API
            response = client.chat.completions.create(
                model="gpt-4o-2024-05-13",
                messages = [

                    {"role": "system", "content": "You are a helpful assistant that only returns Python code."},
                    {"role": "user", "content": combined_input},
                ]
            )
            gpt_response = response.choices[0].message.content
            
            # 清除輸出框並顯示 GPT 的回應
            output_textbox.delete("1.0", tk.END)
            output_textbox.insert(tk.END, gpt_response)

            output = response.choices[0].message.content.strip()
            output = output[9:-3]

            print(output)
            try:
                exec(output)
            except Exception as e:
                print(f"執行生成的程式碼時發生錯誤: {e}")
        except Exception as e:
            output_textbox.delete("1.0", tk.END)
            output_textbox.insert(tk.END, f"Error: {e}")

# 設定 GUI
window = tk.Tk()
window.title("GPT 訊息傳送器")

# 使用者輸入區域
input_label = tk.Label(window, text="請輸入文字：")
input_label.pack()

user_input_textbox = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=10)
user_input_textbox.pack()

# 按鈕
send_button = tk.Button(window, text="送出給 GPT", command=send_to_gpt)
send_button.pack()


# GPT 回應區域
output_label = tk.Label(window, text="GPT 回應：")
output_label.pack()

output_textbox = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=10)
output_textbox.pack()

# 啟動視窗主循環
window.mainloop()
