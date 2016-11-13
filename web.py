#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 08:47:43 2016

@author: brendan
"""

from flask import Flask, request
import sqlite3

sqlite_file = 'course_listings.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("SELECT DISTINCT program FROM programs")
m = c.fetchall()
n = []
for i in m:
    n.append(i[0])
print(n)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'], title='Index')
def index():
    if request.method == 'POST':
        print(request.form.getlist('hello'))
        print(request.form.getlist("hell"))

    return '''<form method="post">
    
<input type="checkbox" name="hello" value="{a}" checked> Co-op
</br>
<input type="checkbox" name="hello" value="{}" checked>
</br>

<input type="submit">
</form>'''

app.run()