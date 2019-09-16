# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 18:07:02 2019

@author: Isaac
"""

import csv
import os
from Classes.Project import Project

# Initialise sets
root = ''
internal = set([])
external = set([])
prescraped = set([])

# Function to import previous site-link scraping project
def import_sites(project):
    
    path = os.getcwd() + '\Projects\\' + project + '\\'
    
    # Import rooturl
    with open(path + 'rooturl.txt', mode = 'r') as txt_load:
        root = txt_load.read()
        print(f'Root url {root} imported')
    
    # Import internal_sites
    with open(path + 'internal_sites.csv', mode = 'r') as csv_load:
        reader = csv.reader(csv_load)
        for site in reader:
            internal.add(site[0])
        print(f'{len(internal)} internal sites imported')
            
    # Import prescraped_sites (Resets prescraped)
    with open(path + 'prescraped_sites.csv', mode = 'r') as csv_load:
        reader = csv.reader(csv_load)
        for site in reader:
            prescraped.add(site[0])
        print(f'{len(prescraped)} prescraped sites imported')
    
    # Import external_sites
    with open(path + 'external_sites.csv', mode = 'r') as csv_load:
        reader = csv.reader(csv_load)
        for site in reader:
            external.add(site[0])
        print(f'{len(external)} external sites imported')

# Check if user wants to import information
def import_check(project):

    if input('Import previous progress? (y/n) ') != 'n':
        print('\nImporting sites...')
        import_sites(project)
    else:
        print('\nSites not imported')
    
    return Project(project, root, internal, prescraped, external)
