from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Option to keep Chrome open

# Specify path to Chrome User Data Folder
options.add_argument(r'--user-data-dir=C:\Users\Shubham Sundaram\AppData\Local\Google\Chrome\User Data')
# This creates the new user I have called SeleniumProfile
options.add_argument('--profile-directory=SeleniumProfile')

driver = webdriver.Chrome(options=options)