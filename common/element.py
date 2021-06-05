from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""
    wait_time = 10
    element = ""

    def set_element(self, driver, locator):
        """Sets the element to the value supplied"""

        self.driver = driver
        return WebDriverWait(self.driver.instance, self.wait_time).until(EC.visibility_of_element_located(locator))

    def get_element(self):
        """Gets the text of the specified object"""
        pass
