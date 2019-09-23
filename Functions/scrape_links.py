# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:52:02 2019

@author: Isaac
"""

from Functions.yes_no_check import yes_no_check
from Functions.get_links_bs import get_links

def scrape_links(project, max_iter = 5, 
                 continuous_iter = False, iter_size = 100):
    
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
        
        # Split batch of links for iteration
        prescraped_links = list(project.get_prescraped())
        if len(prescraped_links) > iter_size:
            project.set_prescraped(set(prescraped_links[100:]))
            prescraped_links = prescraped_links[:100]
        
        # Setup iteration information
        num_links = len(prescraped_links)
        print(f'\n{num_links} links to scrape')
        link_num = 1
        
        # Iterate over each site
        for site in prescraped_links:
            
            print(f'\nIterating over {site}')
            print(f'Site {link_num}/{num_links}')
            
            (internal, external, 
             to_review, media) = get_links(site, project.get_root())
            project.add_external(external)
            project.add_to_review(to_review)
            project.add_media(media)
            
            # Skip to next site if no internal links
            if len(internal) == 0:
                link_num = link_num + 1
                continue
            # Check for new internal links and group them up
            new_links = new_links|internal
            link_num = link_num + 1
        
        new_unique_links = new_links.difference(project.get_internal())
        
        # Add new internal links found in this iteration
        # To the next iteration
        project.add_prescraped(new_unique_links)
        # To the internal sites set
        project.add_internal(new_unique_links)
        
        # End the iteration process if
        # 1. No new links are found
        # 2. Nothing left in prescraped list
        if not new_unique_links and not len(project.get_prescraped()):
            has_new_links = False
            print(f'No new links found in iteration {num_iter}.\n')
            break
        
        # Check new added links
        #print(f'\n New links from iteration {num_iter}... ')
        #for link in new_unique_links:
        #    print(link)
        print(f'{len(new_unique_links)} new links\n')
        print('\n')
        
        num_iter = num_iter + 1
        
        # Continue with next iteration or stop iterating
        if not continuous_iter and num_iter <= max_iter:
            if not yes_no_check(f'Continue with iteration {num_iter}?'):
                break
            
    print(f'{num_iter} iterations done.\n')

def parameter_input():
    
    max_iter = input('Input maximum number of scraping iterations: ')
    while not max_iter.isdigit() or int(max_iter) < 1:
        print('Please input a positive integer.')
        max_iter = input('Input maximum number of scraping iterations: ')
    
    continuous_iter = yes_no_check('Enable continuous iteration?')
    
    iter_size = input('Input maximum batch size of each iteration: ')
    while not max_iter.isdigit() or int(iter_size) < 1:
        print('Please input a positive integer.')
        iter_size = input('Input maximum batch size of each iteration: ')
    return int(max_iter), continuous_iter, int(iter_size)