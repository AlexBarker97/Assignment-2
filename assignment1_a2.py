#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:41:25 2017

@author: shreejiths
"""
#Python Template for ES2B4 Assignment

#Name: Alex Barker
#ID : U1512136
#Assignment Section : A2

######## Your Code Below ########
p1=input('Player 1: ')
p2=input('Player 2: ')

TruthTableArray = [
                    ["Tie","Player 2 wins!","Player 1 wins!"],
                    ["Player 1 wins!","Tie","Player 2 wins!"],
                    ["Player 2 wins!","Player 1 wins!","Tie"]
                  ]
                   
choices = {"rock":0, "paper":1, "scissors":2}

if (p1 != 'rock') and (p1 != 'paper') and (p1 != 'scissors'):
    if (p2 != 'rock') and (p2 != 'paper') and (p2 != 'scissors'):
        print('both players did not choose either "rock","paper" or "scissors"')
    else:
        print('player 1 did not choose either "rock","paper" or "scissors"')
elif (p2 != 'rock') and (p2 != 'paper') and (p2 != 'scissors'):
    print('player 2 did not choose either "rock","paper" or "scissors"')
else:
    result = TruthTableArray[choices[p1]][choices[p2]]
    print(result)