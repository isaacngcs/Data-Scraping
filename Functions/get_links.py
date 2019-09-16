# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:25:37 2019

@author: Isaac
"""

from bs4 import BeautifulSoup
import requests
import re

# Add User-Agent parameter
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

# Retrieve all links from a given webpage
# Separate links into internal and external links
def get_links(url, siteurl):
    
    # Retrieve content from url
    page_link = url
    page_response = requests.get(page_link, headers=headers, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser",
                                 from_encoding="iso-8859-1")
    
    # Create sets for internal and external links
    internal = set([])
    external = set([])
    
    # Retrieve links and sorts them into internal and external links
    for unsorted_link in page_content.findAll(
        'a', attrs={'href': re.compile("^http")}):
        link = unsorted_link.get('href')
        if link.startswith(siteurl):
            internal.add(link)
        else:
            external.add(link)
            
    return internal, external
