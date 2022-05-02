import json
import time
import mouse
import pyscreenshot as ImageGrab
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import timeit
import easyocr
import numpy as np


# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")

# driver = webdriver.Chrome(chrome_options=options)

# driver.get("https://www.primerlearning.org")
# driver.execute_script("window.scrollTo(0, 1080)") 

reader = easyocr.Reader(['en'], gpu=False)
# time.sleep(11)

# #Fullscreen
# mouse.move(1290, 810, absolute=True, duration=0.01)
# time.sleep(0.1)
# mouse.click('left')

# time.sleep(2)

# #Turn of animation
# mouse.move(750, 960, absolute=True, duration=0.01)
# time.sleep(0.05)
# mouse.click('left')

#-------STARTUP DONE----------

def OneFlip():
    mouse.move(820, 900, absolute=True, duration=0.01)
    time.sleep(0.05)
    mouse.click('left')

def CheckFlipsLeft():
    im=ImageGrab.grab(bbox=(1050,805,1250,850))    
    im=np.array(im)
    flipsRemaining = reader.readtext(im, detail=0)[0]
    CheckFlipsLeft.flipsNum = [int(s) for s in flipsRemaining.split() if s.isdigit()][0]

def KeepScore():
    im=ImageGrab.grab(bbox=(900,430,1100,535))
    im=np.array(im)
    scoreText = reader.readtext(im, detail=0)
    scoreText = ' '.join(scoreText)
    scoreNums = [int(s) for s in scoreText.split() if s.isdigit()]
    heads = scoreNums[0]
    tails= scoreNums[1]
    score = f'{heads}.{tails}'
    tempSeq.append(score)

def Label():
    830/1030
    mouse.move(830, 1030, absolute=True, duration=0.01)
    time.sleep(0.05)
    mouse.click('left')

    #CHeck if Fair or Cheater
    time.sleep(1)
    im=ImageGrab.grab(bbox=(910,380,1020,450))
    im = im.convert("RGB")
    pixels = [i for i in im.getdata()]
    cheater = (211,89,116) in pixels

    if cheater == True:
        Label.totalCheater += 1
        print('CHEATER')
        with open('data.json', 'r+') as f:
            data = json.load(f)
            List = data["Cheater"]
            if tempSeq not in List:
                List.append(tempSeq)
            data["Cheater"] = List
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    else:
        Label.totalFair += 1
        print('FAIR')
        with open('data.json', 'r+') as f:
            data = json.load(f)
            List = data["Fair"]
            if tempSeq not in List:
                List.append(tempSeq)
            data["Fair"] = List
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

def CheckGameOver():
    time.sleep(0.4)
    im=ImageGrab.grab(bbox=(680,480,1240,580))
    im=np.array(im)
    gameOverText = reader.readtext(im, detail=0)
    print(gameOverText)
    if len(gameOverText) == 1:
        gameOverText = gameOverText[0]
    if 'Game Over' in gameOverText:
        print('lol im gay')
        time.sleep(2)
        mouse.move(950, 1030, absolute=True, duration=0.01)
        time.sleep(0.05)
        mouse.click('left')

Label.totalFair = 0 
Label.totalCheater = 0


for rpt in range(10):
    time.sleep(2)
    tempSeq = []
    CheckFlipsLeft()
    if CheckFlipsLeft.flipsNum < 15:
        totalFlips = CheckFlipsLeft.flipsNum
    else:
        totalFlips = 15
    for i in range(totalFlips):
        OneFlip()
        time.sleep(0.1)
        KeepScore()
    Label()
    CheckGameOver()
    with open('data.json', 'r') as f:
            data = json.load(f)
            fList = data["Fair"]
            cList = data["Cheater"]
            tList = fList + cList

    print(f'{rpt+1} Complete   |   Total Fair: {len(fList)} ({Label.totalFair})  Total Cheater: {len(cList)} ({Label.totalCheater})')
    print('-----------------------')