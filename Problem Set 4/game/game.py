#Problem Statement: https://cs50.harvard.edu/python/2022/psets/4/game/
import random
import sys

def main():
    n=get_input("Level: ")
    x=random.randint(1,n)
    while True:
        guess=get_input("Guess: ")
        if (guess==x):
            sys.exit("Just right!")
        elif(guess<x):
            print("Too small!")
        else:
            print("Too large!")

def get_input(prompt):
    while True:
        try:
            n=int(input(prompt))
            if n>0:
                return n
        except ValueError:
            pass

main()