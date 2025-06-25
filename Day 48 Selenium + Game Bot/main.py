from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

CAPTCHA_TEXT = ("Sorry, we just need to make sure you're not a robot."
                " For best results, please make sure your browser is accepting cookies.")
captcha = True
while captcha:
    driver.get('https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6')
    if driver.find_element(By.CLASS_NAME, value='a-last').text != CAPTCHA_TEXT:
        captcha = False

dollar_price = driver.find_element(By.CLASS_NAME, value='a-price-whole')
cent_price = driver.find_element(By.CLASS_NAME, value='a-price-fraction')

print(f'It costs {dollar_price.text}.{cent_price.text}')
driver.quit()
