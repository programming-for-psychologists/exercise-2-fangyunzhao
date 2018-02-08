'''
Created on Feb 7, 2018

@author: Olivia Zhao
'''

import time
import sys
import random
from psychopy import visual,event,core ,gui


names = open('names.txt', 'r').readlines()
lastNames = [name.split(' ')[1] for name in names] 
lastNames = [name.replace('\n', '') for name in lastNames]

win = visual.Window([800 , 600] , color = "black", units = 'pix')
lastNameStim = visual.TextStim( win , text = "", height = 40, color = "white", pos = [0,0])
crossStim = visual.TextStim( win , text = "+", height = 40, color = "white", pos = [0,0])
while True:
    crossStim.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(lastNames)
    lastNameStim.setText(nameShown)
    lastNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()


    if event.getKeys(['q']):
        break