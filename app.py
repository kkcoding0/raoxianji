from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

from model import app
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='192.168.1.153',port=8000)