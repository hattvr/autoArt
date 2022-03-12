import configparser, time, warnings, os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import wait
from selenium.webdriver.support.expected_conditions import element_located_selection_state_to_be, presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from configparser import ConfigParser

# Read config file and grab username/password
config = ConfigParser()
config.read('config.ini')
username = config.get('data','username')
password = config.get('data','password')
migrated = config.get('data','migrated')
sq = config.get('data','sq')

# Disable python logging to console
warnings.filterwarnings("ignore")
clear = lambda: os.system('cls')
clear()
# Setup web-driver
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--hide-scrollbars')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--log-level=3')
options.add_argument('--disable-infobars')
options.add_argument('--start-maximized')
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
clear()