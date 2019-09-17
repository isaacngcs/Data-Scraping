# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:13:32 2019

@author: Isaac
"""

from Functions.yes_no_check import yes_no_check
from Classes.Project import Project

def new_project():
    
    name = input('Creating new project, enter project name: ')
    
    root = 'https://noc.com.sg/foodking/'
    print(f'Current rooturl: {root}')
    
    if yes_no_check('Change rooturl?'):
        root = get_valid_root()
        print(f'Rooturl changes to {root}')
    
    project = Project(name, root)
    project.add_prescraped(root)
    
    return project

def get_valid_root():
    
    import re
    valid = re.compile("\w+\.\w+")
    
    valid_root = False
    while not valid_root:
        root = input('Enter new rooturl: ')
        if valid.match(root):
            root = format_url(root)
            valid_root = True
        else:
            print(f'{root} is an invalid rooturl')
    
    return root

def format_url(url):
    
    if not url.startswith('http'):
        url = 'http://' + url
    if not url.endswith('/'):
        url = url + '/'
        
    return url