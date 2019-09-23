# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:27:02 2019

@author: Isaac
"""

# Search for Projects folder in current directory
# If found, list all Projects/subdirectories

import os
from Functions.yes_no_check import yes_no_check
from Functions.set_path import set_path

def folder_check():
    
    projects_path = set_path('Data Scraping') + '\Projects'
    if os.path.exists(projects_path):
        print('Projects folder verified.')
        return True
    else:
        print('Projects folder not found.')
        return False
    
def project_check(name):
    
    if name in get_project_list():
        print(f'{name} folder exist.')
        return True
    else:
        print(f'{name} folder does not exist.')
        return False

def get_project_list():
    
    projects_path = set_path('Data Scraping') + '\Projects'
    projects = next(os.walk(projects_path))[1]
    return projects

def list_projects(project_list):
    
    for index in range(1, len(project_list) + 1):
        print(f'{index}: {project_list[index - 1]}')
    print(f'{len(project_list)} projects found.')

def project_choice(project_list):
    
    if yes_no_check('Import existing project?'):
        index = int(input('Project to import (Enter index): '))
        if index in range(1, len(project_list) + 1):
            print(f'{project_list[index - 1]} selected.')
            return project_list[index - 1]
    print('No project selected.')
    return ''

def create_folder(folder = 'Projects'):
    
    path = set_path('Data Scraping') + '\Projects'
    
    # Create projects folder if it does not exist
    if folder == 'Projects':
        os.mkdir(path)
        print('Projects folder created.')
    else:
        os.mkdir(path + '\\' + folder)
        print(f'Project folder {folder} created.')