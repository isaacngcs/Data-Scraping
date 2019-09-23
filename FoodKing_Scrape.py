# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:44:04 2019

@author: Isaac
"""

# To scrape FoodKing site for data

"""
Structure to extract page links:
"nav-previous" ... a href=url
"nav-next" ... a href=url

no nav-previous for first url
no nav-next for last url

*Possibly used to index which webpages came first

Class:
    FoodKing Project (sub-class of Project)
Attributes:
    ...

Class:
    Page
Attributes:
    str(URL)

Class:
    Food Review Page (sub-class of Page)
Attributes:
    str(Author)
    str(Category)
    set{class(Restaurant)s}
    class(Top Picks)
    str(YouTube link)
    str(URL)

Class:
    Restaurant
Attributes:
    str(Category)
    File(Images/Gifs)
    int(Rating)
    str(Location)
    datetime(Opening Hours)

Class:
    Top Picks
Attributes:
    dict{class(Judge)s:class(Restaurant)s}

Class:
    Author
Functions:
    To determine regex or extraction style

(OPTIONAL)
Class:
    Judge
Attributes:
    int(Appearances)


    
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