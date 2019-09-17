# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 18:07:16 2019

@author: Isaac
"""

from Functions.yes_no_check import yes_no_check
from Classes.Project import Project

# Function for saving links to files
def export_sites(project):
    print('\nSaving all internal links to internal_sites.csv')
    import csv
    with open('internal_sites.csv', mode = 'w', newline = '') as csv_save:
        writer = csv.writer(csv_save)
        for site in sites:
            # csv.writer.writerow() expects a list of strings,
            # if a single string is given, it is treated as
            # a list of one-character strings instead
            # therefore [site] is required
            writer.writerow([site])
    print(f'{len(sites)} internal sites saved.')

    print('\nSaving prescraped links to prescraped_sites.csv')
    with open('prescraped_sites.csv', mode = 'w', newline = '') as csv_save:
        writer = csv.writer(csv_save)
        for site in links_to_iter:
            writer.writerow([site])
    print(f'{len(links_to_iter)} prescraped sites saved.')

    print('\nSaving all external links to external_sites.csv')
    with open('external_sites.csv', mode = 'w', newline = '') as csv_save:
        writer = csv.writer(csv_save)
        for site in external_sites:
            writer.writerow([site])
    print(f'{len(external_sites)} external sites saved.')
    
    print('\n')
    
# Check if internal_sites.csv, prescraped_sites.csv,
# and external_sites.csv files exist

# If it exists, prompt if user wants to overwrite files
import pathlib

def export_confirmation(project):
    
    # *Confirm export
    # export_confirmation()
    # *Check if folder exist (y/n)
    # get_project_list()
    # *(y) Confirm overwrite (y/n)
    # *(yy) Export sites
    # export_sites()
    # *(n) Confirm create new folder (y/n)
    # create_new_folder() TODO
    # *(ny) Create new folder
    # *(ny) Export sites
    # export_sites()

    path = pathlib.Path('internal_sites.csv')
    
    if path.is_file():
        if yes_no_check('Site files exist. Overwrite files?'):
            print('Sites not exported.')
        else:
            export_sites()
            print('Sites exported')
    else:
        export_sites()
        print('Sites exported.')
