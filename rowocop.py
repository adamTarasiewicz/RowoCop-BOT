from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://system.mrugalski.pl/")
driver.maximize_window()

zaczynamy = driver.find_element(By.ID, "go")
zaczynamy.click()

kop = driver.find_element(By.ID, "kop")

ceidk1 = driver.find_element(By.ID, "ceidk")
ksiazka1 = driver.find_element(By.ID, "ksiazka1")
ksiazka2 = driver.find_element(By.ID, "ksiazka2")
asystentka = driver.find_element(By.ID, "asystentka")
motywacja = driver.find_element(By.ID, "motywacja")
szkolenie = driver.find_element(By.ID, "szkolenie")
pracownik = driver.find_element(By.ID, "pracownik")
kierownik = driver.find_element(By.ID, "kierownik")
koparka = driver.find_element(By.ID, "koparka")
coach = driver.find_element(By.ID, "coach")
kasa = driver.find_element(By.XPATH, "//*[@id='kasa']/b")
month = driver.find_element(By.XPATH, "//*[@id='ilem']/b")

workerNumbers = 4
boughtWorkers = 0

superKwota = 500000


def ww(self=WebElement):
    if self.is_displayed():
        self.click()


if __name__ == '__main__':
    for i in range(0, 1000000000000000000):
        kop.click()
        ww(ceidk1)
        ww(ksiazka1)
        ww(ksiazka2)
        ww(asystentka)
        ww(motywacja)
        ww(szkolenie)

        if int(month.text) * 4 > boughtWorkers:
            ww(pracownik)
            boughtWorkers = boughtWorkers + 1

        ww(kierownik)
        ww(coach)

        if int(kasa.text) > superKwota:
            ww(koparka)
            superKwota += 100000
