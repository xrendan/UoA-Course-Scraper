#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:21:30 2016

@author: brendan
"""

from bs4 import BeautifulSoup
import requests



#The following code scrapes The University of Alberta Course Catalogue and Prints all of the courses offered
soup_Faculties = BeautifulSoup(requests.get("https://catalogue.ualberta.ca/Course").text, "html.parser")

faculty_Links = soup_Faculties.find("table").find_all("a")

facultyCodes = []
facultyNames = []

for link in faculty_Links:
    facultyNames.append(link.string.strip())
    facultyCodes.append(link.attrs["href"].replace("/Course/Faculty?facultyCode=", ""))


for idx, faculty in enumerate(facultyCodes):
    r = requests.get("https://catalogue.ualberta.ca/Course/Faculty", params = {"facultyCode": faculty})
    soup_Subject = BeautifulSoup(r.text, "html.parser")
    subject_Rows = soup_Subject.find("table").find_all("tr")
    
    #print(facultyNames[idx])
    
    subjectNames = []
    subjectCodes = []
    for row in subject_Rows:
        #subject_Cols = subject_Rows.find("td")
        try:
            subjectNames.append(row.find_all("td")[1].string.strip())
            subjectCodes.append(row.find("a").attrs["href"].replace("/Course/Subject?subjectCode=", ""))
        except:
            pass
    #print(subjectCodes)


    for subject in subjectCodes:

            
        s = requests.get("https://catalogue.ualberta.ca/Course/Subject", params = {"subjectCode": subject})
        soup = BeautifulSoup(s.text, "html.parser")
        courses = soup.find_all("div", class_="claptrap-course")
        
        for i in courses:
            
            #course number
            print(i.find("span", class_="claptrap-course-number").string.strip())
            
            #course name
            print(i.find("span", class_="claptrap-course-title").string.strip())
            
            #Course Description
            try:
                print(i.find("p").contents[2].strip())
            except:
                print("No Description Available")
                