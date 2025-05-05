import random

#List of card ranks
card_ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen']

#List of suits
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

#Function to create a deck of cards
def create_deck():
    deck = []
    for suit in suits:
        for rank in card_ranks:
            deck.append(rank + ' of ' + suit)
    random.shuffle(deck) #Shuffle the deck to randomize the order
    return deck