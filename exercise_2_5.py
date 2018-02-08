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
NameStim = visual.TextStim( win , text = "", height = 40, color = "white", pos = [0,0])
crossStim = visual.TextStim( win , text = "+", height = 40, color = "white", pos = [0,0])
rightStim = visual.TextStim( win , text = "O", height = 40, color = "Green", pos = [0,0])
wrongStim = visual.TextStim( win, text = 'X', height = 40, color = "red", pos = [0,0])

while True:
    crossStim.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(allNames)
    NameStim.setText(nameShown)
    NameStim.draw()
    win.flip()
    if nameShown in firstNames:
        rightResponse = ['f']
    if nameShown in lastNames:
        rightResponse = ['l']
    response = event.waitKeys(keyList= ['f', 'l'])
    if response == rightResponse:
        rightStim.draw()
    else:
        wrongStim.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    
    if event.getKeys(['q']):
        break