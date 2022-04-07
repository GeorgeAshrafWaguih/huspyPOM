from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPage
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="/Users/georgeashraf/bin/chromedriver")

    def test_login(self):
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/login')

        login = LoginPage
        login.enter_username("tomsmith")
        login.enter_password("SuperSecretPassword!")
        login.click_login()

        if driver.current_url == "https://the-internet.herokuapp.com/secure":
            print("login passed")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()




