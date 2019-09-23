# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:44:04 2019

@author: Isaac
"""

class Project:
    
    def __init__(self, name, root, internal = set([]), prescraped = set([]), 
                 external = set([]), to_review = set([]), media = set([])):
        
        self.__name = name
        self.__root = root
        self.__internal = internal
        self.__prescraped = prescraped
        self.__external = external
        self.__to_review = to_review
        self.__media = media
    
    def get_name(self):
        
        return self.__name
    
    def get_root(self):
        
        return self.__root
    
    def get_internal(self):
        
        return self.__internal
    
    def set_internal(self, internal):
        
        if not isinstance(internal, set):
            raise TypeError("internal must be of type \"set\"")
        self.__internal = internal
    
    def add_internal(self, links):
        
        if isinstance(links, list):
            self.__internal = self.__internal|set(links)
        elif isinstance(links, str):
            self.__internal = self.__internal|set([links])
        elif isinstance(links, set):
            self.__internal = self.__internal|links
        else:
            raise TypeError("invalid type {type(links)}")
    
    def get_prescraped(self):
        
        return self.__prescraped
    
    def set_prescraped(self, prescraped):
        
        if not isinstance(prescraped, set):
            raise TypeError("prescraped must be of type \"set\"")
        self.__prescraped = prescraped
    
    def add_prescraped(self, links):
        
        if isinstance(links, list):
            self.__prescraped = self.__prescraped|set(links)
        elif isinstance(links, str):
            self.__prescraped = self.__prescraped|set([links])
        elif isinstance(links, set):
            self.__prescraped = self.__prescraped|links
        else:
            raise TypeError("invalid type {type(links)}")
    
    def get_external(self):
        
        return self.__external
    
    def set_external(self, external):
        
        if not isinstance(external, set):
            raise TypeError("external must be of type \"set\"")
        self.__external = external
        
    def add_external(self, links):
        
        if isinstance(links, list):
            self.__external = self.__external|set(links)
        elif isinstance(links, str):
            self.__external = self.__external|set([links])
        elif isinstance(links, set):
            self.__external = self.__external|links
        else:
            raise TypeError("invalid type {type(links)}")
        
    def get_to_review(self):
        
        return self.__to_review
    
    def set_to_review(self, to_review):
        
        if not isinstance(to_review, set):
            raise TypeError("external must be of type \"set\"")
        self.__to_review = to_review
        
    def add_to_review(self, links):
        
        if isinstance(links, list):
            self.__to_review = self.__to_review|set(links)
        elif isinstance(links, str):
            self.__to_review = self.__to_review|set([links])
        elif isinstance(links, set):
            self.__to_review = self.__to_review|links
        else:
            raise TypeError("invalid type {type(links)}")
            
    def get_media(self):
        
        return self.__media
    
    def set_media(self, media):
        
        if not isinstance(media, set):
            raise TypeError("external must be of type \"set\"")
        self.__media = media
        
    def add_media(self, links):
        
        if isinstance(links, list):
            self.__media = self.__media|set(links)
        elif isinstance(links, str):
            self.__media = self.__media|set([links])
        elif isinstance(links, set):
            self.__media = self.__media|links
        else:
            raise TypeError("invalid type {type(links)}")
            
    def sort_links(self):
        
        self.__internal = sorted(self.__internal)
        self.__prescraped = sorted(self.__prescraped)
        self.__external = sorted(self.__external)
        self.__to_review = sorted(self.__to_review)
        self.__media = sorted(self.__media)