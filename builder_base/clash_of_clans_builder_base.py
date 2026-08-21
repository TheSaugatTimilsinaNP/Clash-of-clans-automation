import time
import pyautogui
import random

#Troops
giant = "builder_base/troops/giant.png"
witch = "builder_base/troops/witch.png"
cannon = "builder_base/troops/cannon.png"
barbarian = "builder_base/troops/barbarian.png"
battle_machine = "builder_base/troops/battle_machine.png"
battle_copter = "builder_base/troops/battle_copter.png"
#Troops List
troops = ['Q', '1', '2', '3', '4', '5', '6']

#Co-Ordinates:
top_left_x = 221
top_left_y = 522
top_right_x = 1227
top_right_y = 147
bottom_left_x = 567
bottom_left_y = 792
bottom_right_x = 1694
bottom_right_y = 535
screen_width, screen_height = pyautogui.size()

def reset_mouse_focus():
    screen_width, screen_height = pyautogui.size()
    time.sleep(0.1)
    pyautogui.moveTo(screen_width/2, screen_height/2, duration=0.5)
    time.sleep(0.1)

# # zooms out the game by scrolling
def simulate_zoom_out():
    print("Trying to Zoom out.")
    # Hold the Ctrl key during the entire scrolling sequence
    with pyautogui.hold('ctrl'):
        for _ in range(1, 20):
            pyautogui.scroll(random.randint(12000, 18000) * -1)  # Scroll down (zoom out)
            time.sleep(random.uniform(0.1, 1))

def end_game():
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('builder_base/btn/end_battle_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
        time.sleep(1)
        pyautogui.click(pyautogui.locateCenterOnScreen('builder_base/btn/okay_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
        time.sleep(2)
        pyautogui.click(pyautogui.locateCenterOnScreen('builder_base/btn/return_home_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
    except:
        print("Couldn't End battle. Now, Trying to Surrender.")
        try:
            pyautogui.click(pyautogui.locateCenterOnScreen('builder_base/btn/surrender_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
            time.sleep(1)
            pyautogui.click(pyautogui.locateCenterOnScreen('builder_base/btn/okay_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
            time.sleep(2)
            pyautogui.click(pyautogui.locateCenterOnScreen('builder_base/btn/return_home_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
        except:
            print("Couldn't End or surrender. Now, Trying to Return Home.")
            pyautogui.click(pyautogui.locateCenterOnScreen('builder_base/btn/return_home_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
            time.sleep(1)
        time.sleep(1)
    time.sleep(1)

def click_troops_heroes(troop_name):
    print("Trying to click: ", troop_name)
    print("Active Title:", pyautogui.getActiveWindowTitle())
    pyautogui.click(pyautogui.locateCenterOnScreen(troop_name, confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))

def activate_power():
    # print("Activating power now.")
    # pyautogui.press("Q")
    # pyautogui.press("Q")
    time.sleep(1)
    #Activate Hero power
    for _ in range (1, 4):
        time.sleep(19)
        # pyautogui.press("Q")

#deploy 14 giants
def deploy_giants():
    click_troops_heroes(giant)
    # pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=4, interval=0.2)
    pyautogui.click(x = bottom_left_x, y = bottom_left_y, clicks=1, interval=0.2)
    # pyautogui.click(x = top_right_x, y = top_right_y, clicks=4, interval=0.2)
    pyautogui.click(x = top_left_x, y = top_left_y, clicks=3, interval=0.2)
    
#deploy 1 canon
def deploy_canon():
    click_troops_heroes(cannon)
    pyautogui.click(x = bottom_left_x, y = bottom_left_y, clicks=1, interval=0.2)

def deploy_battle_machine():
    click_troops_heroes(battle_machine)
    pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=1, interval=0.2)

def deploy_battle_copter():
    click_troops_heroes(battle_copter)
    pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=1, interval=0.2)

# def deploy_witch():
#     print("Trying to Deploy witch.")
#     click_troops_heroes(witch)
#     pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=4, interval=0.2)

def deploy_barbarians():
    print("Trying to Deploy Barbarians.")
    click_troops_heroes(barbarian)
    pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=4, interval=1)
    pyautogui.click(x = bottom_right_x+15, y = bottom_right_y-15, clicks=4, interval=1)

def play_game():
    # simulate_zoom_out()
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('builder_base/btn/attack_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
    time.sleep(1)
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('builder_base/btn/find_now_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
    except:
        print("Couldn't locate find now button to find match.")
        # pyautogui.click(pyautogui.locateCenterOnScreen('find_match_btn_2.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
    time.sleep(random.uniform(5, 8))
    time.sleep(4)
    # simulate_zoom_out()
    time.sleep(1)
    deploy_giants()
    time.sleep(random.uniform(1, 2)-0.5)
    deploy_canon()
    time.sleep(random.uniform(1, 2)-0.5)
    try:
        deploy_battle_machine()
    except:
        print("Couldn't deploy battle machine.")
        deploy_battle_copter()
    time.sleep(random.uniform(1, 2))
    # deploy_witch()
    # time.sleep(random.uniform(1, 2))
    deploy_barbarians()
    time.sleep(random.uniform(1, 2))
    activate_power()
    time.sleep(random.uniform(40, 50))
    try:
        end_game()
    except:
        end_game()

time.sleep(1)
for i in range(1, 10):
    time.sleep(random.uniform(5.5, 10))
    print("Playing game now: ", i)
    pyautogui.click(x = 242, y = 600, clicks=4, interval=0.2)
    play_game()