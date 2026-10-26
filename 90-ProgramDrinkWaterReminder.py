# Exercise 11 -

import os 
import time

REPEAT_INTERVAL = 3600

while True:
    command = 'osascript -e \'say "Hey Aish Drink Water"\''
    os.system(command)
    time.sleep(REPEAT_INTERVAL)