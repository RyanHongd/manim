import os
from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
import subprocess



app = Flask(__name__)
CORS(app)  # 讓前端能夠存取這個 Flask 伺服器
VIDEO_PATH = "output_media/videos/1080p60/MainScene2.mp4"



@app.route('/generate', methods=['POST'])
def generate_video():
    data = request.json
    user_input = data.get("text", "")  # 取得前端輸入的數學問題

    if not user_input.strip():
        return jsonify({"error": "請輸入數學問題"}), 400

    # 執行 gpttest.py 並傳遞題目
    try:
        result = subprocess.run(
            ["python", "manim/vid_process/system.py", f'"{user_input}"'],
            capture_output=True, text=True, check=True
        )
        print("system.py 輸出:", result.stdout)
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "生成影片失敗", "details": e.stderr}), 600

    # 檢查影片是否存在
    if os.path.exists(VIDEO_PATH):
        return jsonify({"message": "影片已生成", "video_url": f"http://127.0.0.1:5000/download"})
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
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True)


