# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:44:04 2019

@author: Isaac
"""

from Functions.list_projects import (folder_check, get_project_list,
                                     list_projects, project_choice)

# List projects available
to_import = ''
print('Importing list of projects..\n')
if folder_check():
    project_list = get_project_list()
    list_projects(project_list)
    to_import = project_choice(project_list)
    
# Setting starting variables for sitecrawling
# Given a siteurl, this bot aims to crawl through the site
# and return all internal and external sites linked within
# in two sets respectively

from Functions.import_sites import import_confirmation, import_sites
from Classes.Project import Project

project = None

if to_import and import_confirmation():
    project = import_sites(to_import)
    print(f'Project {to_import} imported.')

# Create new project if no project imported
if not project:
    from Functions.new_project import new_project
    project = new_project()
    
# Scrape through all prescraped links in project
# Set maximum number of iterations (Default: 5)
# Choose whether to pause between iterations (Default: False)

from Functions.scrape_links import scrape_links

scrape_links(project)

# Sorting all site links alphabetically
project.sort_links()

from Functions.export_sites import export_confirmation, export_sites

if export_confirmation():
    