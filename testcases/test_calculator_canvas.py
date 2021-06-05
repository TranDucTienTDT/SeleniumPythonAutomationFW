import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.calculatorscreen import CalculatorScreen


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.online-calculator.com/full-screen-calculator/")
        self.driver.maximize_window()
        self.rect = self.driver.get_window_rect()
        self.x = self.rect['x'] + 530
        self.y = self.rect['y'] + 280
        print(self.x, self.y)
        print(self.driver)


    def test_calculator_screen(self):
        calculatorScreen = CalculatorScreen(self.driver)
        #calculatorScreen.switch_iframe()
        calculatorScreen.validate_canvas_is_present()
        calculatorScreen.click_position(self.x, self.y)
        calculatorScreen.click_position(self.x + 100, self.y)

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
