#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 09:31:15 2016

@author: brendan
"""

from tkinter import *
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
