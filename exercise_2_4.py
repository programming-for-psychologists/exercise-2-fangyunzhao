'''
Created on Feb 7, 2018

@author: Olivia Zhao
'''

import time
import sys
import random
from psychopy import visual, event, core, gui


names = open('names.txt', 'r').readlines()

allNames = []
for name in names:
    allNames.append(name.split(' ')[0])
    allNames.append(name.split(' ')[1])

lastNames = [name.split(' ')[1] for name in names] 
lastNames = [name.replace('\n', '') for name in lastNames]
firstNames = [name.split(' ')[0] for name in names] 
    
allNames = [name.replace('\n', '') for name in allNames]

win = visual.Window([800 , 600] , color = "black", units = 'pix')
crossStim = visual.TextStim( win , text = "+", height = 40, color = "white", pos = [0,0])
NameStim = visual.TextStim( win , text = "", height = 40, color = "white", pos = [0,0])

while True:
    crossStim.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(allNames)
    NameStim.setText(nameShown)
    NameStim.draw()
    win.flip()
    if nameShown in firstNames:
        event.waitKeys(keyList = 'f')
    elif nameShown in lastNames:
        event.waitKeys(keyList = 'l')
    win.flip()


    if event.getKeys(['q']):
        break