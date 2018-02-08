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
    
allNames = [name.replace('\n', '') for name in allNames]


win = visual.Window([800 , 600] , color = "black", units = 'pix')
NameStim = visual.TextStim( win , text = "", height = 40, color = "white", pos = [0,0])
crossStim = visual.TextStim( win , text = "+", height = 40, color = "white", pos = [0,0])

while True:
    crossStim.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(allNames)
    NameStim.setText(nameShown)
    NameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()


    if event.getKeys(['q']):
        break