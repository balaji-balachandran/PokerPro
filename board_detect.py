import sys
from detect import capture_screenshot

IDENTIFIER = 'BOARD_CAMERA'

# Create connection from client to the server.
# Identify as the hand camera
def createConnection(server_ip: str, client_ip: str, server_port: int, client_port: int):
    # TODO: Establish socket or HTTP connection to the server
    pass

# Takes an array of cards as an argument.
# e.g. ['AH', 'KS', '2C', '4D', '2H']
# card array length may be greater than 5
# if there was an error with the detection

# Sends the cards to the server
def sendToServer(cards: [str]):
    # TODO: communicate to server the cards we have
    pass

if __name__ == '__main__':
    screenshot_filename = 'data/board.png'

    # Not enough command line arguments entered, 
    # assume we are purposefully debugging
    if(len(sys.argv) < 6):
        print("-------------------- DEBUG MODE --------------------")
        capture_screenshot(screenshot_filename, print)    
        exit()
    
    server_ip = sys.argv[2]
    client_ip = sys.argv[3]
    server_port = sys.argv[4]
    client_port = sys.argv[5]

    # Set up connection as client (hand camera) to server
    createConnection(server_ip, server_port, client_ip, client_port)

    # Start capturing screenshots and send back to server with callback
    capture_screenshot(screenshot_filename, sendToServer)

    # Uncomment this line to test with simply printing the cards
    # capture_screenshot(screenshot_filename, print)