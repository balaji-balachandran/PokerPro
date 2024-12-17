from detect import capture_screenshot
import sys
import requests
import time

IDENTIFIER = 'HAND_CAMERA'
server_ip = '192.168.1.13'

# Sends an array of cards to the server
# e.g., ['AH', 'KS', '2C', '4D', '2H']
def sendToServer(cards: [str]):
    # server_ip = sys.argv[2]  # Server IP passed as a command-line argument
    endpoint = f"http://{server_ip}:5000/hand"  # The `/hand` endpoint
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
    screenshot_filename = 'data/hand_detect.png'

    # Check if enough command-line arguments are provided
    if len(sys.argv) < 6:
        print("-------------------- DEBUG MODE --------------------")
        while True:
            capture_screenshot(screenshot_filename, sendToServer)  # Debugging: just print detected cards
            exit()
            time.sleep(5)
    
    # Read server and client parameters from command-line arguments
    server_ip = sys.argv[2]
    client_ip = sys.argv[3]
    server_port = sys.argv[4]
    client_port = sys.argv[5]

    # Set up connection as the client
    # createConnection(server_ip, client_ip, server_port, client_port)

    # Start capturing screenshots, detect cards, and send results to the server
    print("Starting card detection...")

    capture_screenshot(screenshot_filename, sendToServer)  # Capture screenshot and send cards
