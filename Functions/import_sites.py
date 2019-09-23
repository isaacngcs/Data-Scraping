# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 18:07:02 2019

@author: Isaac
"""

import csv
from Functions.yes_no_check import yes_no_check
from Functions.set_path import set_path
from Classes.Project import Project

# Initialise sets
root = ''
internal = set([])
external = set([])
prescraped = set([])
to_review = set([])
media = set([])

# Function to import previous site-link scraping project
def import_sites(project_name):
    
    path = set_path('Data Scraping') + '\Projects\\' + project_name + '\\'
    
    # Import rooturl
    try:
        with open(path + 'rooturl.txt', mode = 'r') as txt_load:
            root = txt_load.read()
            print(f'Root url {root} imported')
    except FileNotFoundError:
        print('rooturl.txt not found.')
    
    # Import internal_sites
    try:
        with open(path + 'internal_sites.csv', mode = 'r') as csv_load:
            reader = csv.reader(csv_load)
            for site in reader:
                internal.add(site[0])
            print(f'{len(internal)} internal sites imported')
    except FileNotFoundError:
        print('internal_sites.csv not found.')
            
    # Import prescraped_sites (Resets prescraped)
    try:
        with open(path + 'prescraped_sites.csv', mode = 'r') as csv_load:
            reader = csv.reader(csv_load)
            for site in reader:
                prescraped.add(site[0])
            print(f'{len(prescraped)} prescraped sites imported')
    except FileNotFoundError:
        print('prescraped_sites.csv not found.')
    
    # Import external_sites
    try:
        with open(path + 'external_sites.csv', mode = 'r') as csv_load:
            reader = csv.reader(csv_load)
            for site in reader:
                external.add(site[0])
            print(f'{len(external)} external sites imported')
    except FileNotFoundError:
        print('external_sites.csv not found.')
    
    # Import to_review_sites
    try:
        with open(path + 'to_review_sites.csv', mode = 'r') as csv_load:
            reader = csv.reader(csv_load)
            for site in reader:
                to_review.add(site[0])
            print(f'{len(to_review)} to_review sites imported')
    except FileNotFoundError:
        print('to_review_sites.csv not found.')
    
    # Import media_sites
    try:
        with open(path + 'media_sites.csv', mode = 'r') as csv_load:
            reader = csv.reader(csv_load)
            for site in reader:
                media.add(site[0])
            print(f'{len(media)} media sites imported')
    except FileNotFoundError:
        print('media_sites.csv not found.')
    
    return Project(project_name, root, internal, prescraped, 
                   external, to_review, media)

# Check if user wants to import information
def import_confirmation():

    if yes_no_check('Import previous progress?'):
        print('\nImporting sites...')
        return True
    else:
        print('\nSites not imported')
        return False
    