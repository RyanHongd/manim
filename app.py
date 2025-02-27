import os
from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

app = Flask(__name__)
CORS(app)  # 讓前端能夠存取這個 Flask 伺服器
VIDEO_PATH = "output_media/videos/1080p60/MainScene2.mp4"

# 讀取 inputtest.txt 內容
def read_file():
    try:
        with open('inputtest.txt', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "找不到 inputtest.txt"
    except Exception as e:
        return f"發生錯誤: {e}"

@app.route('/generate', methods=['POST'])
def generate_video():
    data = request.json
    user_input = data.get("text", "").strip()

    if not user_input:
        return jsonify({"error": "請輸入數學問題"}), 400

    # 合併題目與 `inputtest.txt` 內容
    content = read_file()
    combined_input = f"題目是：{user_input},{content}"
    print(combined_input)
    # 呼叫 GPT 產生 Python 影片程式碼
    response = client.chat.completions.create(
        model="gpt-4o-2024-05-13",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that only returns Python code."},
            {"role": "user", "content": combined_input}
        ]
    )

    output = response.choices[0].message.content.strip()
    output = output[9:-3]  # 去除 ```python ``` 和 ``` 結尾

    print("GPT 產生的 Python 代碼：")
    print(output)

    # 執行 GPT 產生的 Python 代碼
    try:
        exec(output)  # 直接執行 Python 影片程式碼
    except Exception as e:
        return jsonify({"error": "執行生成的程式碼時發生錯誤", "details": str(e)}), 600

    # 確認影片是否成功生成
    if os.path.exists(VIDEO_PATH):
        return jsonify({"message": "影片已生成", "video_url": "http://127.0.0.1:5000/download"})
    else:
        return jsonify({"error": "影片生成失敗"}), 500

@app.route('/download', methods=['GET'])
def download_video():
    if os.path.exists(VIDEO_PATH):
        return send_file(VIDEO_PATH, as_attachment=True)
    else:
        return jsonify({"error": "影片不存在"}), 404

@app.route('/base', methods=['GET'])
def base():
    return render_template('frontend/RyanHongd.github.io/1/index.html')

if __name__ == '__main__':
    app.run(debug=True)


