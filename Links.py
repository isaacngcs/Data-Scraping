# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:44:04 2019

@author: Isaac
"""

from Classes.Project import Project
from Functions.list_projects import folder_check, list_projects

# List projects available
to_import = ''
print('Importing list of projects..\n')
if folder_check():
    projects = list_projects()
    for index in range(1, len(projects) + 1):
        print(f'{index}: {projects[index - 1]}')
    print(f'{len(projects)} projects found.')
    
    if input('Import existing project? (y/n) ')  == 'y':
        index = int(input('Project to import (Enter index): '))
        if index in range(1, len(projects) + 1):
            to_import = projects[index - 1]
            print(f'{projects[index - 1]} selected.')
        else:
            print('No project selected.')

# Setting starting variables for sitecrawling
# Given a siteurl, this bot aims to crawl through the site
# and return all internal and external sites linked within
# in two sets respectively

from Functions.import_sites import import_check

project = None

if to_import:
    project = import_check(to_import)
    print(f'Project {to_import} imported.')

# Set the siteurl for crawling
root = 'https://noc.com.sg/foodking/'
if not project:
    name = input('Creating new project, enter project name: ')
    project = Project(name, root)
    project.add_prescraped(root)

# Scrape through all prescraped links in project
# Set maximum number of iterations (Default: 5)
# Choose whether to pause between iterations (Default: False)

from Functions.scrape_links import scrape_links

scrape_links(project)

# Sorting all site links alphabetically
project.sort_links()

from Functions.export_sites import export_sites, export_check
