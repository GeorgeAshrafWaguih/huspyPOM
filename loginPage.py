from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_id = "username"
        self.password_id = "password"
        self.login_button_class = "radius"

    def enter_username(self, username):
        self.driver.find_element(By.ID, value=self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, value=self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CLASS_NAME, value=self.login_button_class).click()



