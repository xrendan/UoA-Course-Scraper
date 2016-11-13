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
    #print(l)
    secondwindow = tkinter.Tk()
    secondwindow.title("Plots")
    secondwindow.geometry("600x800")
    secondwindow.configure(background="SteelBlue1")
    
    w = tkinter.Frame(secondwindow)
    x = tkinter.Frame(secondwindow)
    w.pack()
    x.pack()
    
    courses = []
    for idx, j in enumerate(l):
        if j == 1:
            courses.append(n[idx])
    
            
    classes = []
    for idx, i in enumerate(courses):
        lbl0 = tkinter.Label(w, text = i, bg="SteelBlue1", font=('Helvetica',20))
        lbl0.pack()
#        lbl0 = tkinter.Label(w, text = "|", bg="SteelBlue1", font=('Helvetica',20))
#        lbl0.pack(side=tkinter.LEFT)
        print()
        print(i)
        c.execute('SELECT CourseNum FROM programs WHERE Program = ?', (i,))
        m = c.fetchall()
        t = []
        for p in m:
            t.append(p[0])
        classes.append(t)
        
        for i, val in enumerate(classes[idx]):
            btn = tkinter.Button(w, text = val, command = lambda index=i: description(val))
            btn.pack(side=tkinter.TOP)
    
    print(classes[0])
    
    secondwindow.mainloop()

    
def description(i):
 
    thirdwindow = tkinter.Tk()
    thirdwindow.title("Plots")
    thirdwindow.geometry("1500x800")
    thirdwindow.configure(background="green")
    
    lbl0 = tkinter.Label(thirdwindow, text = i, bg="SteelBlue1", font=('Helvetica',14))
    lbl0.pack()      
    

    print()
    print(i)
    c.execute('SELECT CourseDescription FROM courses WHERE CourseNum = ?', (i,))
    m = c.fetchall()
    print(m)
    t = []
    jim = []
    for p in m:
        t.append(p[0])
    jim.append(t)
    
    btn = tkinter.Label(thirdwindow, text = jim[0], font=('Helvetica',20))
    btn.pack(side=tkinter.TOP)


    
    thirdwindow.mainloop()   
    
    

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
window.mainloop()
