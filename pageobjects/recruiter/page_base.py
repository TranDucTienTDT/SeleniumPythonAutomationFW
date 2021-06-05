from selenium.webdriver.common.keys import Keys

from common.element import BasePageElement
from common.locators import HeaderLocators, LoginPageLocators


class Elements(BasePageElement):
    """This class gets the search text from the specified locator"""

    pass


class BasePage(object):
    """Base class to initialize the base page that will be called from all Recruiter pages"""

    def __init__(self, driver):
        self.driver = driver


class Header(BasePage):
    """Header of Recruiter pages"""

    def __init__(self, driver):
        super().__init__(driver)
        self.lang_selector_dropdown = BasePageElement().set_element(self.driver, HeaderLocators.LANG_SELECTOR)
        self.user_avatar = BasePageElement().set_element(self.driver, HeaderLocators.USER_AVATAR)

    def verify_user_avatar_is_displayed(self):
        return self.user_avatar.is_displayed()


class LoginPage(BasePage):
    """Login Recruiter page action methods come here"""

    def __init__(self, driver):
        super().__init__(driver)
        self.signup_btn = BasePageElement().set_element(self.driver, LoginPageLocators.SIGNUP_BTN)
        self.password_txt = BasePageElement().set_element(self.driver, LoginPageLocators.PASSWORD_TXT)
        self.username_txt = BasePageElement().set_element(self.driver, LoginPageLocators.USERNAME_TXT)

    def login(self, username, password):
        self.username_txt.send_keys(username + Keys.TAB)
        self.password_txt.send_keys(password + Keys.ENTER)
        return Header(self.driver)

    def go_to_kyc(self):
        self.signup_btn.click()
        return KycPage(self.driver)


class KycPage(BasePage):
    """Home page action methods come here. This is default Jobs Page"""
    pass
