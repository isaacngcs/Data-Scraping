# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:35:43 2019

@author: Isaac
"""

import os

def set_path(root): # Set additional parameters for subdirs, root + dir + dir
    
    path = os.getcwd()
    while os.path.basename(path) != root:
        path = os.path.normpath(os.path.join(os.getcwd(),'..'))
    return path