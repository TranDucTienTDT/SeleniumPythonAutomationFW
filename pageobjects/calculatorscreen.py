from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorScreen:

    def __init__(self, driver):
        self.driver = driver
        self.calculator_canvas = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[@title='Back to Homepage']")))

        self.iframe = self.driver.find_element_by_xpath("//iframe[@id = 'fullframe']")
        self.action = self.set_action()

    def set_action(self):
        return ActionChains(self.driver)

    def switch_iframe(self):
        self.driver.switch_to.frame(self.iframe)

    def click_position(self, x, y):
        self.action = self.set_action()
        self.action.move_by_offset(x, y).click().perform()
        self.action.reset_actions()

    def validate_canvas_is_present(self):
        assert self.calculator_canvas.is_displayed()

