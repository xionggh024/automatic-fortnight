# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:49:39 2016

@author: Bear
"""

import pyautogui
pyautogui.size()
width,height=pyautogui.size()

#moveTo移动到指定的坐标
for i in range(1):
    pyautogui.moveTo(100,100,duration=0.25)
    pyautogui.moveTo(200,100,duration=0.25)
    pyautogui.moveTo(200,200,duration=0.25)    
    pyautogui.moveTo(100,100,duration=0.25)
    

#moveRel相对于当前鼠标位置移动光标    
for i in range(1):
    pyautogui.moveRel(100,0,duration=0.25)
    pyautogui.moveRel(0,100,duration=0.25)
    pyautogui.moveRel(-100,200,duration=0.25)    
    pyautogui.moveRel(0,-100,duration=0.25)

#获得当前鼠标位置    
print(pyautogui.position())

