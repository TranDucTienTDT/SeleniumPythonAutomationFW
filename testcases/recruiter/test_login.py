import unittest

from pageobjects.recruiter.loginpage import LoginPage
from pageobjects.recruiter.header import Header
from testcases.recruiter.test_base import TestBase


class TestLogin(TestBase):

    def test_login_success(self):
        loginPage = LoginPage(self.driver)
        assert loginPage.login("tien1@mailinator.com", "123456") \
            .verify_user_avatar_is_displayed()


if __name__ == '__main__':
    unittest.main()
