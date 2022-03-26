from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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

zatrudnij_pracownika = 0
kupno_koparki = 500000


def koszty(self):
    if self.is_displayed():
        self.click()


if __name__ == '__main__':
    for i in range(0, 1000000000000000000):
        kop.click()
        koszty(ceidk1)
        koszty(ksiazka1)
        koszty(ksiazka2)
        koszty(asystentka)
        koszty(motywacja)
        koszty(szkolenie)

        if int(month.text) * 4 > zatrudnij_pracownika:
            koszty(pracownik)
            zatrudnij_pracownika += 1

        koszty(kierownik)
        koszty(coach)

        if int(kasa.text) > kupno_koparki:
            koszty(koparka)
            kupno_koparki += 100000
