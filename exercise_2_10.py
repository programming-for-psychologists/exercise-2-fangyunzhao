'''
Created on Feb 7, 2018

@author: Olivia Zhao
'''

import time
import sys
import random
from psychopy import visual, event, core, gui
from backports.configparser.helpers import str
from pandocfilters import Str

def popupError(text):
    errorDlg = gui.Dlg(title="Error", pos=(200,400))
    errorDlg.addText('Error: '+text, color='Red')
    errorDlg.show()
    

names = open('names.txt', 'r').readlines()
output = open('output.txt', 'w')
firstNames = [name.split(' ')[0] for name in names] 
firstNames = [name.lower() for name in firstNames]

win = visual.Window([800 , 600] , color = "black", units = 'pix')
crossStim = visual.TextStim( win , text = "+", height = 40, color = "white", pos = [0,0])
wrongStim = visual.TextStim( win, text = 'X', height = 40, color = "red", pos = [0,0])
firstNameStim = visual.TextStim( win , text = "", height = 40, color = "white", pos = [0,0])

timer = core.Clock()
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
    timer.reset()
    if nameShown == userVar['Name']:
        rightR = ['space']
    else:
        rightR = None
    
    res = event.waitKeys(maxWait = 1, keyList = 'space')
    
    if res:
        t = timer.getTime() * 1000
    if res != rightR:
        wrongStim.draw()
        win.flip()
        core.wait(.5)
    ans = int(res == rightR)
    
    output.write(str(ans) + '\t' + str(t) + '\n')
    
    if event.getKeys('q'):
        output.close()
        break

