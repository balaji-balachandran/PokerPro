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
    server_ip = sys.argv[1]
    client_ip = sys.argv[2]
    server_port = sys.argv[3]
    client_port = sys.argv[4]

    # Set up connection as client (hand camera) to server
    createConnection(server_ip, server_port, client_ip, client_port)

    # Start capturing screenshots and send back to server with callback
    capture_screenshot('data/board.png', sendToServer)

    # Uncomment this line to test with simply printing the cards
    # capture_screenshot('data/board.png', print)