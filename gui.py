#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 09:31:15 2016

@author: brendan
"""

import tkinter
import sqlite3

sqlite_file = 'course_listings.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()



c.execute("SELECT DISTINCT program FROM programs")
m = c.fetchall()
n = []
l = []
for i in m:
    n.append(i[0])
    l.append(0)


def toggle(i):
    global l
    if l[i]:
        l[i] = 0
        
    else:
        l[i] = 1
    print(l)
    

col = "indian red"
window = tkinter.Tk()
window.title("Sketch GUI Building Last Minute")
window.geometry("600x800")
window.configure(background=col)

lbl = tkinter.Label(window, text ="Engineering Program Comparer", bg=col, font=('Helvetica',30))
lbl.pack()

for i, val in enumerate(n):
    btn = tkinter.Button(window, text = val, command = lambda index=i: toggle(index))
    btn.pack(side=tkinter.TOP)
# Code to add widgets will go here...
r = window.mainloop()
