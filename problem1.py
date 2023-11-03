#!python3
'''
Advanced Dungeons and Dragons
optional rolling systems include:
a) roll 4 dice, discard the lowest
b) roll 3 dice, reroll 1's.
'''
import random

#Option a)

StatsList = ['Strength','Intelligence','Wisdom','Dexterity','Constitution','Charisma']
ScoreList = ['','','','','','']

def Roll_A():
    RollList=[]
    for i in range(4):
        roll=random.randint(1,6)
        RollList.append(roll)

    RollList.sort()
    RollList.pop(0)
    print(RollList)
    score=sum(RollList)
    return score
    
for i in range(6):
    ScoreList[i]=Roll_A()

for m in range(6):
    print(StatsList[m],'==>',ScoreList[m])



#Option b)

