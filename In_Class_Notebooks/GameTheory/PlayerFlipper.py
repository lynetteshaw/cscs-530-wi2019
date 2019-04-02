# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:30:04 2018

@author: shawla
"""

def move(history):
    mine, theirs = history
    if len(mine) % 2 == 0:
        return 'C'
    else:
        return 'D'