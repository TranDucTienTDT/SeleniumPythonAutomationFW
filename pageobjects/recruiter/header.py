from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Header:

    def __init__(self, driver):
        self.driver = driver
        self.lang_selector_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='lang-selector-dropdown']")))
        self.display_lang = ""
        self.user_avatar = ""

    def change_language(self, lang):
        self.lang_selector_dropdown.click()
        if lang == 'VI':
            self.display_lang = WebDriverWait(self.driver.instance, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//li[1]")))
        elif lang == 'EN':
            self.display_lang = WebDriverWait(self.driver.instance, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//li[2]")))
        self.display_lang.click()

    def verify_user_avatar_is_displayed(self):
        self.user_avatar = WebDriverWait(self.driver.instance, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='user-avatar']")))
        return self.user_avatar.isDisplayed()