from flask import Flask, request, render_template, send_file
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload_video():
    uploaded_file = request.files['video']
    # Ensure 'temp' directory exists
    os.makedirs('temp', exist_ok=True)
    # Save the uploaded video to the 'temp' directory
    uploaded_file.save('temp/original_video.mp4')
    return 'Video uploaded successfully'



@app.route('/trim', methods=['POST'])
def trim_video():
    start_time = float(request.form['start_time'])
    end_time = float(request.form['end_time'])

    input_video_path = 'temp/original_video.mp4'
    output_video_path = 'temp/trimmed_video.mp4'

    ffmpeg_extract_subclip(input_video_path, start_time, end_time, targetname=output_video_path)

    return 'Video trimmed successfully'

@app.route('/download')
def download_video():
    trimmed_video_path = 'temp/trimmed_video.mp4'
    return send_file(trimmed_video_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
