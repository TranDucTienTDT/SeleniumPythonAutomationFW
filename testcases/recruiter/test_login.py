import unittest

from pageobjects.recruiter.page_base import LoginPage
from testcases.recruiter.test_base import TestBase


class TestLogin(TestBase):

    def test_login_success(self):
        login_page = LoginPage(self.driver)
        assert login_page.login("tien1@mailinator.com", "123456") \
            .verify_user_avatar_is_displayed()


if __name__ == '__main__':
    unittest.main()
