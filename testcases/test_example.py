import time
import unittest

from webdriver import Driver


class TestQABoy(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_home_screen_components(self):
        Map_coordinates = dict({
            "latitude": 10.776494822918954,
            "longitude": 106.71232523014088,
            "accuracy": 100
        })
        Map_coordinates1 = dict({
            "latitude": 10.782607741906473,
            "longitude": 106.71880544672644,
            "accuracy": 100
        })
        self.driver.instance.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)

        self.driver.navigate("https://www.google.com/maps")
        self.driver.instance.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates1)
        self.driver.maximize_window()
        time.sleep(10)

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()