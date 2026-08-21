import time
import pyautogui
import random

#Heroes
archer_queen = 'hero/archer_queen.png'
barbarian_king = 'hero/barbarian_king.png'
grand_warden = 'hero/grand_warden.png'
minion_prince = 'hero/minion_prince.png'
royal_champion = 'hero/royal_champion.png'
dragon_duke = 'hero/dragon_duke.png'
heroes_list = [dragon_duke, grand_warden, archer_queen, barbarian_king]#, , archer_queen, royal_champion, barbarian_king, minion_prince]
#Troops
giant = "troops/giant.png"
archer = "troops/archer.png"
electro_dragon = "troops/electro_dragon.png"
wall_breaker = "troops/larry.png"
event_broom_witch = "troops/event_broom_witch.png"
event_electro_troop = "troops/event_electro_troop.png"
#Seige Machines
wall_wrecker = "seige_machines/wall_wrecker.png"
wall_wrecker_2 = "seige_machines/wall_wrecker_2.png"
flame_fringer = "seige_machines/flame_flinger.png"
clan_troops = "clan_troops.png"
issue_with_clan_troops = "issue_with_clan_troops.png"

#Co-Ordinates:
top_left_x = 221
top_left_y = 522
top_right_x = 1227
top_right_y = 147
bottom_left_x = 567
bottom_left_y = 792
bottom_right_x = 1694
bottom_right_y = 535
#screen_wicth, screen_height
screen_width, screen_height = pyautogui.size()

def reset_mouse_focus():
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width/2, screen_height/2, duration=0.5)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)

#zooms out the game
def simulate_zoom_out():
    # print("Trying to Zoom out.")
    # for _ in range(1, 20):
    #     pyautogui.scroll(random.randint(10000, 12000)*-1)      # Scroll down (zoom out) by 10 "clicks"
    #     time.sleep(random.uniform(0.1, 0.3))
    # pass
    print("Zooming out...")
    pyautogui.keyDown('ctrl')  # Hold Ctrl key
    for _ in range(1):
        pyautogui.scroll(-500)  # Moderate downward scroll
        time.sleep(random.uniform(0.1, 0.3))

pyautogui.keyUp('ctrl')

def claimRewards():
    print("claiming Rewards.")
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('claim_reward_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
    time.sleep(4)
    reset_mouse_focus()
    pyautogui.click(clicks=5, interval=0.25) # 5 click with a 0.25 second pause between clicks
    time.sleep(2)
    pyautogui.click(pyautogui.locateCenterOnScreen('continue_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
    
def end_game():
    time.sleep(1)
    try:
        try:
            pyautogui.click(pyautogui.locateCenterOnScreen('end_battle_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
            time.sleep(1)
            pyautogui.click(pyautogui.locateCenterOnScreen('okay_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
            time.sleep(2)
            pyautogui.click(pyautogui.locateCenterOnScreen('return_home_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
        except:
            print("Couldn't End battle. Now, Trying to Surrender.")
            try:
                pyautogui.click(pyautogui.locateCenterOnScreen('surrender_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
                time.sleep(1)
                pyautogui.click(pyautogui.locateCenterOnScreen('okay_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
                time.sleep(2)
                pyautogui.click(pyautogui.locateCenterOnScreen('return_home_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
            except:
                print("Couldn't End or surrender. Now, Trying to Return Home.")
                pyautogui.click(pyautogui.locateCenterOnScreen('return_home_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
                time.sleep(1)
            time.sleep(1)
    except:
        claimRewards()
    time.sleep(1)

#Clicks Troops or heroes based on the name
def click_troops_heroes(troop_name):
    pyautogui.click(pyautogui.locateCenterOnScreen(troop_name, confidence=0.75, grayscale=True, region=(0, 0, screen_width, screen_height)))

def activate_hero_power():
    time.sleep(1)
    #Activate Hero power
    for hero in heroes_list:
        try:
            click_troops_heroes(hero)
            reset_mouse_focus()
        except:
            print("Couldn't activate hero power.")

#Deploys Heroes on Fixed Co-ordinates
def deploy_heroes():
    time.sleep(1)
    # Deploy Dragon Duke
    click_troops_heroes(dragon_duke)
    pyautogui.moveTo(top_left_x, top_left_y, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)
    #Deploy Barbarian King
    click_troops_heroes(barbarian_king)
    pyautogui.moveTo(top_right_x, top_right_y, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)
    # Deploy Grand Warden
    click_troops_heroes(grand_warden)
    pyautogui.moveTo(bottom_right_x, bottom_right_y, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)
    #Deploy Archer Queen
    click_troops_heroes(archer_queen)
    pyautogui.moveTo(bottom_left_x, bottom_left_y, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)

#deploy 16 giants
def deploy_giants():
    click_troops_heroes(giant)
    pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=4, interval=0.2)
    pyautogui.click(x = bottom_left_x, y = bottom_left_y, clicks=4, interval=0.2)
    pyautogui.click(x = top_right_x, y = top_right_y, clicks=4, interval=0.2)
    pyautogui.click(x = top_left_x, y = top_left_y, clicks=4, interval=0.2)
    # Some troops to complete Event ----
    #                                   v
    # click_troops_heroes(archer)
    # pyautogui.click(x = top_left_x, y = top_left_y, clicks=3, interval=0.2)
    #Deploying wallbreakers after Giants
    deploy_wall_breakers()

def deploy_wall_breakers():
    #Wait for 2 seconds to allow giants to move forward
    time.sleep(random.uniform(2, 3))
    click_troops_heroes(wall_breaker)
    pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=3, interval=0.2)
    pyautogui.click(x = bottom_left_x, y = bottom_left_y, clicks=4, interval=0.2)
    pyautogui.click(x = top_right_x, y = top_right_y, clicks=4, interval=0.2)
    pyautogui.click(x = top_left_x, y = top_left_y, clicks=4, interval=0.2)

def deploy_seige_machines():
    try:
        click_troops_heroes(wall_wrecker)
        pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=3, interval=0.2)
    except:
        try:
            click_troops_heroes(wall_wrecker_2)
            pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=3, interval=0.2)
        except:
            try:
                click_troops_heroes(flame_fringer)
                pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=3, interval=0.2)
            except: 
                print("Couldn't deploy wall wrecker, Trying to deploy clan troops.")
                try:
                    click_troops_heroes(clan_troops)
                    pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=3, interval=0.2)
                except:
                    click_troops_heroes(issue_with_clan_troops)
                    pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=3, interval=0.2)
    
def deploy_electro_dragons():
    print("Trying to deploy electro dragon.")
    click_troops_heroes(electro_dragon)
    time.sleep(0.2)
    click_troops_heroes(electro_dragon)
    pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=2, interval=0.2)
    pyautogui.click(x = bottom_left_x, y = bottom_left_y, clicks=2, interval=0.2)
    pyautogui.click(x = top_right_x, y = top_right_y, clicks=2, interval=0.2)
    pyautogui.click(x = top_left_x, y = top_left_y, clicks=2, interval=0.2)
    print("Deployed electro dragon.")

def deploy_event_troops():
    try:
        click_troops_heroes(event_electro_troop)
        pyautogui.click(x = bottom_right_x, y = bottom_right_y, clicks=13, interval=0.2)
        pyautogui.click(x = bottom_left_x, y = bottom_left_y, clicks=13, interval=0.2)
        pyautogui.click(x = top_left_x, y = top_left_y, clicks=12, interval=0.2)
        pyautogui.click(x = top_right_x, y = bottom_right_y, clicks=12, interval=0.2)
    except: 
        print("Couldn't deploy event special electro broom troop.")

def fulfill_clan_troops():
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('clan_troops_fulfill_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
        time.sleep(1)
        pyautogui.click(pyautogui.locateCenterOnScreen('clan_troops_fulfill_confirm_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
    except:
        try:
            pyautogui.click(pyautogui.locateCenterOnScreen('clan_troops_fulfill_request_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
            time.sleep(1)
            pyautogui.click(pyautogui.locateCenterOnScreen('clan_troops_fulfill_request_okay_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
        except:
            print("Couldn't request for clan troops, Not spending Gems.")
    print("Couldn't fulfill clan troops instantly.")
    
def play_game():
    simulate_zoom_out()
    time.sleep(1.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('attack_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
    time.sleep(1)
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('find_match_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
    except:
        pyautogui.click(pyautogui.locateCenterOnScreen('find_match_btn_2.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
    time.sleep(1.5)
    fulfill_clan_troops()
    time.sleep(1.5)
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('attack_green_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
    except:
        pyautogui.click(pyautogui.locateCenterOnScreen('attack_green_btn_2.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
    time.sleep(random.uniform(12, 15))
    # simulate_zoom_out()
    deploy_giants()
    time.sleep(0.5)
    deploy_seige_machines()
    time.sleep(0.5)
    deploy_heroes()
    time.sleep(0.5)
    activate_hero_power()
    time.sleep(0.5)
    deploy_electro_dragons()
    time.sleep(0.5)
    # deploy_event_troops()
    time.sleep(random.uniform(60, 80))
    end_game()

time.sleep(1)
# pyautogui.click(pyautogui.locateCenterOnScreen('full_screen_btn.png', confidence=0.7, grayscale=True, region=(0, 0, screen_width, screen_height)))
for i in range(1, 20):
    time.sleep(random.uniform(4, 6))
    print("Playing game now: ", i)
    pyautogui.click(x = 242, y = 600, clicks=4, interval=0.2)
    play_game()