import numpy as np
import random
from flask import Flask, render_template

name = 'server_ai'
app = Flask(name)


@app.route("/")
def hello_world():
    return render_template('home.html')


if __name__ == '__main__':
    port = 5000 + 1
    app.run(use_reloader=False, debug=True, port=port)