from selenium.webdriver.common.by import By


class HeaderLocators(object):
    """A class for header locators. All header locators should come here"""

    LANG_SELECTOR = (By.XPATH, "//div[@id='lang-selector-dropdown']")
    VI_LANG_ICON = (By.XPATH, "//li[1]")
    EN_LANG_ICON = (By.XPATH, "//li[2]")
    USER_AVATAR = (By.XPATH, "//div[@id='user-avatar']")


class LoginPageLocators(object):
    """A class for login page locators. All login page locators should come here"""

    USERNAME_TXT = (By.XPATH, "//input[@type='email']")
    PASSWORD_TXT = (By.XPATH, "//input[@type='password']")
    SIGNUP_BTN = (By.CSS_SELECTOR, ".sign-up")

class KycPageLocators(object):
    """A class for KYC page locators. All KYC page locators should come here"""

    pass
