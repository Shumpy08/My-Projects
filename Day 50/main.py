import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import config


FACEBOOK_URL = "https://www.facebook.com/"
TINDER_URL = "https://tinder.com/"
DAILY_LIMIT = 100


def facebook_login():
    """Logs in to Facebook."""
    driver.get(url=FACEBOOK_URL)
    time.sleep(2)
    driver.find_element_by_id("u_0_h").click()
    driver.find_element_by_id("email").send_keys(config.FACEBOOK_EMAIL)
    driver.find_element_by_id("pass").send_keys(config.FACEBOOK_PASS)
    driver.find_element_by_id("pass").submit()


def tinder_login():
    driver.get(url=TINDER_URL)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/'
                                 'header/div/div[2]/div[2]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
    time.sleep(1)

    try:
        driver.find_element_by_xpath('//*[@id="u_0_4"]/div[2]/div[2]/div[1]/button').click()
    except NoSuchElementException:
        pass
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()
    time.sleep(2)

    try:
        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]').click()
    except NoSuchElementException:
        pass


def swipe(swipe_right=False):
    """Swipes left unless "swipe_right=True" is specified."""
    nav = driver.find_element_by_id("Tinder")
    if swipe_right:
        nav.send_keys(Keys.RIGHT)
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[4]/button').click()
        except NoSuchElementException:
            pass
        else:
            time.sleep(1)
    else:
        nav.send_keys(Keys.LEFT)


driver = webdriver.Chrome()
facebook_login()
time.sleep(5)
tinder_login()
time.sleep(2)

for _ in range(DAILY_LIMIT):
    swipe()
    time.sleep(1)

driver.close()