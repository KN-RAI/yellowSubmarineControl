from flask import Response
from server.video.camera import camera_read


def video_stream():
    return Response(camera_read(), mimetype='multipart/x-mixed-replace; boundary=frame')
