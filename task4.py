#!python3
'''
Dungeons and Dragons Character Generator
In Dungeons and Dragons, players roll 3 dice to generate statistics for their characters.  The statistics recorded are:
strength
intelligence
wisdom
dexterity
constitution
charisma
Create a character generator that generates a character's statistics
'''
StatsList = ['Strength','Intelligence','Wisdom','Dexterity','Constitution','Charisma']
ScoreList = ['','','','','','']
import random

def DiceRoll3():
    roll1=random.randint(1,6)
    roll2=random.randint(1,6)
    roll3=random.randint(1,6)

    score=roll1+roll2+roll3
    return score

for i in range(6):
    ScoreList[i]=DiceRoll3()

for m in range(6):
    print(StatsList[m],'==>',ScoreList[m])