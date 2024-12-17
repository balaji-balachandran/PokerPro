import requests
from algorithm import getHandOdds
from algorithm import convertLabelToNumeric
from algorithm import convertNumericToLabel
import pyttsx3
import time
num_players = 6
server_ip = '192.168.1.13' 

def get_current_cards(data):
    if data:
        return data[-1]['cards']
    return []

def get_previous_cards(data):
    if data:
        return data[-2]['cards']
    return []

# def is_new_game(hand_results, board_results):
#     current_hand = get_current_cards(hand_results)
#     current_board = get_current_cards(board_results)
#     previous_hand = get_previous_cards(hand_results)
#     previous_board = get_previous_cards(board_results)

#     if(len(previous_board) != len(current_board) or current_hand != previous_hand):
#         return True
#     return False

def get_response():
    response = requests.get(f"http://{server_ip}:5000/get_results")
    data = response.json() #gets all data in server
    hand_results = data.get('hand_results') # gets all hand_result data in server(old and new)
    board_results = data.get('board_results') # gets all board_result data in server(old and new)
    return hand_results, board_results

def calculate_output_result(hand_results, board_results):
    hand_cards_current = get_current_cards(hand_results) # gets current hand
    board_cards_current = get_current_cards(board_results) # gets current board
    if 'None' in hand_cards_current or 'None' in board_cards_current:
        return
    print(hand_cards_current)
    print(board_cards_current)
    hand = tuple([convertLabelToNumeric(card) for card in hand_cards_current])
    board = [convertLabelToNumeric(card) for card in board_cards_current]

    win_prob, hand_probs = getHandOdds(hand, num_players, board, 1000)
    win_prob = win_prob * 100
    prob = str(win_prob)

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed (words per minute)
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    if len(hand_cards_current) != 2:
        text = "Error reading hand, hold up hand to camera to retry"
    if len(board_cards_current) > 5:
        text = "Error reading board, retrying now"
    else: 
        text = f"Your hand {convertNumericToLabel(hand[0])} and {convertNumericToLabel(hand[1])} gives you a {prob} percent chance of winning"

    # Convert text to speech
    engine.say(text)

    # Wait for the speaking to finish
    engine.runAndWait()
        
if __name__ == '__main__':

    count = 0
    while True:
        hand_results, board_results = get_response()
        calculate_output_result(hand_results, board_results)
        time.sleep(5)
        
    
