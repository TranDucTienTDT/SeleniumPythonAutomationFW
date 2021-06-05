from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.recruiter.header import Header


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_txt = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//input[@type='email']")))
        self.password_txt = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//input[@type='password']")))

        self.signup_btn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, ".sign-up")))

    def login(self, username, password):
        self.username_txt.send_keys(username + Keys.TAB)
        self.password_txt.send_keys(password + Keys.ENTER)
        return Header(self.driver)

    def go_to_kyc(self):
        self.signup_btn.click()
