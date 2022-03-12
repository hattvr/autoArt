# Minecraft NameMC Art Uploader
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

# TODO
# - Clean up config file to make settings thread urls and comments more user friendly

class User:
    def login(self):
        if (migrated == False):
            print("[+] Attempting to login...")
            browser.get('https://www.minecraft.net/en-us/profile/skin')
            time.sleep(5)
            browser.find_element_by_name('emailField').send_keys(username)
            browser.find_element_by_name('password').send_keys(password)
            browser.find_element_by_xpath('//*[@id="CoreAppsApp"]/main/div/div/div/div/div[1]/div[2]/form/button').click()
            print("[!] Please complete the captcha if there is one available!")
            wait = WebDriverWait(browser, 300)
            wait.until(presence_of_element_located((By.XPATH, '//*[@id="profiledd1Button"]')))
            try:
                if presence_of_element_located((By.XPATH, '//*[@id="CoreAppsApp"]/main/div/div/div/div/div/div/div/div/h1')):
                    answers = config['data']['sq'].split(',')
                    browser.find_element_by_xpath("(//*[@data-aem-contentname='Input'])[1]").send_keys(answers[0])
                    browser.find_element_by_xpath("(//*[@data-aem-contentname='Input'])[2]").send_keys(answers[1])
                    browser.find_element_by_xpath("(//*[@data-aem-contentname='Input'])[3]").send_keys(answers[2])
                    browser.find_element_by_xpath('//*[@id="CoreAppsApp"]/main/div/div/div/div/div/div/div/div/form/div[4]/button').click()
                    print("[+] Logged in successfully...")
                else:
                    pass
            except Exception as error:
                pass
        else:
            print("[+] Account is migrated! Attempting to login via Microsoft...")
            browser.get('https://www.minecraft.net/en-us/profile/skin')
            time.sleep(3)
            browser.find_element_by_xpath('//*[@id="CoreAppsApp"]/main/div/div/div/div/div[1]/div[1]/div/a').click()
            time.sleep(1)
            browser.find_element_by_name('loginfmt').send_keys(username, Keys.RETURN)
            time.sleep(1)
            browser.find_element_by_name('passwd').send_keys(password, Keys.RETURN)
            time.sleep(1)
            try:
                if presence_of_element_located((By.CLASS_NAME, 'lightbox-cover')):
                    browser.find_element_by_id("idSIButton9").click()
                else:
                    pass
            except Exception as error:
                pass
            print("[+] Logged in successfully...")

    def changeSkin(self):
        time.sleep(3)
        count = 1
        for i in range(27,1,-1):
            try:
                browser.find_element_by_xpath("//*[@id='CoreAppsApp']/main/div/div/div/div/div[2]/div/div[1]/div[2]/div/input").send_keys(f"C://Users/Zaeem/Desktop/Projects/autoArt/skins/Skin-{str(i)}.png")
                time.sleep(2)
                browser.find_element_by_xpath("//*[@id='CoreAppsApp']/main/div/div/div/div/div[2]/div/div[1]/div[2]/div/button[1]").click()
                print(f"[{count}] Successfully uploaded. Uploading next skin in a minute!")
                count += 1
                time.sleep(100)
            except Exception as error:
                print(error)
                time.sleep(30)
        print("[+] NameMC Art Complete!")
                
# Set user details
mc = User()
mc.login()
mc.changeSkin()