'''
Created on Feb 7, 2018

@author: Olivia Zhao
'''

import time
import sys
import random
from psychopy import visual, event, core, gui

def popupError(text):
    errorDlg = gui.Dlg(title="Error", pos=(200,400))
    errorDlg.addText('Error: '+text, color='Red')
    errorDlg.show()
    

names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names] 
firstNames = [name.lower() for name in firstNames]

win = visual.Window([800 , 600] , color = "black", units = 'pix')
crossStim = visual.TextStim( win , text = "+", height = 40, color = "white", pos = [0,0])
wrongStim = visual.TextStim( win, text = 'X', height = 40, color = "red", pos = [0,0])
firstNameStim = visual.TextStim( win , text = "", height = 40, color = "white", pos = [0,0])


userVar = {'Name' : 'Enter your name'}

# to get a pop-up for name
while True:
    box = gui.DlgFromDict(userVar)
    if userVar['Name'] not in firstNames:
        popupError('Name does not exist')
    else:
        print userVar['Name']
        break
    if event.getKeys('q'):
        break

# stimulus
while True:
    crossStim.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(firstNames)
    firstNameStim.setText(nameShown)
    firstNameStim.draw()
    win.flip()
    if nameShown == userVar['Name']:
        rightR = ['space']
    else:
        rightR = None
    
    res = event.waitKeys(maxWait = 1, keyList = 'space')
    
    if res != rightR:
        wrongStim.draw()
        win.flip()
        core.wait(.5)
    
    if event.getKeys('q'):
        break

