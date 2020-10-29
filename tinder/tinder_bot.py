from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#python3 -i tinder_bot.py

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"/Users/vr/Desktop/tinder/chromedriver")

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(6)

        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type = 'button' and @aria-label = 'Log in with Facebook']//span"))).click()

        # switch to login popup
        base_window = bot.driver.window_handles[0]
        bot.driver.switch_to_window(self.driver.window_handles[1])

        email_in = bot.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys("rvasiliev30@gmail.com")

        pw_in = bot.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys("capitanmarvel96")

         

        popup_1 = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[3]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[3]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button/span/svg/path')
        like_btn.click()

    def dislike(self):
        dislike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                like_btn.click()
            except Exception:
                try:
                    bot.close_popup()
                except Exception:
                    bot.close_match()

    

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


