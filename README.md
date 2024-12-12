# Poker Pro
We suck at poker. So we made a system to cheat so we could suck a little less. 
## Get Started
1. First, install Python 3.12 from https://www.python.org/downloads/. Newer versions may work, but are untested
1. Clone the repository
```
https://github.com/balaji-balachandran/PokerPro.git
```
3. Navigate to the directory
```
cd PokerPro
```

4. Install the opencv, ultralytics, and pyttsx3 modules. Note there may be various aliases for python. Use one that works
 > If your machine recognizes py
  ```
  py -m pip install opencv-python ultralytics==8.0.0 pyttsx3
  ```
> If your machine recognizes python3
  ```
  python3 -m pip install opencv-python ultralytics==8.0.0 pyttsx3
  ```
> If your machine recognizes py
  ```
  python -m pip install opencv-python ultralytics==8.0.0 pyttsx3
  ```
5. Run ```server.py```
```
py server.py [Server Port]
```
6. Run ```hand_detect.py``` from a device with a webcam that will see your own cards
```
py hand_detect.py [Webcam Index] [Server IP] [Server Port] [Client Port]
```
7. Run ```board_detect.py``` from a device with a webcam that will see your own cards
```
py board_detect.py [Webcam Index] [Server IP] [Server Port] [Client Port]
```


As the game progresses, the program will alert you of your odds of winning, hitting a particular hand, etc.
