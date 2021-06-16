from selenium.webdriver.common.keys import Keys

from common.element import BasePageElement
from common.locators import HeaderLocators, LoginPageLocators, KycPageLocators


class Elements(BasePageElement):
    """This class gets the search text from the specified locator"""

    pass


class BasePage(object):
    """Base class to initialize the base page that will be called from all Recruiter pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. This is default Jobs Page"""
    pass


class Header(BasePage):
    """Header of Recruiter pages"""

    def __init__(self, driver):
        super().__init__(driver)
        self.lang_selsctor_dropdown = BasePageElement().__set__(self.driver, HeaderLocators.LANG_SELECTOR)
        self.user_avatar = BasePageElement().__set__(self.driver, HeaderLocators.USER_AVATAR)

    def verify_user_avatar_is_displayed(self):
        return self.user_avatar.is_displayed()


class LoginPage(BasePage):
    """Login Recruiter page action methods come here"""

    def __init__(self, driver):
        super().__init__(driver)
        self.signup_btn = BasePageElement().__set__(self.driver, LoginPageLocators.SIGNUP_BTN)
        self.password_txt = BasePageElement().__set__(self.driver, LoginPageLocators.PASSWORD_TXT)
        self.username_txt = BasePageElement().__set__(self.driver, LoginPageLocators.USERNAME_TXT)

    def login(self, username, password):
        self.username_txt.send_keys(username + Keys.TAB)
        self.password_txt.send_keys(password + Keys.ENTER)
        return Header(self.driver)

    def go_to_kyc(self):
        self.signup_btn.click()
        # return KycPage(self.driver)


class KycJobDescriptionPage(BasePage):
    """Know Your Customer (KYC) page action methods come here"""

    def __init__(self, driver):
        super().__init__(driver)
        self.job_title_txt = BasePageElement().__set__(self.driver, KycPageLocators.JOB_TITLE_TXT)
        self.location_txt = BasePageElement().__set__(self.driver, KycPageLocators.LOCATION_TXT)
        self.level_dropdown = BasePageElement().__set__(self.driver, KycPageLocators.LEVEL_DROPDOWN)
        self.industry_dropdown = BasePageElement().__set__(self.driver, KycPageLocators.INDUSTRY_DROPDOWN)
        self.employment_type_dropdown = BasePageElement().__set__(self.driver, KycPageLocators.EMPLOYMENT_TYPE_DROPDOWN)
        self.job_description_rtxt = BasePageElement().__set__(self.driver, KycPageLocators.JOB_DESCRIPTION_RTXT)
        self.job_requirements_rtxt = BasePageElement().__set__(self.driver, KycPageLocators.JOB_REQUIREMENTS_RTXT)
        self.benefits_insurance_chkbox = BasePageElement().__set__(self.driver, KycPageLocators.BENEFITS_INSURANCE_CHKBOX)
        self.benefits_bonus_chkbox = BasePageElement().__set__(self.driver, KycPageLocators.BENEFITS_BONUS_CHKBOX)
        self.benefits_paid_leave_chkbox = BasePageElement().__set__(self.driver, KycPageLocators.BENEFITS_PAID_LEAVE_CHKBOX)
        self.benefits_travel_chkbox = BasePageElement().__set__(self.driver, KycPageLocators.BENEFITS_TRAVEL_CHKBOX)

        self.next_btn = BasePageElement().__set__(self.driver, KycPageLocators.NEXT_BTN)

    def fill_in_job_description(self, job_title, location):
        """Input form 01. Job description."""
        self.job_title_txt.send_keys(job_title + Keys.TAB)
        self.location_txt.send_keys(location + Keys.TAB)
        self.level_dropdown.click()

        return KycBusinessInfoPage(self.driver)


class KycBusinessInfoPage(BasePage):
    """Know Your Customer (KYC) page action methods come here"""

    def __init__(self, driver):
        super().__init__(driver)
        self.company_name_txt = BasePageElement().__set__(self.driver, KycPageLocators.COMPANY_NAME_TXT)
        self.company_size_dropdown = BasePageElement().__set__(self.driver, KycPageLocators.COMPANY_SIZE_DROPDOWN)
        self.headcount_number_dropdown = BasePageElement().__set__(self.driver, KycPageLocators.HEADCOUNT_NUMBER_DROPDOWN)
        self.recruiter_job_title_dropdown = BasePageElement().__set__(self.driver, KycPageLocators.RECRUITER_JOB_TITLE_DROPDOWN)
        self.know_about_us_dropdown = BasePageElement().__set__(self.driver, KycPageLocators.KNOW_ABOUT_US_DROPDOWN)
        self.next_btn = BasePageElement().__set__(self.driver, KycPageLocators.NEXT_BTN)
        self.back_btn = BasePageElement().__set__(self.driver, KycPageLocators.BACK_BTN)

    def fill_in_business_info(self, job_title, location):
        """Input form 02. Business Info."""

        return KycNewAccountPage(self.driver)

class KycNewAccountPage(BasePage):
    """Know Your Customer (KYC) page action methods come here"""

    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_txt = BasePageElement().__set__(self.driver, KycPageLocators.FIRST_NAME_TXT)
        self.last_name_txt = BasePageElement().__set__(self.driver, KycPageLocators.LAST_NAME_TXT)
        self.email_txt = BasePageElement().__set__(self.driver, KycPageLocators.EMAIL_TXT)
        self.password_txt = BasePageElement().__set__(self.driver, KycPageLocators.PASSWORD_TXT)
        self.mobile_txt = BasePageElement().__set__(self.driver, KycPageLocators.MOBILE_TXT)
        self.term_of_use_chkbox = BasePageElement().__set__(self.driver, KycPageLocators.TERM_OF_USE_CHKBOX)
        self.subcribe_chkbox = BasePageElement().__set__(self.driver, KycPageLocators.SUBSCRIBE_CHKBOX)
        self.finish_btn = BasePageElement().__set__(self.driver, KycPageLocators.NEXT_BTN)
        self.back_btn = BasePageElement().__set__(self.driver, KycPageLocators.BACK_BTN)
