import time
import unittest
from webdriver import Driver


class TestBase(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate('https://sandbox-recruiter.jobhopin.com/login')
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(10)
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
