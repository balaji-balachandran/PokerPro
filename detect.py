from ultralytics import YOLO
import time
import cv2
import sys

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("playing_card_model.pt")  # load a pretrained model (recommended for training)

cards_dictionary = {
    0: '10C',
    1: '10D',
    2: '10H',
    3: '10S',
    4: '2C',
    5: '2D',
    6: '2H',
    7: '2S',
    8: '3C',
    9: '3D',
    10: '3H',
    11: '3S',
    12: '4C',
    13: '4D',
    14: '4H',
    15: '4S',
    16: '5C',
    17: '5D',
    18: '5H',
    19: '5S',
    20: '6C',
    21: '6D',
    22: '6H',
    23: '6S',
    24: '7C',
    25: '7D',
    26: '7H',
    27: '7S',
    28: '8C',
    29: '8D',
    30: '8H',
    31: '8S',
    32: '9C',
    33: '9D',
    34: '9H',
    35: '9S',
    36: 'AC',
    37: 'AD',
    38: 'AH',
    39: 'AS',
    40: 'JC',
    41: 'JD',
    42: 'JH',
    43: 'JS',
    44: 'KC',
    45: 'KD',
    46: 'KH',
    47: 'KS',
    48: 'QC',
    49: 'QD',
    50: 'QH',
    51: 'QS'
}


def getCardsFromLabels(labels):
    global cards_dictionary
    if(len(labels) == 0):
        return ['None']

    cards = []    
    for label in labels:
        if(label not in cards_dictionary):
            cards.append('Error')
        else:
            cards.append(cards_dictionary[label])
    return cards


def analyze_screenshot(filename):
    results = model(filename)

    unique_labels = set([int(x[-1]) for x in results[0]])
    cards = getCardsFromLabels(unique_labels)
    
    return cards

def capture_screenshot(screenshot_filename, callback = None):
    global model

    # Open the webcam
    try:
        cap = cv2.VideoCapture(int(sys.argv[1]))  # 0 is the default camera
    except ValueError:
        print("Error with argument: Could not open webcam.")
        return
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 's' to take a screenshot or 'q' to quit.")

    while True:
        # Read frames from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the webcam feed
        cv2.imshow("Webcam Feed", frame)

        # Check for key presses
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # Press 's' to save a screenshot
            
            cv2.imwrite(screenshot_filename, frame)
            print(f"Screenshot saved as {screenshot_filename}")
            cards = analyze_screenshot(screenshot_filename)
            if(len(cards) != 0 and callback != None):
                callback(cards)
            
        
        elif key == ord('q'):  # Press 'q' to quit
            print("Exiting...")
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Capture screenshot takes in a file location to save to and a callback
    # e.g. use print to simply show the read card data to the screen
    capture_screenshot('data/screenshot.png', print)