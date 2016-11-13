#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:58:53 2016

@author: brendan
"""

import sqlite3

   
sqlite_file = 'course_listings.sqlite'    
table_name = 'courses'  # name of the table to be created
new_field = 'Course Number' # name of the column
field_type = 'TEXT'  # column data type

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn = table_name, nf = new_field, ft = field_type))

conn.commit()
conn.close()