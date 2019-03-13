
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class Python_Selenium_Tryout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/student/Documents/djangogirls/chromedriver')
        self.driver.get("http://127.0.0.1:8000/")

    def test_Title(self):
        assert "Django" in self.driver.title

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
