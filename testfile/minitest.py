from openai import OpenAI
import os
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
import tempfile
import subprocess

# 載入 .env 檔案中的 API 金鑰
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 設定 GPT API
client = OpenAI(api_key=api_key)

# 全域變數儲存 GPT 生成的程式碼
generated_code = ""

def read_file():
    try:
        with open('inputtest.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        print("文件內容如下：")
        print(content)
        return content
    except FileNotFoundError:
        print("找不到 input.txt 文件，請確認檔案是否存在。")
    except Exception as e:
        print(f"發生錯誤: {e}")

# 調用函數來讀取並輸出文件內容
content = read_file()

# 傳送內容給 GPT 並顯示生成的程式碼
def send_to_gpt():
    global generated_code
    user_input = user_input_textbox.get("1.0", tk.END).strip()
    combined_input = f"{user_input},{content}"
    if combined_input:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-2024-05-13",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": combined_input},
                ]
            )
            generated_code = response.choices[0].message.content.strip()
            output_textbox.delete("1.0", tk.END)
            output_textbox.insert(tk.END, generated_code)
        except Exception as e:
            output_textbox.delete("1.0", tk.END)
            output_textbox.insert(tk.END, f"Error: {e}")

# 執行 GPT 生成的程式碼
def execute_code():
    global generated_code
    if generated_code:
        try:
            # 建立臨時檔案
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
                temp_file.write(generated_code)
                temp_file_path = temp_file.name
            
            # 使用 subprocess 執行程式碼
            result = subprocess.run(
                ["python", temp_file_path],
                capture_output=True,
                text=True
            )

            # 顯示執行結果或錯誤訊息
            if result.returncode == 0:
                output_textbox.insert(tk.END, f"\n執行成功！輸出內容：\n{result.stdout}")
            else:
                output_textbox.insert(tk.END, f"\n執行失敗！錯誤內容：\n{result.stderr}")

            # 刪除臨時檔案
            os.remove(temp_file_path)
        except Exception as e:
            output_textbox.insert(tk.END, f"\n執行生成的程式碼時發生錯誤: {e}")
    else:
        output_textbox.insert(tk.END, "\n沒有生成的程式碼可執行！")

# 設定 GUI
window = tk.Tk()
window.title("GPT 訊息傳送器")

# 使用者輸入區域
input_label = tk.Label(window, text="請輸入文字：")
input_label.pack()

user_input_textbox = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=10)
user_input_textbox.pack()

# 按鈕：傳送給 GPT
send_button = tk.Button(window, text="送出給 GPT", command=send_to_gpt)
send_button.pack()

# GPT 回應區域
output_label = tk.Label(window, text="GPT 生成的程式碼：")
output_label.pack()

output_textbox = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=10)
output_textbox.pack()

# 按鈕：執行程式碼
execute_button = tk.Button(window, text="執行生成的程式碼", command=execute_code)
execute_button.pack()

# 啟動視窗主循環
window.mainloop()





