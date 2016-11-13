#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:59:36 2016

@author: brendan
"""

import sqlite3

sqlite_file = 'course_listings.sqlite'   
table_name = 'courses'
id_column = 'CourseNumber' # name of the PRIMARY KEY column
new_column0 = 'CourseURL'
new_column1 = 'CourseName'  # name of the new column
new_column2 = 'CourseDescription'  # name of the new column
new_column3 = 'Department'
new_column4 = 'Faculty'


new_column5 = 'PreReq1'
new_column6 = 'PreReq2'
new_column7 = 'PreReq3'
new_column8 = 'PreReq4'
new_column9 = 'PreReq5'

new_column10 = 'CoReq1'
new_column11 = 'CoReq2'
new_column12 = 'CoReq3'
new_column13 = 'CoReq4'
new_column14 = 'CoReq5'

new_column15 = 'Conflict1'
new_column16 = 'Conflict2'
new_column17 = 'Conflict3'
new_column18 = 'Conflict4'
new_column19 = 'Conflict5'



column_type = 'TEXT' # E.g., INTEGER, TEXT, NULL, REAL, BLOB

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column0, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column1, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column2, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column3, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column4, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column5, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column6, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column7, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column8, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column9, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column10, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column11, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column12, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column13, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column14, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column15, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column16, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column17, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column18, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column19, ct=column_type))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()