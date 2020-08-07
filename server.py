from flask import Flask
from flask import render_template

app = Flask(__name__, 
            static_url_path='', 
            static_folder='./static',
            template_folder='./templates')
print(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/<page_name>.html')
def hello_world(page_name = None):
    return render_template(f'{page_name}.html')

