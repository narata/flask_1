# -*- coding: utf-8 -*-
# @Time     : 2018/4/16 14:28
# @Author   : Narata
# @File     : demo.py
# @Software : PyCharm

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/hello/')
def hello_world():
    return render_template('hello.html', args=request.args.get('args', '1'))


if __name__ == '__main__':
    app.run(debug=True)
