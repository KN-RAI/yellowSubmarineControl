from flask import Flask
from flask import render_template
app = Flask(__name__,
            template_folder='gui/templates',
            static_folder='gui/static',
            static_url_path='/static')


@app.route('/')
def hello_world():
    return render_template('hud.html')
