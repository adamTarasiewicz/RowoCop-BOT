import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://seleniumdemo.com")
driver.maximize_window()

# XPath = //tagname[@Attribute=’Value’]

class testLoginPage(unittest.TestCase):

    def test_login_succesful_pass(self):
        login = driver.find_element(By.ID, "menu-item-22")
        login.click()
        username = driver.find_element(By.ID, "username")
        username.send_keys("demotest@gmail.com")
        password = driver.find_element(By.ID, "password")
        password.send_keys("hasloHaslo123")
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()

        # verify
        my_account_is_visible = driver.find_element(By.XPATH, "//h1[@class='entry-title']")
        self.assertTrue(my_account_is_visible, 'My account')

        logout = driver.find_element(By.LINK_TEXT, "Logout")
        logout.click()


    def test_login_unsuccesful_pass(self):
        username = driver.find_element(By.ID, "username")
        username.send_keys("1111")
        password = driver.find_element(By.ID, "password")
        password.send_keys("1111")
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()

        # verify
        failed_login = driver.find_element(By.CLASS_NAME, "woocommerce-notices-wrapper")
        self.assertTrue(failed_login, 'ERROR')



if __name__ == "__main__":
    unittest.main()

# demotest@gmail.com
# hasloHaslo123
# https://www.lambdatest.com/blog/complete-guide-for-using-xpath-in-selenium-with-examples/