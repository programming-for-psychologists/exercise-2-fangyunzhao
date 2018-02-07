'''
Created on Feb 7, 2018

@author: fangyunzhao
'''

import time
import sys
import random
from psychopy import visual,event,core #,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""    

win = visual.Window([800 , 600] , color = "black", units = 'pix')
firstNameStim = visual.TextStim( win , text = "", height = 40, color = "white", pos = [0,0])
crossStim = visual.TextStim( win , text = "+", height = 40, color = "white", pos = [0,0])
while True:
    crossStim.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(firstNames)
    firstNameStim.setText(nameShown)
    firstNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()


    if event.getKeys(['q']):
        break