from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    """This class manage the web driver"""
    def __init__(self):
        self.instance = webdriver.Chrome(ChromeDriverManager().install())

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")

    def maximize_window(self):
        self.instance.maximize_window()


