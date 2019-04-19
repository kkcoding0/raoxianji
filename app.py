from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import flash

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '123456'

from model import app

@app.route('/opcdata')
def index():
    return render_template('index.html')

@app.route('/login')
def logzhuan():
    return render_template('index0.html')

@app.route('/register')
def register():
    return render_template('index0.html')

if __name__ == '__main__':
    app.run(host='192.168.1.153',port=8000)