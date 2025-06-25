from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Shumpy")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("S")
email = driver.find_element(By.NAME, "email")
email.send_keys("codenigga2000@gmail.com")

enter = driver.find_element(By.XPATH, "/html/body/form/button")
enter.send_keys(Keys.ENTER)