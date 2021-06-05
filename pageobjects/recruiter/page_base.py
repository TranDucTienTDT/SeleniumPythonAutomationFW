from selenium.webdriver.common.keys import Keys

from common.element import BasePageElement
from common.locators import MainPageLocators


class Elements(BasePageElement):
    """This class gets the search text from the specified locator"""

    pass


class BasePage(object):
    """Base class to initialize the base page that will be called from all Recruiter pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. This is default Jobs Page"""


class Header(BasePage):
    """Header of Recruiter pages"""


class LoginPage(BasePage):
    """Login Recruiter page action methods come here"""

    def __init__(self, driver):
        super().__init__(driver)
        self.signup_btn = BasePageElement().__set__(self,)
        self.password_txt =
        self.username_txt =

    def login(self, username, password):
        self.username_txt.send_keys(username + Keys.TAB)
        self.password_txt.send_keys(password + Keys.ENTER)
        return Header(self.driver)

    def go_to_kyc(self):
        self.signup_btn.click()
