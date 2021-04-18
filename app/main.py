from flask import Flask
from flask import render_template
from server.video.stream import video_stream

app = Flask(__name__,
            template_folder='gui/templates',
            static_folder='gui/static',
            static_url_path='/static')


@app.route('/')
def hud():
    return render_template('hud.html')


# https://towardsdatascience.com/video-streaming-in-web-browsers-with-opencv-flask-93a38846fe00
@app.route('/video')
def video():
    return video_stream()
