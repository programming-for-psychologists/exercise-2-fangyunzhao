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

userVar = {'Name' : 'Enter your name'}

while True:
    box = gui.DlgFromDict(userVar)
    if userVar['Name'] not in firstNames:
        popupError('Name does not exist')
    else:
        print userVar['Name']
        break
    if event.getKeys('q'):
        break


