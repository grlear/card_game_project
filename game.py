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
    random.shuffle(deck)  ##Advanced Topic: Shuffle the deck to randomize the order
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

#Function to get a valid card from a player
def get_valid_card(player_hand, player_number):
    while True:
        print("Player " + str(player_number) + " Hand: " + str(player_hand))
        rank = input("Player " + str(player_number) + ", enter the RANK of your card: ")
        suit = input("Player " + str(player_number) + ", enter the SUIT of your card: ")
        card = (rank, suit)
        if card in player_hand:
            player_hand.remove(card)
            print("Player " + str(player_number) + " plays: " + str(card))
            return card
        else:
            print("Invalid card. Please enter a valid rank and suit from your hand.")

def play_game():
    #Initialize the deck and deal cards to both players
    deck = create_deck()
    player1_hand, player2_hand = deal_cards(deck)
    
    #Player scores
    player1_score = 0
    player2_score = 0
    
    #Determine who leads first (random)
    current_leader = random.choice([1, 2]) #Advanced Topic: Randomly select who leads first
    print("Player " + str(current_leader) + " will lead the first round.")

    #Game loop
    round_counter = 0
    while round_counter < 16:
        round_counter += 1
        print("\nRound " + str(round_counter) + ":")
        
        if current_leader == 1:
            print("Player 1's turn")
            card1 = get_valid_card(player1_hand, 1)
            
            print("\nPlayer 2's turn")
            card2 = get_valid_card(player2_hand, 2)

        else:
            print("Player 2's turn")
            card2 = get_valid_card(player2_hand, 2)
            
            print("\nPlayer 1's turn")
            card1 = get_valid_card(player1_hand, 1)

        #Determine the winner of the round
        if compare_cards(card1, card2):
            print("Player 1 wins the round!")
            player1_score += 1
            current_leader = 1
        else:
            print("Player 2 wins the round!")
            player2_score += 1
            current_leader = 2

    #Final scores
    print("\n--- Final Score ---")
    print("Player 1: " + str(player1_score))
    print("Player 2: " + str(player2_score))

    if player1_score > player2_score:
        print("Player 1 wins the game!")
    elif player2_score > player1_score:
        print("Player 2 wins the game!")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    play_game()