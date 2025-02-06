from openai import OpenAI
import os
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
from manim import UP,DOWN
from manim import *
import subprocess
import platform
from add import add
from minus import minus
from multiplication import multiplication
from division import division
from write import write_text
from column_method import column_method

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

window = tk.Tk()
window.title("GPT 訊息傳送器")
window.geometry("800x400")  # 設定初始大小

# 使用者輸入區域
input_label = tk.Label(window, text="請輸入文字：", font=("Arial", 12))
input_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

user_input_textbox = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=6, font=("Arial", 12))
user_input_textbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# 送出按鈕
send_button = tk.Button(window, text="送出給 GPT", command=send_to_gpt, font=("Arial", 12), bg="lightblue")
send_button.grid(row=2, column=0, pady=10)

# GPT 回應區域
output_label = tk.Label(window, text="GPT 回應：", font=("Arial", 12))
output_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

output_textbox = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=6, font=("Arial", 12))
output_textbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# 啟動視窗主循環
window.mainloop()