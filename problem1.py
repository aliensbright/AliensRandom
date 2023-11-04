#!python3
'''
Advanced Dungeons and Dragons
optional rolling systems include:
a) roll 4 dice, discard the lowest
b) roll 3 dice, reroll 1's.
'''
import random
StatsList = ['Strength','Intelligence','Wisdom','Dexterity','Constitution','Charisma']
ScoreList = [0,0,0,0,0,0]

#Option a)

def Roll_A():
    RollList=[]
    for i in range(4):
        roll=random.randint(1,6)
        RollList.append(roll)

    RollList.sort()
    RollList.pop(0)
    scoreA=sum(RollList)
    return scoreA
    
for i in range(6):
    ScoreList[i]=Roll_A()

for m in range(6):
    print(StatsList[m],'==>',ScoreList[m])

#Option b)


def Roll_B():
    RollList=[]
    roll=1
    for i in range(3):
        roll=random.randint(1,6)
        while roll==1:
            roll=random.randint(1,6)
        else:
            RollList.append(roll)
    print(RollList)
    scoreB=sum(RollList)
    return scoreB

for i in range(6):
    ScoreList[i]=Roll_B()

for m in range(6):
    print(StatsList[m],'==>',ScoreList[m])