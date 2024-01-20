import pyautogui
from time import sleep
import os

def main():
    
    initializePyAutoGUI()
    countdownTimer()
        
# =============================================================================
#     checkGameOver()
# =============================================================================
    playGame()
# =============================================================================
#     openDoor()
# =============================================================================
    
# =============================================================================
#     startNewGame()
# =============================================================================
# =============================================================================
#     reportMousePosition()
# =================================================

    print("Done")


def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True


def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 3):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")

def reportMousePosition(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        sleep(1)
        
def startNewGame():
    # Click on new game
    pyautogui.click(702, 1323, duration=0.1)
    # to get into char selection screen
    pyautogui.click(702, 1323, duration=0.2) 
    # click on too easy
    sleep(0.8)
    pyautogui.click(166, 417) 
    # start game
    pyautogui.click(2440, 1526, duration=0.3)
    sleep(0.5)
    # Skip cutscene
    pyautogui.click(2440, 1526, duration=0.5)
    sleep(5.5)
    playGame()
    
def playGame():    
    # Open first door
    count=0
        
    while True:
        ik = openDoor()
        if ik==1:
            count=count+1
            if count==3:
                resetGame()
        else:
            count=0
        sleep(6)
        checkGameOver()
        checkMainMenu()
        pyautogui.press('1')
        sleep(0.2)
        pyautogui.press('1')
        # heal if possible
        pyautogui.click(2353, 65, duration=0.1)
        sleep(0.5)
        
                
    return None
    
def openDoor():    
    images_to_check = [
            'door_001.png',
            'door_002.png',
            'door_003.png',
            'door_004.png',
            'door_005.png',
            'door_006.png',
            'door_007.png',
            'door_008.png',
            'door_009.png',
            'door_010.png'
        ]
    
    # loop over images until one is found, then return the index of the found
    # image
    for index, image_filename in enumerate(images_to_check):
        script_dir = os.path.dirname(__file__)
        Door_path = os.path.join(
            script_dir, 
            'images', 
            image_filename)
        try:
            image_pos = pyautogui.locateOnScreen(Door_path, confidence=0.9)
        except: print("Door {} not found".format(index+1))
        else:
            if image_pos:
                print("Door {} found".format(index+1))
                pyautogui.click(x=image_pos[0]+50, y=image_pos[1]+50, button='right')  # right-click the mouse
                sleep(0.2)
                pyautogui.click(x=image_pos[0]+50, y=image_pos[1]+50, button='right')  # right-click the mouse
                return None
                
    return 1
    
def checkGameOver():
    script_dir = os.path.dirname(__file__)
    Door_path = os.path.join(
        script_dir, 
        'images', 
        'game_over.png'
    )
    try:
        image_pos = pyautogui.locateOnScreen(Door_path, confidence=0.8)
    except: print("Game not over")
    else:
        if image_pos:
            print("Game over")
            sleep(0.5)
            pyautogui.click(x=2111, y=1534)  # right-click the mouse
            sleep(2)
            pyautogui.click(x=2404, y=1567)  # right-click the mouse
            sleep(4)
            startNewGame()
            return None
        
def checkMainMenu():
    script_dir = os.path.dirname(__file__)
    Door_path = os.path.join(
        script_dir, 
        'images', 
        'main_menu.png'
    )
    try:
        image_pos = pyautogui.locateOnScreen(Door_path, confidence=0.8)
    except: print("Not at main menu")
    else:
        if image_pos:
            print("Reached main menu")
            sleep(0.5)
            sleep(2)
            startNewGame()
            return None        

if __name__ == "__main__":
    main()
