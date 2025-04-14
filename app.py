import os
from flask import Flask, request, jsonify, send_file, render_template, redirect, url_for
from flask_cors import CORS
import subprocess
import shutil

def move_video_to_static(source_path, target_folder='static\\videos'):
    os.makedirs(target_folder, exist_ok=True)
    filename = os.path.basename(source_path)
    target_path = os.path.join(target_folder, filename)
    shutil.move(source_path, target_path)
    print(f"已移動影片到：{target_path}")
    return filename

app = Flask(__name__)
CORS(app)  # 讓前端能夠存取這個 Flask 伺服器
VIDEO_PATH = "manim\\output_media\\videos\\1080p60\\MainScene2.mp4"
# 執行 gpttest.py 並傳遞題目

@app.route('/base', methods=['GET'])
def base():
    return render_template('index.html') 

@app.route('/generate', methods=['POST'])
def generate_video():
    data = request.json
    user_input = data.get("text", "")  # 取得前端輸入的數學問題

    if not user_input.strip():
        return jsonify({"error": "請輸入數學問題"}), 400

    

    try:
        print("1")
        result = subprocess.run(
            ["python", "vid_process\\system.py", user_input],  # 不要手動加引號
            capture_output=True, text=True
        )
        print("=== 執行 system.py 的 stdout ===")
        print(result.stdout)

        if result.returncode != 0:
            print(result.stderr)
            return jsonify({"error": "system.py 執行失敗", "details": result.stderr}), 300

        # 檢查影片是否生成
        if not os.path.exists(VIDEO_PATH):
            
            return jsonify({"error": "影片未生成，可能 system.py 執行失敗"}), 600

    except Exception as e:
        return jsonify({"error": "執行 system.py 時發生錯誤", "details": str(e)}), 700



    # 檢查影片是否存在
    if os.path.exists(VIDEO_PATH):
        filename = move_video_to_static(VIDEO_PATH)
        print("success")
        return jsonify({
            "success": True,
            "video_url": url_for('show_video', filename=filename)
        })
    else:
        return jsonify({"error": "影片生成失敗"}), 400

@app.route('/download', methods=['GET'])
def download_video():
    if os.path.exists(VIDEO_PATH):
        return send_file(VIDEO_PATH, as_attachment=True)
    else:
        return jsonify({"error": "影片不存在"}), 404

@app.route('/video/<filename>')
def show_video(filename):
    print(filename)
    return render_template('video.html', video_filename=f'videos/{filename}')

if __name__ == '__main__':
    app.run(debug=True)


