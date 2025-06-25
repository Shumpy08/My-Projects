from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = "yumemirai744@gmail.com"
TWITTER_PASSWORD = "darbhanga08"
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(options=CHROME_OPTIONS)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url='https://www.speedtest.net/')
        accept_btn = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        accept_btn.click()

    def tweet(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet()
