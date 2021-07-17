#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 16:00:00 2021

@author: riyachak
"""

#Rock, Paper, Scissors
import random
total = 0
ties = 0 
compsc = 0

print ("Welcome to rock, paper, scissors!")
while True: 
    question = input("How many rounds do you want to play? ")
    try: 
        question = int(question)
        break
    except: 
        print ('please enter an integer value.')   
        
while question > 0: 
    decision = input('Rock, Paper, or Scissors? ')
    decision = decision.lower()
    while decision not in ["rock", "paper", "scissors"]:
        print ('invalid move')
        break
    mylist = ["rock", "paper", "scissors"]
    comp = random.choice(mylist)
    print ("Computer chose: ", comp)
    if decision == "rock" and comp == "paper":
        print ('You Lost!')
        compsc = compsc + 1
        
    if decision == "rock" and comp == "rock":
        print ("You Tied!")
        ties = ties + 1
        
    if decision == "rock" and comp == "scissors":
        print ("You Won!")
        total = total + 1
        
    if decision == "paper" and comp == "paper":
        print ("You Tied!")
        ties = ties + 1
        
    if decision == "paper" and comp == "rock":
        print ("You Won!")
        total = total + 1
        
    if decision == "paper" and comp == "scissors":
        print ("You Lost!")
        compsc = compsc + 1
        
    if decision == "scissors" and comp == "paper":
        print ("You Won!")
        total = total + 1

    if decision == "scissors" and comp == "scissors":
        print ("You Tied!")
        ties = ties + 1
        
    if decision == "scissors" and comp == "rock":
        print ("You Lost!")
        compsc = compsc + 1
    
    question = question - 1 

print ("Your Score:", total)
print ("Ties:", ties)
print ("Computer Score:", compsc )
if total > compsc: print ("congrats you won!")
elif total < compsc: print ("You lost :(")
elif total == compsc: print ("You tied with the computer!")

