#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:11:37 2017

@author: shreejiths
"""
#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : assignment_a1_3_2

######## Your Code Below ########

def dictionary_comp():
    i=input('Subject Code: ')
    subject_code = {"ES2B0":0,"ES2B1":1,"ES2B2":2,"ES2B3":3,"ES2B4":4}
    studentRecord = [
                     [['John',90], ['Elvis',85], ['Thomas',95], ['Isha',85], ['Ranveer',79]],
                     [['John',90], ['Elvis',85], ['Thomas',95], ['Isha',85], ['Ranveer',79]],
                     [['John',90], ['Elvis',85], ['Thomas',95], ['Isha',85], ['Ranveer',79]],
                     [['John',90], ['Elvis',85], ['Thomas',95], ['Isha',85], ['Ranveer',79]],
                     [['John',90], ['Elvis',85], ['Thomas',95], ['Isha',85], ['Ranveer',79]]
                    ]

    subject_code = ['ES2B0','ES2B1','ES2B2','ES2B3','ES2B4']
    print("test: ",subject_code)
    
 #   sYR = dict((subject_code,studentRecord) for i in studentRecord[i])
    
    result = subject_code[subject_code[i]][studentRecord[i]]
    print(result)

dictionary_comp()




