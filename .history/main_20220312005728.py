# Minecraft NameMC Art Uploader
import importlib
importlib.import_module('setup.py')

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