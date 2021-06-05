import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.calculatorscreen import CalculatorScreen
from PIL import Image
import pytesseract


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.online-calculator.com/full-screen-calculator/")
        self.driver.maximize_window()
        self.x = self.driver.get_window_rect()["x"]
        self.y = self.driver.get_window_rect()["y"]
        self.w = self.driver.get_window_rect()["width"]
        self.h = self.driver.get_window_rect()["height"]
        print(self.x, self.y, self.w, self.h)

    def test_calculator_screen(self):
        calculatorScreen = CalculatorScreen(self.driver)
        calculatorScreen.click_position(self.w / 2, self.h / 2)
        calculatorScreen.click_position(self.w / 2 + 100, self.h / 2)
        calculatorScreen.click_position(self.w / 2 - 100, self.h / 2)
        calculatorScreen.click_position(self.w / 2 + 250, self.h / 2 + 150)
        self.driver.save_screenshot('test.png')
        test_image = Image.open('test.png')
        print(pytesseract.image_to_string(test_image))
        #source_img = Image.open('full.png')

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
