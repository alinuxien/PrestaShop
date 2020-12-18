import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PrestaShopFrontOffice(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

    def test_homepage(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8001")
        self.assertIn("PrestaShop", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner()
                  
