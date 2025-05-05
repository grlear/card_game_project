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
            deck.append((rank, suit))  #Store cards as tuples (rank, suit)
    random.shuffle(deck)  #Shuffle the deck to randomize the order
    return deck

#Function to deal cards to players
def deal_cards(deck):
    player1_hand = []
    player2_hand = []
    
    for i in range(8):
        player1_hand.append(deck.pop())
        player2_hand.append(deck.pop())
    
    return player1_hand, player2_hand

#Function to compare cards and decide the round winner
def compare_cards(card1, card2):
    rank_order = {'Ace': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12}
    
    #Compare suits first, if suits are the same, compare ranks
    if card1[1] == card2[1]: 
        return rank_order[card1[0]] > rank_order[card2[0]]  
    else:
        return False  #If suits are different, Player 2 wins the round

