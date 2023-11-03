#!python3
'''
Coin Toss
Ask the player to choose heads or tails.
Toss a coin to determine what the coin will be, and then tell the player if they were correct.
(2 points)
'''
import random

compToss = random.randint(0,1)

def playerChoice():
    playerToss = input('Heads or tails? ')
    playerToss.lower()
    playerToss = playerToss.replace(' ','')
    
    if playerToss=='heads' or playerToss=='head':
        playerToss=0
    elif playerToss=='tails' or playerToss=='tail':
        playerToss=1
    else:
        playerToss=None

    return playerToss

def GameOutcome(comp,player):
    if comp==0:
        compChoice='heads'
    else:
        compChoice='tails'
    print(type(player))
    if player==comp:
        print(f'You won, the flipped coin was {compChoice}.')
    elif type(player)==int:
        print(f'You lost, the flipped coin was {compChoice}.')
    else:
        print('invalid input')

playerToss = playerChoice()

GameOutcome(compToss,playerToss)