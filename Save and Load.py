# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:44:04 2019

@author: Isaac
"""

# Objective: Saving to and Loading from a csv file
# 
# Two methods are used to obtain the objective,
#     Python csv library and Pandas
# 
# For each method, two different types of data will be used,
#     List data and Dictionary data

#%%
# Creating two different types of data
# Data type 1: List data
# To include index, number, string, boolean, date
import random
import datetime
rows = 10
index = 1
data = []
for i in range(rows):
    data.append([index, random.randint(1, 1000),
                'string' + str(index), (i%2) == 0,
                datetime.date(year = 2018, month = 1, day = 1) +
                datetime.timedelta(days = index)])
    index = index + 1
print(data)

#%%
# Creating two different types of data
# Data type 2: Dictionary data
# To include index, number, string, boolean, date
rows = 10
index = 1
data2 = {}
for i in range(rows):
    data2[index] = {'number': random.randint(1, 1000),
                    'string': 'string' + str(index),
                    'boolean':(i%2) == 0,
                    'date': datetime.date(year = 2018,
                                          month = 1,
                                          day = 1) +
                    datetime.timedelta(days = index)}
    index = index + 1
print(data2)

#%%
# Saving to and Loading from a csv file
# Using Python csv library
# List data
import csv

with open('test_file_1a.csv', mode = 'w', newline = '') as csv_save:
    writer = csv.writer(csv_save)
    for row in data:
        writer.writerow(row)
        
# newline = '' requried to prevent blank lines in between rows

#%%
# Loading from saved csv file
# Using Python csv library
with open('test_file_1a.csv', mode = 'r') as csv_load:
    reader = csv.reader(csv_load)
    for row in reader:
        print(row)

#%%
# Saving to and Loading from a csv file
# Using Python csv library
# Dictionary data
with open('test_file_1b.csv', mode = 'w', newline = '') as csv_save:
    fieldnames = ['index', 'number', 'string', 'boolean', 'date']
    writer = csv.DictWriter(csv_save, fieldnames = fieldnames)
    writer.writeheader()
    rows = len(data2)
    for row in range(1, rows+1):

        rowdata = data2[row]
        writer.writerow({'index': row,
                         'number': rowdata['number'],
                         'string': rowdata['string'],
                         'boolean': rowdata['boolean'],
                         'date': rowdata['date']})

#%%
# Loading from saved csv file
# Using Python csv library
with open('test_file_1b.csv', mode = 'r') as csv_load:
    reader = csv.DictReader(csv_load)
    is_header = True
    fieldnames = []
    for row in reader:
        if is_header:
            for element in row:
                fieldnames.append(element)
            print(fieldnames)
            is_header = False
        rowdata = []
        for field in fieldnames:
            rowdata.append(row[field])
        print(rowdata)

#%%
# Saving to and Loading from a csv file
# Using Pandas
# List data
import pandas as pd
df = pd.DataFrame(data,
                  columns = ['index', 'number',
                             'string', 'boolean',
                             'date'])
df.set_index('index', inplace = True)
df.to_csv('test_file_2a.csv')

#%%
# Loading from saved csv file
# Using Pandas
df = pd.read_csv('test_file_2a.csv',
                 index_col = 'index',
                 parse_dates = ['date'],
                 header = 0)
print(df)

#%%
# Saving to and Loading from a csv file
# Using Pandas
# Dictionary data
df = pd.DataFrame(data2).T
df.reset_index(level=0, inplace=False)
df.index.name = 'index'
columns = ['number', 'string', 'boolean', 'date']
df = df[columns]
df.to_csv('test_file_2b.csv')

#%%
# Loading from saved csv file
# Using Pandas
df = pd.read_csv('test_file_2b.csv',
                 index_col = 'index',
                 parse_dates = ['date'],
                 header = 0)
print(df)

# Objective: Saving to and Loading from a text file,
# Import data from .txt, .csv, Excel, Stata, SAS, Matlab, SQLite PostgreSQL
# 
# methods are used to obtain the objective,
#     
# For each method, two different types of data will be used,
#     List data and Dictionary data