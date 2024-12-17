import cv2

def check_camera(index):
    """Check if camera at index is available."""
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"Camera found at index {index}")
        cap.release()
    else:
        print(f"No camera at index {index}")

def list_available_cameras(max_index=10):
    """Check and list all available cameras up to max_index."""
    for index in range(max_index):
        check_camera(index)

if __name__ == "__main__":
    list_available_cameras()
