# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:27:54 2021

@author: ASUS
"""

def find_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(find_palindrome('momom'))
# momom