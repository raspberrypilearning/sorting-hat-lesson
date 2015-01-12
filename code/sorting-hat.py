# Sorting Hat version 2 - Uses Pibrella
# By Raspberry Pi Certified Educator Simon Johnson, Team Python at Picademy September 2014 & Raspberry Pi Education Team

import pibrella
import time
import random
import os

def randomgenerator():
    number = random.randint(1, 4)
    if number == 1:
        os.system('mpg123 Gryffindor.mp3')
        time.sleep(1)
    elif number == 2:
        os.system('mpg123 Hufflepuff.mp3')
        time.sleep(1)
    elif number == 3:
        os.system('mpg123 Ravenclaw.mp3')
        time.sleep(1)
    else:
        os.system('mpg123 Slytherin.mp3')
        time.sleep(1)

while True:
    if pibrella.button.read():
        randomgenerator()
