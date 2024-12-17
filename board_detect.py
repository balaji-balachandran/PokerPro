import sys
from detect import capture_screenshot
import requests
IDENTIFIER = 'BOARD_CAMERA'
server_ip = '192.168.1.13'

# Takes an array of cards as an argument.
# e.g. ['AH', 'KS', '2C', '4D', '2H']
# card array length may be greater than 5
# if there was an error with the detection

# Sends the cards to the server
def sendToServer(cards: [str]):
    # server_ip = sys.argv[2]  # Server IP passed as a command-line argument
    endpoint = f"http://{server_ip}:5000/board"  # The `/board` endpoint
    payload = {
        "identifier": IDENTIFIER,
        "cards": cards
    }
    try:
        # POST the detected cards to the server
        response = requests.post(endpoint, json=payload)
        if response.status_code == 200:
            print(f"Successfully sent data to server: {cards}")
        else:
            print(f"Failed to send data to server. Response: {response.text}")
    except Exception as e:
        print(f"Error communicating with server: {e}")

if __name__ == '__main__':
    screenshot_filename = 'data/board.png'

    # Not enough command line arguments entered, 
    # assume we are purposefully debugging
    if(len(sys.argv) < 6):
        print("-------------------- DEBUG MODE --------------------")
        capture_screenshot(screenshot_filename, sendToServer)    
        exit()
    
    server_ip = sys.argv[2]
    client_ip = sys.argv[3]
    server_port = sys.argv[4]
    client_port = sys.argv[5]

    # Set up connection as client (hand camera) to server
    # createConnection(server_ip, server_port, client_ip, client_port)

    # Start capturing screenshots and send back to server with callback
    capture_screenshot(screenshot_filename, sendToServer)

    # Uncomment this line to test with simply printing the cards
    # capture_screenshot(screenshot_filename, print)