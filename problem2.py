'''
Create a list that contains a deck of cards.
Shuffle and deal 5 card hands to 2 different players.  You may want to make use of the list commands we have previously explored to remove cards when they have been dealt to players.
'''
import random
cardDeck=[]
Suits=['C','D','H','S']

def MakeDeck():
    for i in range(1,14):
        for suit in Suits:
            cardDeck.append(f'{i}{suit}')
    random.shuffle(cardDeck)
    return cardDeck

def playerHand(deck):
    hand=[]
    for deal in range(5):
        hand.append(deck.pop(0))
    return hand,deck


cardDeck=MakeDeck()

play1Turn=playerHand(cardDeck)
player1Hand=play1Turn[0]
cardDeck=play1Turn[1]

play2Turn=playerHand(cardDeck)
player2Hand=play2Turn[0]
cardDeck=play2Turn[1]

print('\n',cardDeck)
print('\n',player1Hand,player2Hand)
