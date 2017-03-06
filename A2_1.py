#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:11:37 2017

@author: shreejiths
"""
#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : A2_1

######## Your Code Below ########
def PigLatinImproved():
    VOWELS = ["a","e","i","o","u"]
    PuncMarks = [46,44,33,58,59,39,34,45,95,40,41,91,93,123,125]
    PuncFound = []
    ASCII = []
    SpaceFound = []
    IN = 0
    while IN == 0:
        IN = input("Sentence to translate: ")
        if IN == 'quit':
            IN = 1
        else:
            words = IN.lower()
            L = len(words)
            for i in words:
                ASCII.append(ord(i))
            print(ASCII)
            i=0
            while i < L:
                val = ASCII[i]
                if val == 32:
                    SpaceFound.append(i)
                    i+=1
                else:
                    i+=1
            ####################################################len(SpaceFound)
            FirstLet = words[0]
            ErrorState = 0
            i = 0
            OUT = ""
            if FirstLet in VOWELS:
                OUT = OUT + FirstLet
                while i < L:
                    test = words[i]
                    val = ord(test)
                    i+=1
                    if (val <=122 and val >= 97):
                        OUT = OUT + test
                        continue
                    elif val in PuncMarks:
                        PuncFound.append(test)
                        continue
                    else:
                        ErrorState = 1
                        break
                if FirstLet in VOWELS:
                    for i in PuncFound:
                        OUT = OUT + i
                        OUT = OUT[1:] + "hay"    
                else:
                    OUT = OUT[1:L] + FirstLet
                    for i in PuncFound:
                        OUT = OUT + i
                        OUT = OUT + "ay"
                if ErrorState == 1:
                    print("Please only give letters and punctuation") 
                else:
                    print(OUT)
PigLatinImproved()
