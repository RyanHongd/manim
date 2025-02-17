from flask import Flask, request, jsonify, send_file
import subprocess

app = Flask(__name__)

@app.route('/generate_video', methods=['POST'])
def generate_video():
    data = request.json
    question = data.get("question")

    # 執行你的影片生成程式 (假設產生 output.mp4)
    subprocess.run(["python", "main.py", question])

    return send_file("MainScene2.mp4", as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

