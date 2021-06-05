import time
import unittest

from common.webdriver import Driver


class TestBase(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate('https://sandbox-recruiter.jobhopin.com/login')
        self.driver.instance.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(5)
        self.driver.instance.quit()
