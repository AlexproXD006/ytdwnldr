from flask import Flask, request, send_file, jsonify
from yt_dlp import YoutubeDL
import uuid
import os

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'Falta la URL'}), 400

    filename = f"/tmp/{uuid.uuid4()}.mp4"

    ydl_opts = {
        'format': 'bestvideo[height<=1440][fps<=60]+bestaudio/best[height<=1440][fps<=60]',
        'outtmpl': filename,
        'merge_output_format': 'mp4'
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return send_file(filename, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except:
                pass

if __name__ == '__main__':
    app.run()
