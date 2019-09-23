# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:44:04 2019

@author: Isaac
"""

from Functions.list_projects import (folder_check, get_project_list,
                                     list_projects, project_choice,
                                     create_folder)

# List projects available
to_import = ''
print('Importing list of projects..\n')
if folder_check():
    project_list = get_project_list()
    list_projects(project_list)
    to_import = project_choice(project_list)
else:
    create_folder()
    
# Setting starting variables for sitecrawling
# Given a siteurl, this bot aims to crawl through the site
# and return all internal and external sites linked within
# in two sets respectively

from Functions.import_sites import import_confirmation, import_sites

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

from Functions.scrape_links import scrape_links, parameter_input
from Functions.yes_no_check import yes_no_check

if yes_no_check('Customise scraping parameters?'):
    max_iter, continuous_iter, iter_size = parameter_input()
    scrape_links(project, max_iter, continuous_iter, iter_size)
else:
    scrape_links(project)

# Sorting all site links alphabetically
project.sort_links()

from Functions.export_sites import export_confirmation, export_sites
from Functions.list_projects import project_check

if export_confirmation():
    name = project.get_name()
    if project_check(name):
        if yes_no_check('Overwrite existing files?'):
            export_sites(project)
        else:
            # Optional module - Change name and export
            pass
    else:
        create_folder(name)
        export_sites(project)
    pass