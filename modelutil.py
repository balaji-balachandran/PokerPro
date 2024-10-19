import cv2

# Utility to collect training data for the poker hands
# Run the program to open a webcam.
# Press/hold "s" to capture frame(s) with cards within the frame
# Press "q" to quit the program  

# Files stored at {DATADIRECTORY}/{BASE_FILE_NAME}{#}
DATA_DIRECTORY = "data"
BASE_FILE_NAME="hand"

# File that stores the counter
COUNTERFILE = 'counter.txt'

# Read the current counter from the file
def read_counter():
    try:
        with open(COUNTERFILE, 'r') as file:
            count = int(file.read())
    except:
        count = 0  # If error with file or parsing, assume 0 start

    return count

# Write the updated counter to the file
def write_counter(count):
    with open(COUNTERFILE, 'w') as file:
        file.write(str(count))

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()


counter = read_counter()

# Validate counter to ensure no accidental overwrites
if(counter == 0):
    response = ""
    while(response.lower() != "n" or response.lower() != "y"):
        response = input(f"{response} Counter file not found/corrupted. Start at 0? Y/N: ")
        if(response.lower() == "y"):
            write_counter(0)
            break
        elif(response.lower() == "n"):
            print("Exiting...")
            exit(1)
        else:
            response = "Invalid Response."            

while True:
    ret, frame = cap.read()

    # If frame was not captured correctly, exit
    if not ret:
        print("Issue retrieving frame (stream end?). Exiting ...")
        break

    # Show the frame in the webcam window
    cv2.imshow('Webcam', frame)

    # Get a keystroke
    key = cv2.waitKey(1)

    # Save frame and update counter
    if key == ord('s'):
        cv2.imwrite(f"{DATA_DIRECTORY}/{BASE_FILE_NAME}{counter}.jpg", frame)
        print(f"{DATA_DIRECTORY}/{BASE_FILE_NAME}{counter}.jpg")
        counter += 1
        write_counter(counter)
    
    elif key == ord('q'):
        break


# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()