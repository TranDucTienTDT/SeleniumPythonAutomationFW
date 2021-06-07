from selenium.webdriver.common.by import By


class HeaderLocators(object):
    """A class for header locators. All header locators should come here"""

    LANG_SELECTOR = (By.XPATH, "//div[@id='lang-selector-dropdown']")
    VI_LANG_ICON = (By.XPATH, "//li[1]")
    EN_LANG_ICON = (By.XPATH, "//li[2]")
    USER_AVATAR = (By.XPATH, "//div[@id='lang-selector-dropdown']")


class LoginPageLocators(object):
    """A class for login page locators. All login page locators should come here"""

    USERNAME_TXT = (By.XPATH, "//input[@type='email']")
    PASSWORD_TXT = (By.XPATH, "//input[@type='password']")
    SIGNUP_BTN = (By.CSS_SELECTOR, ".sign-up")


class KycPageLocators(object):
    """A class for KYC page locators. All KYC page locators should come here"""

    JOB_TITLE_TXT = (By.CSS_SELECTOR, ".job-title>div>div>input")
    LOCATION_TXT = (By.CSS_SELECTOR, ".job-location>div>input")
    LEVEL_DROPDOWN = (By.CSS_SELECTOR, ".job-level>div>div")
    INDUSTRY_DROPDOWN = (By.CSS_SELECTOR, ".job-industry>div>div")
    EMPLOYMENT_TYPE_DROPDOWN = (By.CSS_SELECTOR, ".job-employment-type>div>div")
    JOB_DESCRIPTION_RTXT = (By.CSS_SELECTOR, ".job-description>div>div>.ql-editor")
    JOB_REQUIREMENTS_RTXT = (By.CSS_SELECTOR, ".job-requirement>div>div>.ql-editor")
    BENEFITS_INSURANCE_CHKBOX = (By.XPATH, "//div[@class='job-benefits']//div[@role='presentation'][1]")
    BENEFITS_BONUS_CHKBOX = (By.XPATH, "//div[@class='job-benefits']//div[@role='presentation'][2]")
    BENEFITS_PAID_LEAVE_CHKBOX = (By.XPATH, "//div[@class='job-benefits']//div[@role='presentation'][3]")
    BENEFITS_TRAVEL_CHKBOX = (By.XPATH, "//div[@class='job-benefits']//div[@role='presentation'][4]")
    JOB_KEYWORDS_TXT = (By.CSS_SELECTOR, ".job-keywords>div>input")
    SHOW_SALARY_RANGE_SWITCH = (By.CSS_SELECTOR, ".show-salary-range>.switch")
    MIN_SALARY_TXT = (By.XPATH, "//input[@name='minSalary']")
    MAX_SALARY_TXT = (By.XPATH, "//input[@name='maxSalary']")
    USD_CURRENCY_RD = (By.ID, "salary-usd")
    VND_CURRENCY_RD = (By.ID, "salary-vnd")

    COMPANY_NAME_TXT = (By.CSS_SELECTOR, ".job-working-hour>div>input")
    COMPANY_SIZE_DROPDOWN = (By.CSS_SELECTOR, ".job-company-size>div>div")
    HEADCOUNT_NUMBER_DROPDOWN = (By.CSS_SELECTOR, ".job-level>div>div")
    RECRUITER_JOB_TITLE_DROPDOWN = (By.XPATH, "//div[@class='job-industry']//div[@class='wrapper'][1]")
    KNOW_ABOUT_US_DROPDOWN = (By.XPATH, "//div[@class='job-industry']//div[@class='wrapper'][2]")

    FIRST_NAME_TXT = (By.CSS_SELECTOR, ".first-name>input")
    LAST_NAME_TXT = (By.CSS_SELECTOR, ".last-name>input")
    EMAIL_TXT = (By.CSS_SELECTOR, ".email>div>input")
    PASSWORD_TXT = (By.CSS_SELECTOR, ".password>div>input")
    MOBILE_TXT = (By.CSS_SELECTOR, ".job-working-hour>div>input")
    TERM_OF_USE_CHKBOX = (By.XPATH, "//div[@class='square icon'][1]")
    SUBSCRIBE_CHKBOX = (By.XPATH, "//div[@class='square icon'][2]")
    NEXT_BTN = (By.CSS_SELECTOR, "button.solid.blue.primary-button.button.next")
    BACK_BTN = (By.CSS_SELECTOR, "button.outline.primary-button.button.back")



