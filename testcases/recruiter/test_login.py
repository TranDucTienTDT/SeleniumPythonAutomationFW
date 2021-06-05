import unittest

from pageobjects.recruiter import page_base
from pageobjects.recruiter.loginpage import LoginPage
from pageobjects.recruiter.header import Header
from testcases.recruiter.test_base import TestBase


class TestLogin(TestBase):

    def test_login_success(self):
        login_page = page_base.LoginPage(self.driver)
        assert login_page.login("tien1@mailinator.com", "123456") \
            .verify_user_avatar_is_displayed()


if __name__ == '__main__':
    unittest.main()
