import json
import mouse
import time
import pyscreenshot as ImageGrab
import pytesseract

with open('data.json', 'r') as f:
        data = json.load(f)

fairList = data["Fair"]
cheatList = data['Cheater']
totalList = fairList + cheatList

def oneFlip():
	mouse.move(840, 860, absolute=True, duration=0.01)
	mouse.click('left')

time.sleep(2)
newList = []
tempList = []
def checkGameOver():
    im=ImageGrab.grab(bbox=(840,960,1060,1000))
    text = pytesseract.image_to_string(im, lang="eng")
    # print(text)
    if 'Reset game' in text:
        checkGameOver.gameOver = True
    else:
        checkGameOver.gameOver = False


def label():
    if dominantText == 'Fair':
        mouse.move(840, 980, absolute=True, duration=0.01)
        mouse.click('left')
    if dominantText == 'Cheater':
        mouse.move(1060, 980, absolute=True, duration=0.01)
        mouse.click('left')




fairChance = 0
cheatChance = 0
dominantChance = 0
cunt = 0 
checkGameOver()
while checkGameOver.gameOver == False:
    print('---------------NEW---------------')
    newList = []
    tempList = []
    fairChance = 0
    cheatChance = 0
    dominantChance = 0
    cunt = 0 
    while dominantChance < 80:
        oneFlip()
        time.sleep(0.2)
        #get screenshot and detect text
        im=ImageGrab.grab(bbox=(920,500,1060,560))
        text = pytesseract.image_to_string(im, lang="eng")
        #filter text
        text = [int(s) for s in text.split() if s.isdigit()]
        text = list(map(str, text))
        score = '.'.join(text)
        # print(score)

        if cunt == 0:
            for item in totalList:
                if score in item:
                    newList.append(item)
            # print('first len:  ', len(newList))
            # print(newList)
        else:
            for item in newList:
                if score in item:
                    tempList.append(item)
            newList = tempList
            # print('second len:  ', len(newList))
            tempList = []
        time.sleep(0.4)

        chance = 1 / len(newList) * 100

        fairCount = 0
        cheatCount = 0
        for i in newList:
            if i in fairList:
                fairCount += 1
            if i in cheatList:
                cheatCount += 1

        # print(fairCount, cheatCount, len(newList))
        fairChance = fairCount / len(newList) * 100
        cheatChance = cheatCount / len(newList) * 100
        if fairChance > cheatChance:
            dominantChance = fairChance
            dominantText = 'Fair'
        else:
            dominantChance = cheatChance
            dominantText = 'Cheater'
        # print(fairChance, cheatChance)

        # print(len(newList))
        # print(f'Chance of perfect match is {chance}%')
        print(f'Chance of being {dominantText} is {dominantChance}%')
        cunt += 1
    label()
    time.sleep(3)
    checkGameOver()

