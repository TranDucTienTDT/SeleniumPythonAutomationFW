import unittest

from pageobjects.recruiter.page_base import LoginPage, KycPage
from testcases.recruiter.test_base import TestBase


class TestLogin(TestBase):

    def test_signup(self):
        login_page = LoginPage(self.driver)
        login_page.go_to_kyc()
        kyc_page = KycPage(self.driver)
        kyc_page.fill_in('tester', 'hcm')


if __name__ == '__main__':
    unittest.main()
