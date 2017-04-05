#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:41:25 2017

@author: shreejiths
"""
#Python Template for ES2B4 Assignment

#Name: Alex Barker
#ID : U1512136
#Assignment Section : A3-3

######## Your Code Below ########
n=input("Please give a number to find the factorial of: ")
digitTest=n.isdigit()
if(digitTest==True):
    n=int(n)
    start=n
    fact=1
    while (n>1):
        fact *= n
        n -= 1
    print(start,"factorial is",fact)
else:
    print("please give positive integers only")