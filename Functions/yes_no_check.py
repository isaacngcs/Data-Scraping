# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:45:00 2019

@author: Isaac
"""

def yes_no_check(question):
    while True:
        reply = input(question + ' (y/n): ').lower().strip()
        if reply == 'y':
            return True
        if reply == 'n':
            return False
        print('Invalid response, please input y or n.')