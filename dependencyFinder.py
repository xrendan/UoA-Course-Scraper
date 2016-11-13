#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 22:03:31 2016

@author: brendan
"""

import sqlite3

conn = sqlite3.connect("course_listings.sqlite")
c = conn.cursor()
counter = 0 

c.execute("SELECT CourseNum, CourseDescription from courses")
#
#numRows = list(c)[0][0]

#for i in range(1, numRows):
    
for row in c:
    if "prerequisite." in row[1]:
        pass
    if "prerequisite:" in row[1]:
        str = row[1]
        str = str.split("prerequisite:", 1)[1]
        str = str.split(".", 1)[0].strip()
        str = str.replace(",", "")
        str = str.split(";", 1)[0].strip()
        
        
        new_str = str.split(" ")
        
        if len(new_str) <= 2:
            str = str.replace(" ", "")
            print(row[0])
            print(str)
            print()
            
            counter += 1
            
            
    if "Prerequisite:" in row[1]:
        str = row[1]
        str = str.split("Prerequisite:", 1)[1]
        str = str.split(".", 1)[0].strip()
        str = str.replace(",", "")
        str = str.split(";", 1)[0].strip()
        
        
        new_str = str.split(" ")
        
        if len(new_str) <= 2:
            str = str.replace(" ", "")
            print(row[0])
            print(str)
            print()
            
            counter += 1
    
            
    if "prerequisites:" in row[1]:
        str = row[1]
        str = str.split("prerequisites:", 1)[1]
        str = str.split(".", 1)[0].strip()
        str = str.replace(",", "")
        str = str.split(";", 1)[0].strip()
        
        
        new_str = str.split(" ")
        
        if len(new_str) <= 2:
            str = str.replace(" ", "")
            print(row[0])
            print(str)
            print()
            
            counter += 1
            
            
    if "Prerequisites:" in row[1]:
        str = row[1]
        str = str.split("Prerequisites:", 1)[1]
        str = str.split(".", 1)[0].strip()
        str = str.replace(",", "")
        str = str.split(";", 1)[0].strip()
        
        
        new_str = str.split(" ")
        
        if len(new_str) <= 2:
            str = str.replace(" ", "")
            print(row[0])
            print(str)
            print()
            
            counter += 1
        
        
 
print("counter: ", end="")
print(counter)