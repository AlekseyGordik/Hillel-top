import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
def test_3():
    assert 5%2 == 1

options = Options()
# options.add_argument("start-maximized"); # open Browser in maximized mode
# options.add_argument("disable-infobars"); # disabling infobars
# options.add_argument("--disable-extensions"); # disabling extensions
# options.add_argument("--disable-gpu"); # applicable to windows os only
# options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
options.add_argument("--no-sandbox")
# options.add_argument("headless")

# START DRIVER
# driver = webdriver.Chrome('/home/dima/Завантаження/Hillel/chromedriver', options=options)
driver = webdriver.Chrome(service=Service("С:\\chromedriver.exe, options=options") )

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.python.org/")

 # assert "Python1" in driver.title # Test fail
time.sleep(2) #sleep for 2 sec

assert "Welcome to Python" in driver.title

