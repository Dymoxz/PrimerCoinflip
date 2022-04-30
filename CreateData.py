import mouse
import time
from PIL import Image
import pytesseract
import pyscreenshot as ImageGrab
import time
import cv2 
import numpy as np
import json

time.sleep(2)


def CheckFlipsRemaining():
	time.sleep(1)
	im=ImageGrab.grab(bbox=(1030,800,1180,830))
	text = pytesseract.image_to_string(im, lang="eng")
	#filter text
	text = [int(s) for s in text.split() if s.isdigit()]
	text = text[0]
	flipsRemaining = text
	print('remain:   ', flipsRemaining)
	if flipsRemaining >= 15:
		CheckFlipsRemaining.totalFlips = 15
	else:
		CheckFlipsRemaining.totalFlips = flipsRemaining

def oneFlip():
	mouse.move(840, 860, absolute=True, duration=0.01)
	mouse.click('left')

def label():
	mouse.move(840, 980, absolute=True, duration=0.01)
	mouse.click('left')
	time.sleep(0.91)
	im=ImageGrab.grab(bbox=(930,480,980,530))

	im = im.convert("RGB")
	pixels = [i for i in im.getdata()]

	fair = (122,162,100) in pixels

	if fair == True:
		with open('test.json', 'r+') as f:
			data = json.load(f)
			List = data["Fair"]
			if tempSeq not in List:
				List.append(tempSeq)
			data["Fair"] = List
			f.seek(0)
			json.dump(data, f, indent=4)
			f.truncate()
	else:
		with open('test.json', 'r+') as f:
			data = json.load(f)
			List = data["Cheater"]
			if tempSeq not in List:
				List.append(tempSeq)
			data["Cheater"] = List
			f.seek(0)
			json.dump(data, f, indent=4)
			f.truncate()

def checkGameOver():
	im=ImageGrab.grab(bbox=(840,960,1060,1000))
	text = pytesseract.image_to_string(im, lang="eng")
	print(text)
	if 'Reset game' in text:
		mouse.move(960, 980, absolute=True, duration=0.01)
		mouse.click('left')
	


for i in range(10):
	tempSeq = []
	CheckFlipsRemaining()
	for i in range(CheckFlipsRemaining.totalFlips):
		oneFlip()
		#get screenshot and detect text
		im=ImageGrab.grab(bbox=(920,500,1060,560))
		text = pytesseract.image_to_string(im, lang="eng")
		#filter text
		text = [int(s) for s in text.split() if s.isdigit()]
		text = list(map(str, text))
		score = '.'.join(text)
		print(score)
		tempSeq.append(score)
	print(tempSeq)
	label()
	time.sleep(2.4)
	checkGameOver()
	time.sleep(0.2)


