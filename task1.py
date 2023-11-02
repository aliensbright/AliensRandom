#!python3
'''
Number Guessing Game
Have the computer generate a random number from 1 to 100.  The players will try to guess the number, and the computer will tell them if they are too high or too low.  Play continues until they guess correctly at which point the computer tells them how many guesses it took.
(2 points) 
'''
import random
playerGuess=0
count=1

def instructions():
    print('You will have 10 guesses to determine a random integer from 1-100. I will reply whether your guess is lower or higher than the answer')
    compNum=random.randint(1,100)
    return compNum

compNum = instructions()

while playerGuess!=compNum and count<11:
    playerGuess=int(input(f'\nEnter guess {count}:'))
    if playerGuess<compNum:
        print('\nToo Low!')
    elif playerGuess>compNum:
        print('\nToo High!')
    elif playerGuess==compNum:
        print(f'You got it, the answer was {compNum}!')
        break
    count+=1
else:
    print(f'You did not guess the number in 10 guesses. The correct answer was {compNum}')
