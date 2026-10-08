from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# TODO:
# move credentials to environment variables

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

driver = webdriver.Chrome()

driver.get("https://social.example.com/login")

driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

time.sleep(10)
driver.quit()
