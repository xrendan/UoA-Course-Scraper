#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 22:03:31 2016

@author: brendan
"""

import sqlite3

conn = sqlite3.connect("course_listings.sqlite")
c = conn.cursor()
d = conn.cursor()
counter = 0 

def getReqs(test, string):
    if test in string:
        str = string
        #print(str)
        str = str.split(test, 1)[1]
        str = str.split(".", 1)[0].strip()
        str = str.replace(",", "")
        str = str.split(";", 1)[0].strip()
        
        
        new_str = str.split(" ")
        
        if len(new_str) <= 2:
            str = str.replace(" ", "")
            return [str]
        else:
            array = []
            subject = -1
            new_str = str.split(" or ")
            try:
                
                if str.split(" ") != new_str and int(str.split(" ", 1)[1]) < 1000:
                    subject = str.split(" ", 1)[0]
            except:
                pass
            for i in new_str:
                #print(new_str)
                #print(i)
                if "consent" in i:
                    array.append("consent")
                elif "Consent" in i:
                    array.append("consent")
                elif "permission" in i:
                    array.append("consent")
                elif "Permission" in i:
                    array.append("consent")
                elif "vary" in i:
                    array.append("vary")
                elif "Vary" in i:
                    array.append("vary")
                elif len(i.split()) == 2:
                    array.append(i.replace(" ", ""))
                elif i.split(" and ") != i:
                    test_str = i.split(" and ")
                    for j in test_str:
                        if len(j.split()) == 2:
                            array.append(j.replace(" ", ""))
                elif int(i) < 1000 and subject != -1:
                    array.append([subject, i].join())
                else:
                    array.append("error")
                    
            #print(new_str)
            #print()
            return array
    return []


c.execute("SELECT CourseNum, CourseDescription from courses")



test_cases = ["prerequisite:", "Prerequisite:","prerequisites:", "Prerequisites:", \
              "prerequisite ", "Prerequisite ","prerequisites ", "Prerequisites "]
for row in c:
    for i in test_cases:
        prereq = getReqs(i, row[1])
        if len(prereq) >= 1 and "error" not in prereq: 
            counter +=1
            for l in prereq:
                    d.execute("INSERT INTO prerequisites VALUES (?, ?)", (row[0], l))
                    print("success")
                
            
#        if "error" in prereq: 
#            #print(row[1].split(i, 1)[1])
#            counter +=1
#            print(prereq)


c.execute("SELECT CourseNum, CourseDescription from courses")
      
test_cases = ["corequisite:", "Corequisite:","corequisites:", "Corequisites:", \
              "corequisite ", "Corequisite ","corequisites ", "Corequisites ", \
              "co-requisite:", "Co-requisite:","co-requisites:", "Co-requisites:", \
              "co-requisite ", "Co-requisite ","co-requisites ", "Co-requisites "]
for row in c:
    for i in test_cases:
        prereq = getReqs(i, row[1])
        if len(prereq) >= 1 and "error" not in prereq: 
            #counter +=1
            for l in prereq:
                    d.execute("INSERT INTO corequisites VALUES (?, ?)", (row[0], l))
                    #print("success")
                
            
#        if "error" in prereq: 
#            print(row[1].split(i, 1)[1])
#            counter +=1
#            print(prereq)
    
  
            
print("counter ", end="")
print(counter)

conn.commit()
conn.close()