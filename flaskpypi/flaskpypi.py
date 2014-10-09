#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import xml.etree.ElementTree as ET
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

class Download:
    def __init__(self):
        self.link = ''
        self.title = ''


@app.route('/')
def main():
    return "Yep"


@app.route('/simple')
@app.route('/simple/')
def simple():
    return '<html><body><a href="/simple/flaskpypi">flaskpypi</a></body></html>'


@app.route('/simple/<app>')
@app.route('/simple/<app_>/')
def simple_package(app_):
    dirname = '/home/wayne/programming/flaskpypi/dist/'+app_
    if not os.path.isdir(dirname):
        pypiurl = 'https://pypi.python.org/simple/'
        r = requests.get(pypiurl+app_+'/')
        doc = ET.fromstring(r.text)
        os.mkdir(dirname)
        filenames = (a.attrib['href'] for a in doc.iter('a'))
        filenames = []
        for link in (a.attrib['href'] for a in doc.iter('a')):
            link = link.lstrip('./')
            r = requests.get(pypiurl+'../'+link)
            filename = link[1+link.rfind('/'):link.rfind('#')]
            filenames.append(filename)
            with open(os.path.join(dirname, filename), 'wb') as f:
                f.write(r.content)

    downloads = []
    app.logger.debug(os.listdir(dirname))
    for path in os.listdir(dirname):
        download = Download()
        download.link = '/simple/download/'+app_+'/'+path
        download.title = path[:path.rfind('#')]
        downloads.append(download)
        app.logger.debug(path)
         
    return render_template('simple.html',
                           package=app_,
                           downloads=sorted(downloads, key=lambda x: x.title))


@app.route('/simple/download/<package>/<version>')
def simple_download(package, version):
    dirname = os.path.join('/home/wayne/programming/flaskpypi/dist', package)
    return send_from_directory(dirname, version, as_attachment=True)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
