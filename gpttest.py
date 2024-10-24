from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key = api_key
)

# 開啟並讀取 input.txt 檔案
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


response = client.chat.completions.create(
    model="gpt-4o-2024-05-13",
    messages = [
        {"role": "system", "content": "You are a helpful assistant that only returns Python code."},
        {"role": "user", "content": content}
    ]

)

output = response.choices[0].message.content.strip()
output = output[9:-3]

print(output)
try:
    exec(output)
except Exception as e:
    print(f"執行生成的程式碼時發生錯誤: {e}")