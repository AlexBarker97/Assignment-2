#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:41:25 2017

@author: shreejiths
"""
#Python Template for ES2B4 Assignment

#Name: Alex Barker
#ID : U1512136
#Assignment Section : A3-2

######## Your Code Below ########
import time
i=input("Starting Value (seconds): ")
digitTest=i.isdigit()
if(digitTest==True):
        i=int(i)
        while (i >= 1):  
            print ('seconds remaining: ', i)
            i -= 1
            time.sleep(1)
        if (i >= -1):
            print ("Finished!")
else:
    print("please give positive integers only")