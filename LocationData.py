# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:44:04 2019

@author: Isaac
"""

# Add User-Agent parameter
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

import Project

# Find structure of website
siteurl = 'https://noc.com.sg/foodking/'

# Get location data from webpage
# Retrieve all links from a given webpage
# Separate links into internal and external links
def getdata(url):
    
    # Retrieve content from url
    page_link = url
    page_response = requests.get(page_link, headers=headers, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser",
                                 from_encoding="iso-8859-1")
    
    # Create sets for internal and external links
    internal = set([])
    external = set([])
    
    # Retrieve links and sorts them into internal and external links
    links = set([])
    for unsorted_link in page_content.findAll(
        'a', attrs={'href': re.compile("^http://")}):
        link = unsorted_link.get('href')
        if link.startswith(siteurl):
            internal.add(link)
        else:
            external.add(link)
            
    return internal, external

"""
Structure to extract page links:
"nav-previous" ... a href=url
"nav-next" ... a href=url

no nav-previous for first url
no nav-next for last url

Structure for data:

eg1...
p Ratings: 3 Stars, Food-King Good!

p SAN LAKSA STEAMBOAT

p 404 Telok Blangah Road, Singapore 098840

p Mon – Sun, 11AM to 2.30PM, 4.30PM to 11PM



p And here’s our Top 3 Picks of the Day!

p Nina’s pick – San Laksa Steamboat

p Sylvia’s pick –  San Laksa Steamboat

p Aiken’s pick – San Laksa Steamboat

eg2...
And here’s our Top Picks of the Day!

Sylvia’s pick – Australian Mango Sorbet

Ryan’s pick – Dark Chocolate

Aiken’s pick – Boysenberry, Acai and Coconut

Dee’s pick – Summer Berries Sorbet

*Use regex on 'Top Picks of the Day'

eg3...
Ratings: 3 Stars, Food-King Good!!

ONE FABER GROUP

"""

# Saving location data to csv file