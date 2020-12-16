import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', executable_path='/usr/bin/google-chrome', service_args=['--verbose', '--log-path=./selenium.log'])

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8001/admin-dev")
        current_url = driver.current_url
        login = driver.find_element_by_id("email")
        login.clear()
        login.send_keys("demo@prestashop.com")
        passwd = driver.find_element_by_id("passwd")
        passwd.clear()
        passwd.send_keys("prestashop_demo")
        submit = driver.find_element_by_id("submit_login")
        submit.click()
        WebDriverWait(driver, 15).until(EC.url_changes(current_url))
        self.assertIn("Dashboard", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
