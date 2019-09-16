# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:27:02 2019

@author: Isaac
"""

# Search for Projects folder in current directory
# If found, list all Projects/subdirectories

import os

def folder_check():
    projects_path = os.getcwd() + '\Projects'
    if os.path.exists(projects_path):
        print('Projects folder verified.')
        return True
    else:
        print('Projects folder does not exist.')
        return False

def list_projects():
    projects_path = os.getcwd() + '\Projects'
    projects = next(os.walk(projects_path))[1]
    return projects
