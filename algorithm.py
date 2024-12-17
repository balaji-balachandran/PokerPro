import sys
import random
from copy import deepcopy

# Algorithm to determine odds of winning a hand

# Hands are tuples of numeric values from 0-51
# Rank order
# 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

# Suit order 
# Clubs, diamonds, hearts, spades

ROYAL_FLUSH = 9
STRAIGHT_FLUSH = 8
QUADS = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
TRIPS = 3
TWO_PAIR = 2
PAIR = 1
HIGH_CARD = 0

# Draw a card from the deck and return it
# Note: Deck is passed by reference
def drawCard(deck):
    card = random.choice(deck)
    deck.remove(card)
    
    return card

# Function that returns 1 if you win against
# ALL other hands and 0 if you lose to some hand
# 2 if you split
def IWin(my_hand, other_hands):
    willSplit = False

    for other_hand in other_hands:
        if(my_hand[0] < other_hand[0]):
            return 0
        elif(my_hand[0] > other_hand[0]):
            continue
        # TODO: Handle tie break cases
        tiebreak_result = tiebreak(my_hand[1], other_hand[1])
        if(tiebreak_result == 1):
            continue
        elif(tiebreak_result == 2):
            return 0
        else:
            willSplit = True

    # Only return true if we won't split
    return 2 if willSplit else 1

# Returns a tuple of (Hand type, 'highness' of Hand)
# E.g. pair of aces would return ()
# Hand Types
# - Royal Flush     (9) -> No tiebreak
# - Straight Flush  (8) -> tiebreak on higher top number
# - Four of a Kind  (7) -> tiebreak on higher quads, tiebreak on 
# - Full House      (6)
# - Flush           (5)
# - Straight        (4)
# - Three of a Kind (3)
# - Two Pair        (2)
# - Pair            (1)
# - High Card       (0)

def MakeBestHand(hand, board):
    cards = list(hand) + board
    cards.sort()
    
    clubs = [x for x in cards if 0 <= x <= 12]
    diamonds = [x for x in cards if 13 <= x <= 25]
    hearts = [x for x in cards if 26 <= x <= 38]
    spades = [x for x in cards if 39 <= x <= 51]

    # Royal and straight flush check
    for group in [clubs, diamonds, hearts, spades]:        
        # Check for 5 consecutive elements
        for i in range(len(group) - 4):  # Stop 4 elements before the end
            if group[i+1] == group[i] + 1 and \
               group[i+2] == group[i] + 2 and \
               group[i+3] == group[i] + 3 and \
               group[i+4] == group[i] + 4:
                return [ROYAL_FLUSH, [0]] if ((group[i] + 4) % 13) == 12 else \
                       [STRAIGHT_FLUSH, [(group[i] + 4) % 13]]

    # Calculate rank differences
    card_ranks = [0] * 13
    for card in cards:
        card_ranks[card % 13] += 1

    for i in range(len(card_ranks)):
        # Quads check 
        if(card_ranks[i] == 4):
            # Determine our kicker
            for j in range(len(card_ranks) - 1, -1, -1):
                if 0 < card_ranks[j] < 4:
                    return [QUADS, [i, j]]

            # We should never get here
            return [None, None, None]

    # Full house can be made of either two trips or 
    if (3 in card_ranks and 2 in card_ranks) or card_ranks.count(3) == 2:
        # Choose the higher triple
        triple = None
        for i in range(len(card_ranks) - 1, -1, -1):
            if(card_ranks[i] == 3):
                triple = i
                break
        
        for j in range(len(card_ranks) - 1, -1, -1):
            if(card_ranks[j] >= 2 and triple != j):
                pair = j
                return [FULL_HOUSE, [triple, pair]]

    # Flush Check
    for group in [clubs, diamonds, hearts, spades]:
        if(len(group) >= 5):
            # There's probably a better way to mathematically figure 
            # out a more minimal number of cards to send back, but 
            # that sounds like a Humza problem 
            return[FLUSH, group[-5:]]

    # Straight Check
    for i in range(len(card_ranks) - 5, -1, -1):
        if(card_ranks[i] > 0 and \
           card_ranks[i + 1] > 0 and \
           card_ranks[i + 2] > 0 and \
           card_ranks[i + 3] > 0 and \
           card_ranks[i + 4] > 0):
           return [STRAIGHT, [i + 4]]
        
    # Check for A-5 Straight
    if( card_ranks[-1] > 0 and \
        card_ranks[0] > 0 and \
        card_ranks[1] > 0 and \
        card_ranks[2] > 0 and \
        card_ranks[3] > 0 
    ):
        return [STRAIGHT, [3]]

    for i in range(len(card_ranks)):
        # Trips check 
        if(card_ranks[i] == 3):
            # Determine our kickers
            for j in range(len(card_ranks) - 1, -1, -1):
                if 0 < card_ranks[j] < 3:
                    for k in range(j - 1, -1, -1):
                        if 0 < card_ranks[k] < 3:
                            return [TRIPS, [i, j, k]]

            # We should never get here
            return [None, None, None]

    # Two pair check
    if(card_ranks.count(2) >= 2):
        higher_pair = None
        lower_pair = None
        for i in range(len(card_ranks) - 1, -1, -1):
            if card_ranks[i] == 2:
                higher_pair = i
                break
        for i in range(higher_pair - 1, -1, -1):
            if card_ranks[i] == 2:
                lower_pair = i
                break
        for i in range(len(card_ranks) - 1, -1, -1):
            if card_ranks[i] == 1:
                return [TWO_PAIR, [higher_pair, lower_pair, i]]
        
        return [None, None, None, None]

    # Pair check
    for i in range(len(card_ranks)):
        if(card_ranks[i] == 2):
            card_ranks[i] = 0

            highest = None
            middle = None
            lowest = None
            for j in range(len(card_ranks) - 1, -1, -1):
                if(card_ranks[j] == 1 and highest == None):
                    highest = j
                elif(card_ranks[j] == 1 and middle == None):
                    middle = j
                elif(card_ranks[j] == 1 and lowest == None):
                    lowest = j
                    return[PAIR, [i, highest, middle, lowest]]
            return [None]

    # High card
    largest_five = sorted([i for i, x in enumerate(card_ranks) if x == 1], reverse=True)[:5]
    return [HIGH_CARD, largest_five]
    
# Returns 1 if player one wins, 2 if player 2 wins,
# or 0 if it is truly a tie
def tiebreak(tiebreak_array_1, tiebreak_array_2):
    for i in range(len(tiebreak_array_1)):
        tiebreak_1 = tiebreak_array_1[i]
        tiebreak_2 = tiebreak_array_2[i]
        if(tiebreak_1 > tiebreak_2):
            return 1
        elif(tiebreak_2 > tiebreak_1):
            return 2

    return 0

# Given two cards and (optionally) a board
# Determine odds of creating each type of hand
# Calculate global odds of winning

# Monte Carlo simulation approach, we run over 
# numerous trials to get de
def getHandOdds(my_hand, num_players, board = [], num_trials = 1000):
    deck = list(range(52))
    # Remove our cards from the deck

    for card in my_hand:
        if card in deck:
            deck.remove(card)

    # Remove cards on the board from the deck
    for card in board:
        if card in deck:
            deck.remove(card)

    wins = 0
    hand_type_count = [0] * 10

    hands_seen = set()
    # For our hand and current board simulate a bunch of trials
    for i in range(num_trials):
        # Create a copy of the deck
        trial_deck = deepcopy(deck)
        trial_board = deepcopy(board)
        
        # Give everyone
        player_hands = []
        for player in range(num_players):
            first_card = drawCard(trial_deck)
            second_card = drawCard(trial_deck)
            player_hands.append((first_card, second_card))
        
        for j in range(5 - len(board)):
            trial_board.append(drawCard(trial_deck))

        # Uncomment to simulate a board
        # trial_board = [0, 10, 20, 25, 51]

        my_best_hand = MakeBestHand(my_hand, trial_board)

        other_hands = [MakeBestHand(player_hand, trial_board) for player_hand in player_hands]
        if(IWin(my_best_hand, other_hands)):
            wins += 1
        
        # Add your hand to the dictionary of what you can create
        my_type = my_best_hand[0]
        # if(my_type not in hands_seen):
        #     hands_seen.add(my_type)
            # print(my_best_hand, [convertNumericToLabel(my_hand[0]), convertNumericToLabel(my_hand[1])] + [convertNumericToLabel(l) for l in trial_board])
            
        hand_type_count[my_type] += 1

    # Normalize wins and count of each hand type by the number of trials
    win_probability = wins / num_trials
    hand_probabilities = []
    for i in range(len(hand_type_count)):
        hand_probabilities.append(hand_type_count[i] / num_trials)

    return win_probability, hand_probabilities
    
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

def convertNumericToLabel(card):
    rank = card % 13
    if(rank == 12):
        rank = 'A'
    elif(rank == 11):
        rank = 'K'
    elif(rank == 10):
        rank = 'Q'
    elif(rank == 9):
        rank = 'J'
    else: 
        rank += 2

    suit = card // 13
    if(suit == 0):
        return str(rank)+'C'
    elif(suit == 1):
        return str(rank)+'D'
    elif(suit == 2):
        return str(rank)+'H'
    elif(suit == 3):
        return str(rank)+'S'

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
    labeled_hand = ["AH", "5H"]

    hand = tuple([convertLabelToNumeric(card) for card in labeled_hand])
    board = [convertLabelToNumeric(card) for card in ['2S', '3S', '4S']]
    # print([convertNumericToLabel(i) for i in hand])
    win_probability, hand_probabilities = getHandOdds(hand, num_players, board, num_trials = 10000)
    print(win_probability, hand_probabilities)

    