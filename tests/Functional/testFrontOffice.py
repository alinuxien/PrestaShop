import os
import xmlrunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PrestaShopFrontOffice(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

    def testHomepage(self):
        driver = self.driver
        driver.get(os.getenv('SRV_QA'))
        self.assertIn("PrestaShop", driver.title)
    
    def testCategories(self):
        driver = self.driver
        driver.get(os.getenv('SRV_QA'))
        cats = driver.find_elements_by_class_name('category')
        self.assertTrue(cats)

    def testNavigateToCategory(self):
        driver = self.driver
        driver.get(os.getenv('SRV_QA'))
        cat_content = driver.find_element_by_css_selector('#category-3 > .dropdown-item').click()
        self.assertIn("Clothes", driver.title)

    def testNavigateToProduct(self):
        driver = self.driver
        driver.get(os.getenv('SRV_QA'))
        product = driver.find_element_by_partial_link_text('Hummingbird Printed T-Shirt').click()
        self.assertIn("Hummingbird printed t-shirt", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
