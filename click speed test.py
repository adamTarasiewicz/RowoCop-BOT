from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://clickspeedtest.com/")
driver.maximize_window()

clicker = driver.find_element(By.ID, "clicker")
x = driver.find_element(By.XPATH, "//*[@id='speedModal']/div/div/div[1]/button")
accept_cookies = driver.find_element(By.ID, "ez-accept-all")
clicks_counter = driver.find_element(By.ID, "clicks")

driver.implicitly_wait(20)

if accept_cookies.is_displayed():
    accept_cookies.click()

while True:
    clicker.click()
    if x.is_displayed():
        x.click()
