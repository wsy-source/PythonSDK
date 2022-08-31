from flask import Flask, render_template,make_response
from typing import Callable

app = Flask(__name__)


@app.get('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
