# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 18:07:16 2019

@author: Isaac
"""

from Functions.yes_no_check import yes_no_check

name = ''
path = ''

# Function for saving links to files
def export_sites(project):
    
    import csv
    from Functions.set_path import set_path
    
    path = (set_path('Data Scraping') +
            '\Projects\\' + project.get_name() + '\\')
    
    print('\nSaving rooturl to rooturl.txt')
    with open(path + 'rooturl.txt', mode = 'w', encoding= 'utf-8') as txt_save:
        root = project.get_root()
        txt_save.write(root)
        print(f'Root url {root} saved.')
    
    print('\nSaving all internal links to internal_sites.csv')
    with open(path + 'internal_sites.csv', 
              mode = 'w', newline = '', encoding= 'utf-8') as csv_save:
        writer = csv.writer(csv_save)
        internal = project.get_internal()
        for site in internal:
            # csv.writer.writerow() expects a list of strings,
            # if a single string is given, it is treated as
            # a list of one-character strings instead
            # therefore [site] is required
            writer.writerow([site])
    print(f'{len(internal)} internal sites saved.')

    print('\nSaving prescraped links to prescraped_sites.csv')
    with open(path + 'prescraped_sites.csv', 
              mode = 'w', newline = '', encoding= 'utf-8') as csv_save:
        writer = csv.writer(csv_save)
        prescraped = project.get_prescraped()
        for site in prescraped:
            writer.writerow([site])
    print(f'{len(prescraped)} prescraped sites saved.')

    print('\nSaving all external links to external_sites.csv')
    with open(path + 'external_sites.csv', 
              mode = 'w', newline = '', encoding= 'utf-8') as csv_save:
        writer = csv.writer(csv_save)
        external = project.get_external()
        for site in external:
            writer.writerow([site])
    print(f'{len(external)} external sites saved.')
    
    print('\nSaving all to_review links to to_review_sites.csv')
    with open(path + 'to_review_sites.csv', 
              mode = 'w', newline = '', encoding= 'utf-8') as csv_save:
        writer = csv.writer(csv_save)
        to_review = project.get_to_review()
        for site in to_review:
            writer.writerow([site])
    print(f'{len(to_review)} to_review sites saved.')
    
    print('\nSaving all media links to media_sites.csv')
    with open(path + 'media_sites.csv', 
              mode = 'w', newline = '', encoding= 'utf-8') as csv_save:
        writer = csv.writer(csv_save)
        media = project.get_media()
        for site in media:
            writer.writerow([site])
    print(f'{len(media)} media sites saved.')
    
    print('\n')
    
# Check if internal_sites.csv, prescraped_sites.csv,
# and external_sites.csv files exist

# If it exists, prompt if user wants to overwrite files
def export_confirmation():
    
    if yes_no_check('Export to file?'):
        print('\nExporting sites...')
        return True
    else:
        print('Sites not exported.')
        return False