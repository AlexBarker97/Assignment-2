#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:41:25 2017

@author: shreejiths
"""
#Python Template for ES2B4 Assignment

#Name: Alex Barker
#ID : U1512136
#Assignment Section : A3-1

######## Your Code Below ########
word=input("Give a word to test if its a palindrome: ",)
word = word.lower()     #could be removed, but for example with names such as "Hannah", it may be wanted
invWord = word[::-1]
print ("inverted word:",invWord)

length=len(word)
i = 0
print("length:",length)
while i < length:
    if word[i] == invWord[i]:
        i += 1
        if i == length - 1:
            print("word is a palindrome")
    else:
        print("the word is not a palindrome")
        break

    