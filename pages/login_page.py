import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.XPATH, "//button[text()='Sign In']")
    sms_panel_text = (By.XPATH, "//div//span[text()='SMS Panel']")

    # Actions
    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username_input))
        self.driver.find_element(By.ID, "username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    # Business Flow
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        time.sleep(5)
        self.click_login()


    # Validation Helper
    def is_login_successful(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.sms_panel_text))
            return True
        except:
            return False