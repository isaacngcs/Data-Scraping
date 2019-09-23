# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:41:13 2019

@author: Isaac
"""

class Foodreview_Page(Page):
    
    def __init__(self, url, author, category, 
                 restaurants, top_picks, youtube_link):
        
        super().__init__(self, url)
        self.__author = self.set_author(author)
        self.__category = self.set_category(category)
        self.__restaurants = self.set_restaurants(restaurants)
        self.__top_picks = self.set_top_picks(top_picks)
        self.__youtube_link = self.set_youtube_link(youtube_link)
        
    def set_author(self, author):
        
        
        
    str(Author)
    str(Category)
    set{class(Restaurant)s}
    class(Top Picks)
    str(YouTube link)
    str(URL)