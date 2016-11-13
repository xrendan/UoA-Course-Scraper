#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 06:42:57 2016

@author: brendan
"""

from bs4 import BeautifulSoup
import requests
import sqlite3

sqlite_file = 'course_listings.sqlite'   
table_name = 'programs'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
counter = 0


departmentsNums = [3149, 3211, 3159, 3199, 3188, 3164, 3157, 3151, 3040]
departmentNames = []

for i, val in enumerate(departmentsNums):
    soup_Department = BeautifulSoup(requests.get("http://calendar.ualberta.ca/preview_program.php", \
                                    params = {"poid" : val}).text, "html.parser")
    departmentNames.append(soup_Department.find("h1").string.strip())
    
    traditional = soup_Department.find_all(class_="acalog-core", limit=2)
    for j, value in enumerate(traditional):
        links = value.find_all("a", href=True)
        

        for k in links:
            link = k.attrs["href"].replace("preview_program.php?catoid=6&poid=", "")
            #print(link)
            soup_Program = BeautifulSoup(requests.get("http://calendar.ualberta.ca/preview_program.php", \
                                                      params = {"poid" : link}).text, "html.parser")
            ProgramName = soup_Program.find("h1").string.replace("(ENG)", "").replace("[Engineering]", "").replace("[Education]", "").strip()
            courses = soup_Program.find_all(class_ = "acalog-course")
            for l in courses:
                classes = l.find_all("a")
                for n in classes:
                    lectures = n.string.split(" - ")[0].replace(" ", "")
#                    print(lectures, end=" ")
#                    print(ProgramName, end=" ")
#                    print(departmentNames[i], end=" ")
                    if j == 0:
                        isTrad = 1
                    else:
                        isTrad = 0
                c.execute("INSERT INTO programs VALUES (?, ?, ?, ?)", (lectures, ProgramName, departmentNames[i], isTrad))
        print()


conn.commit()
conn.close()