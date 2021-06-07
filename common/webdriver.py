from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


class Driver:
    """This class manage the web driver"""

    def __init__(self, browser):
        if browser == 'chrome':
            self.instance = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == 'chromium':
            self.instance = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        elif browser == 'firefox':
            self.instance = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == 'ie':
            self.instance = webdriver.Ie(IEDriverManager().install())
        elif browser == 'edge':
            self.instance = webdriver.Edge(EdgeChromiumDriverManager().install())
        elif browser == 'opera':
            self.instance = webdriver.Opera(executable_path=OperaDriverManager().install())
        elif browser == 'safari':
            self.instance = webdriver.Safari()
        elif browser == 'phantom':
            self.instance = webdriver.PhantomJS()
        else:
            raise TypeError("Browser is not supported yet.")

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")

    def maximize_window(self):
        self.instance.maximize_window()

    def find_element(self, by):
        self.instance.find_element(by)
