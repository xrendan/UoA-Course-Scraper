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
    print(soup_Department.prettify())
    departmentNames.append(soup_Department.find("h1").string.strip())
    
    traditional = soup_Department.find_all(class_="acalog-core", limit=2)
    for j, value in enumerate(traditional):
        
    

print(departmentNames)