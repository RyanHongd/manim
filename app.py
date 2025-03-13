import os
from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
import subprocess



app = Flask(__name__)
CORS(app)  # 讓前端能夠存取這個 Flask 伺服器
VIDEO_PATH = "output_media/videos/1080p60/MainScene2.mp4"
# 執行 gpttest.py 並傳遞題目



@app.route('/generate', methods=['POST'])
def generate_video():
    data = request.json
    user_input = data.get("text", "")  # 取得前端輸入的數學問題

    if not user_input.strip():
        return jsonify({"error": "請輸入數學問題"}), 400

    

    try:
        result = subprocess.run(
            ["python", "manim/vid_process/system.py", f'"{user_input}"'],
            capture_output=True, text=True
        )

        if result.returncode != 0:
            return jsonify({"error": "system.py 執行失敗", "details": result.stderr}), 500

        # 檢查影片是否生成
        if not os.path.exists(VIDEO_PATH):
            return jsonify({"error": "影片未生成，可能 system.py 執行失敗"}), 500

    except Exception as e:
        return jsonify({"error": "執行 system.py 時發生錯誤", "details": str(e)}), 500



    # 檢查影片是否存在
    if os.path.exists(VIDEO_PATH):
        return jsonify({"message": "影片已生成", "video_url": f"http://127.0.0.1:5000/download"})
    else:
        return jsonify({"error": "影片生成失敗"}), 400

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


