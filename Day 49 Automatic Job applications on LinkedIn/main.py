from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

EMAIL = "shumpy0808@gmail.com"
PASSWORD = "darbhanga@08"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3898787404&f_AL=true&f_"
           "WT=2&geoId=102713980&keywords=python%20developer&location=India&origin="
           "JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

sign = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')

sign.click()

email_input = driver.find_element(By.XPATH, value='//*[@id="username"]')
email_input.send_keys(EMAIL)
pass_input = driver.find_element(By.XPATH, value='//*[@id="password"]')
pass_input.send_keys(PASSWORD)
enter_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
enter_button.click()
job = driver.find_element(By.XPATH, value='//*[@id="ember207"]/div/div')
job.click()
sleep(30)
easy_apply = driver.find_element(By.XPATH,
                                 value='/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]'
                                       '/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button/span')
easy_apply.click()
