#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:59:36 2016

@author: brendan
"""

import sqlite3

sqlite_file = 'course_listings.sqlite'   
table_name = 'courses'
table_name1 = 'prerequisites'  # name of the table to be created
table_name2 = 'programs'  # name of the table to be created
table_name3 = 'corequisites'  # name of the table to be created

id_column = 'CourseNumber' # name of the PRIMARY KEY column
new_column0 = 'CourseURL'
new_column1 = 'CourseName'  # name of the new column
new_column2 = 'CourseDescription'  # name of the new column
new_column3 = 'Department'
new_column4 = 'Faculty'

new_column5 = 'Prerequisite'
new_column6 = 'Corequisite'

new_column7 = 'Program'
new_column8 = 'isTrad'
new_column9 = 'Term'
new_column10 = 'Department'



column_type = 'TEXT' # E.g., INTEGER, TEXT, NULL, REAL, BLOB
column_type1 = 'INTEGER'

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
        .format(tn=table_name1, cn=new_column5, ct=column_type))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=new_column7, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=new_column10, ct=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=new_column8, ct=column_type1))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=new_column9, ct=column_type1))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name3, cn=new_column6, ct=column_type))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()