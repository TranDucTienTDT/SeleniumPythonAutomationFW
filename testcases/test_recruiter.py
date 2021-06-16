import time
import unittest
from pageobjects.recruiter.header import Header
from common.webdriver import Driver


class TestQABoy(unittest.TestCase):

    def setUp(self):
        self.driver = Driver('chrome')
        self.driver.navigate('https://sandbox-recruiter.jobhopin.com/login')
        self.driver.maximize_window()

    def test_recruiter(self):
        header = Header(self.driver)
        header.change_language('EN')

    def tearDown(self):
        time.sleep(10)
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()