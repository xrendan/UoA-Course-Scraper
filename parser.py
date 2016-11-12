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
print(soup.get_text())