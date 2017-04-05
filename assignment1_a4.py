#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:41:25 2017

@author: shreejiths
"""
#Python Template for ES2B4 Assignment

#Name: Alex Barker
#ID : U1512136
#Assignment Section : A4

######## Your Code Below ########
def CyclicCipher (word,shift):
    cypherout = ""
    updated = 0
    for i in word:
        val = ord(i)
        updated = val + shift
        if (val <=90 and val >= 65):
            updated -= 65
            updated = updated % 26 
            if updated < 0:
                updated += 26
            updated += 65
            new = chr(updated)
        elif (val <=122 and val >= 97):
            updated -= 97
            updated = updated % 26 
            if updated < 0:
                updated += 26
            updated += 97
            new = chr(updated)
        elif (val <=57 and val >= 48):
            updated -= 48
            updated = updated % 10 
            if updated < 0:
                updated += 10
            updated += 48
            new = chr(updated)
        else:
            new = i
        cypherout = cypherout + new
    print (cypherout)
exitCount = 0
word = input("Enter a word: ")
if word == "Exit cipher":
    exitCount = 1
while (exitCount == 0):   
    shift = input("Enter shift amount: ")
    if not shift.lstrip("-").isdigit():
        print("Please give an integer")
        break
    shift = int(shift)
    new = 0
    CyclicCipher(word,shift)
    word = input("Enter a word: ")
    if word == "Exit cipher":
        exitCount = 1