# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:27:02 2019

@author: Isaac
"""

# Search for Projects folder in current directory
# If found, list all Projects/subdirectories

import os
from Functions.yes_no_check import yes_no_check

def folder_check():
    projects_path = os.getcwd() + '\Projects'
    if os.path.exists(projects_path):
        print('Projects folder verified.')
        return True
    else:
        print('Projects folder not found.')
        return False

def get_project_list():
    projects_path = os.getcwd() + '\Projects'
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