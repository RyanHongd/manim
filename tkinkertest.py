from openai import OpenAI
import os
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv

# 載入 .env 檔案中的 API 金鑰
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 設定 GPT API
client = OpenAI(
    api_key = api_key
)


# 建立視窗應用程式
def send_to_gpt():
    user_input = user_input_textbox.get("1.0", tk.END).strip()
    if user_input:
        try:
            # 呼叫 OpenAI GPT API
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages = [

                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input},
                ]
            )
            gpt_response = response.choices[0].message.content
            
            # 清除輸出框並顯示 GPT 的回應
            output_textbox.delete("1.0", tk.END)
            output_textbox.insert(tk.END, gpt_response)
        except Exception as e:
            output_textbox.delete("1.0", tk.END)
            output_textbox.insert(tk.END, f"Error: {e}")

# 設定 GUI
window = tk.Tk()
window.title("GPT 訊息傳送器")

# 使用者輸入區域
input_label = tk.Label(window, text="請輸入文字：")
input_label.pack()

user_input_textbox = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=10)
user_input_textbox.pack()

# 按鈕
send_button = tk.Button(window, text="送出給 GPT", command=send_to_gpt)
send_button.pack()

# GPT 回應區域
output_label = tk.Label(window, text="GPT 回應：")
output_label.pack()

output_textbox = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=10)
output_textbox.pack()

# 啟動視窗主循環
window.mainloop()
