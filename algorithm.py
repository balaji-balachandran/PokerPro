import sys
import random
from copy import deepcopy

# Algorithm to determine odds of winning a hand

# Hands are tuples of numeric values from 0-51
# Rank order
# 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

# Suit order 
# Clubs, diamonds, hearts, spades

# Draw a card from the deck and return it
# Note: Deck is passed by reference
def drawCard(deck):
    card = random.choice(deck)
    deck.remove(card)
    
    return card

def whoWins():
    pass

# Returns a tuple of (Hand type, 'highness' of Hand)

# Hand Types
# - Royal Flush
# - Straight Flush
# - Four of a Kind
# - Full House
# - Flush   
# - Straight
# - Three of a Kind
# - Two Pair
# - Pair
# - High Card

def MakeBestHand():
    

# Given two cards and an empty board 
# Takes tuple and returns odds 
def getPreflopOdds(my_hand, num_players, num_trials = 1):
    deck = list(range(52))
    # Remove our cards from the deck
    for card in my_hand:
        deck.remove(card)

    # For our hand, simulate a bunch of trials
    for i in range(num_trials):
        # Create a copy of the deck
        trial_deck = deepcopy(deck)
        
        # Give everyone
        player_hands = []
        for player in range(num_players):
            first_card = drawCard(trial_deck)
            second_card = drawCard(trial_deck)
            player_hands.append((first_card, second_card))
        
        board = [drawCard(trial_deck) for j in range(5)]


        print(my_hand)
        print(player_hands)
        print(board)
        print(trial_deck)
        print(len(trial_deck))
    
# Clubs, diamonds, hearts, spades
def convertLabelToNumeric(card):
    suit = card[1]
    offset = 0
    if(suit == 'C'):
        offset = 0
    elif(suit == 'D'):
        offset = 13
    elif(suit == 'H'):
        offset = 26
    elif(suit == 'S'):
        offset = 39

    rank = card[0]
    num = 0
    try:
        num = int(rank) - 2
    except ValueError:
        if(rank == 'J'):
            num = 9
        elif(rank == 'Q'):
            num = 10
        elif(rank == 'K'):
            num = 11
        elif(rank == 'A'):
            num = 12

    return offset + num    

if __name__ == '__main__':
    # Number of players at the table including yourself
    num_players = None
    try:
        num_players = int(sys.argv[1])
    except ValueError:
        print("Number of players must be an integer")
        exit()
    except IndexError:
        print("Number of players not entered; Assuming 6-handed table (5 other players)")
        num_players = 5


    # Get player hand and board from cameras
    labeled_hand = ["AH", "KS"]

    hand = tuple([convertLabelToNumeric(card) for card in labeled_hand])

    getPreflopOdds(hand, num_players)

    