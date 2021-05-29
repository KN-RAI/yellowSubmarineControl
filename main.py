from flask import Flask, Response
from flask import render_template
from camera_pi import Camera

app = Flask(__name__,
            template_folder='gui/templates',
            static_folder='gui/static',
            static_url_path='/static')

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('hud.html')
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)