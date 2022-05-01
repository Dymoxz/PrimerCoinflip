import json
import time
import mouse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://www.primerlearning.org")
driver.execute_script("window.scrollTo(0, 1080)") 

time.sleep(2)

import pyautogui
pyautogui.moveTo(1290, 810)