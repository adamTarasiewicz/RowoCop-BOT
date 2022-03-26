from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://cpstest.net/kohi-click-test/")
driver.maximize_window()

driver.implicitly_wait(20)

start = driver.find_element(By.ID, "start")

while True:
    start.click()
