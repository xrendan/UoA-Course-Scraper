#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:21:30 2016

@author: brendan
"""

from bs4 import BeautifulSoup
import requests

r = requests.get("https://catalogue.ualberta.ca/Course/Subject?subjectCode=ANTHR")
soup = BeautifulSoup(r.text, "html.parser")
courses = soup.find_all("div", class_="claptrap-course")

for i in courses:
    print(i.find("span", class_="claptrap-course-number").string.strip())
    print(i.find("span", class_="claptrap-course-title").string.strip())
    print(i.find("p"))