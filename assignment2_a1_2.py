#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:11:37 2017

@author: shreejiths
"""
#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : assignment_a1_2

######## Your Code Below ########
def Tangent(AMin,AMax):
    '''Prints calues for the tangent of an angle in degrees'''
    import math
    Angles=[x for x in range(AMin,AMax+1)]
    Sin = []
    Cos = []
    Tan = []
    i=AMin
    for i in Angles:
        i=math.radians(i)
        Sin.append(int(math.sin(i)*10000000))
        Cos.append(int(math.cos(i)*10000000))   
    i=AMin
    while i <= AMax:
        Tan.append((Sin[i]/10000000)/(Cos[i]/10000000))
        i+=1
    print("Tangent of", AMin, "to", AMax,"degrees in steps of 1 degree: ")
    print(Tan)

def VowelsExtract(INPUT):
    '''Prints a list of the vowles found in an input given in the form: \n VowelsExtract(input to check)'''
    Vowels = ["A","E","I","O","U","a","e","i","o","u"]
    VowelsFound = []
    INPUT = INPUT.lower()
    L = len(INPUT)
    i=0
    while i < L:
        if INPUT[i] in Vowels:
            VowelsFound.append(INPUT[i])
        i+=1
    print("Vowels Found: ",VowelsFound)

def xx5(Xmin, Xmax, Ymax):
    '''Prints values for y=x*x+5 in ranges given using inputs:\n xx5(lower x, upper x, upper y) \n note, lower y default 0'''
    x = [x for x in range(Xmin, Xmax+1)]
    y = []
    OutDomain = []
    for i in x:
        y.append(i*i+5)
    L = len(y)
    i=0
    while i < L:
        if (y[i]) > Ymax:
            OutDomain.append(i)
            i+=1
            continue
        else:
            i+=1
            continue
    count=0
    for i in OutDomain:
        y.remove(y[i-count])
        x.remove(x[i-count])
        count+=1
    for i in x:
        print(i,(i*i+5))

Tangent(0,89)
print("\n")
VowelsExtract("Alex Barker Assignment 2")
print("\n")
xx5(-5,5,10)