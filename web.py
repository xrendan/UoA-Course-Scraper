#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 08:47:43 2016

@author: brendan
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form.getlist('hello'))

    return '''<form method="post">
<input type="checkbox" name="hello" value="world" checked>
<input type="checkbox" name="hello" value="davidism" checked>
<input type="submit">
</form>'''

app.run()