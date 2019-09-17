# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:52:02 2019

@author: Isaac
"""

from Functions.yes_no_check import yes_no_check
from Classes.Project import Project
from Functions.get_links import get_links

def scrape_links(project, max_iter = 5, continuous_iter = False):
    
    # Iterate through siteurl, returning all internal and external links
    # All links are check for duplicates within and against the sets
    # New internal links are grouped and all internal links will be
    # added to the next iteration
    
    # Start iteration
    num_iter = 1
    max_iter = max_iter
    continuous_iter = continuous_iter
    has_new_links = True
    while has_new_links and num_iter <= max_iter:
        
        # Initialise set for new links
        new_links = set([])
        print('Iteration:', num_iter)
        
        # Setup iteration information
        num_links = len(project.get_prescraped())
        print(f'\n{num_links} links to scrape')
        link_num = 1
        
        # Iterate over each site
        for site in project.get_prescraped():
            
            print(f'\nIterating over {site}')
            print(f'Site {link_num}/{num_links}')
            
            new_internal, new_external = get_links(site, project.get_root())
            project.add_external(new_external)
            
            # Skip to next site if no internal links
            if len(new_internal) == 0:
                link_num = link_num + 1
                continue
            # Check for new internal links and group them up
            new_links = new_links|new_internal
            link_num = link_num + 1
        
        new_unique_links = new_links.difference(project.get_internal())
        
        # End the iteration process if no new links are found
        if not new_unique_links:
            has_new_links = False
            print(f'No new links found in iteration {num_iter}.\n')
            break
        
        # Add new internal links found in this iteration
        # To the next iteration
        project.set_prescraped(new_unique_links)
        # To the internal sites set
        project.add_internal(new_unique_links)
        
        # Check new added links
        print(f'\n New links from iteration {num_iter}... ')
        print(f'{len(new_unique_links)} new links\n')
        for link in new_unique_links:
            print(link)
        print('\n')
        
        num_iter = num_iter + 1
        
        # Continue with next iteration or stop iterating
        if not continuous_iter and num_iter <= max_iter:
            if yes_no_check(f'Continue with iteration {num_iter}?'):
                break
            
    print(f'{num_iter} iterations done.\n')
