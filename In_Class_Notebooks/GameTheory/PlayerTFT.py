# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:38:06 2018

@author: shawla
"""

def move(history):
    mine, theirs = history
    if len(theirs) > 0 and theirs[-1] == 'D':
        return 'D'
    else:
        return 'C'