#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:46:30 2020

@author: jorgereis
"""


class Data:
    
    def __init__(self, dd, mm, aaaa):
        print( 'Construindo obejto de data {}'.format(self) )
        self.dd = dd
        self.mm = mm
        self.aaaa = aaaa  
    
    def formatada(self):
        print( str(self.dd), str(self.mm), str(self.aaaa), sep='/'  )
