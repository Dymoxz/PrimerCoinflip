import pyscreenshot as ImageGrab
import pytesseract
import time
import mouse
time.sleep(2)

def oneFlip():
	mouse.move(840, 860, absolute=True, duration=0.01)
	mouse.click('left')

def checkGameOver():
    im=ImageGrab.grab(bbox=(840,960,1060,1000))
    text = pytesseract.image_to_string(im, lang="eng")
    # print(text)
    if 'Reset game' in text:
        checkGameOver.gameOver = True

for i in range(18):
    oneFlip()

mouse.move(840, 980, absolute=True, duration=0.01)
mouse.click('left')
time.sleep(4)
checkGameOver()

print(checkGameOver.gameOver)