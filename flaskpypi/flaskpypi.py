#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Yep"


@app.route('/simple')
def simple():
    return "simple"


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
