import sys
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
        current_dir = os.path.dirname(os.path.abspath(__file__))  # 取得 system.py 所在資料夾
        file_path = os.path.join(current_dir, "inputtest.txt")    # 建立絕對路徑

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        
        return content
    except FileNotFoundError:
        print("找不到 inputtest.txt 文件，請確認檔案是否存在。")
    except Exception as e:
        print(f"發生錯誤: {e}")

# 從命令列參數獲取題目
if len(sys.argv) > 1:
    user_input = sys.argv[1]
else:
    user_input = "巧克力每條13顆，小名有3條巧克力，媽媽吃掉7塊，他現在有多少顆巧克力?"

# 調用函數來讀取並輸出文件內容
content=read_file()
combined_input = f"題目是：{user_input},{content}"
print("2")

response = client.chat.completions.create(
    model="gpt-4o-2024-05-13",
    messages = [
        {"role": "system", "content": "You are a helpful assistant that only returns Python code."},
        {"role": "user", "content": combined_input}
    ]
 
)

output = response.choices[0].message.content.strip()
output = output[9:-3]

print(output)
try:
    exec(output)
except Exception as e:
    print(f"執行生成的程式碼時發生錯誤: {e}")