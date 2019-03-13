from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

#select post for deleting
post_name = "frg"

#select draft for publishing
draft_name = "Automated title with selenium"

#adding title and text for making a new post
new_post_title = "New Post Automated"
new_post_text = "lorem ipsum"

#sending username and password for login
login_username = "dz"
login_password = "ze"


def login(self):
    self.driver.get("http://127.0.0.1:8000/admin/")
    username_field = self.driver.find_element_by_id("id_username")
    username_field.clear()
    username_field.send_keys("simon")
    password_field = self.driver.find_element_by_id("id_password")
    password_field.clear()
    password_field.send_keys("p@ssword")
    login_button = self.driver.find_element_by_xpath("//input[@value='Log in']")
    login_button.click()


def navigate_to_blogsite(self):
    nav_viewsite = self.driver.find_element_by_xpath("//a[text()='View site']")
    nav_viewsite.click()


class Python_Selenium_Tryout2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/student/Documents/djangogirls/chromedriver')


    def test_fail_login(self):
        self.driver.get("http://127.0.0.1:8000/admin/")
        username_field = self.driver.find_element_by_id("id_username")
        username_field.clear()
        username_field.send_keys(login_username)
        password_field = self.driver.find_element_by_id("id_password")
        password_field.clear()
        password_field.send_keys(login_password)
        login_button = self.driver.find_element_by_xpath("//input[@value='Log in']")
        login_button.click()
        assert self.driver.find_element_by_class_name("errornote")

        """
    def test_Full_Title(self):
        self.driver.get("http://127.0.0.1:8000/")
        assert "list" in self.driver.title

    def test_Full_Title_False(self):
        self.driver.get("http://127.0.0.1:8000/")
        assert "Not_the_Title" in self.driver.title

    def test_Click_on_Post_Shows_Post_Details(self):
        self.driver.get("http://127.0.0.1:8000/")
        elements = self.driver.find_elements_by_id("post")
        print(len(elements))
        elements[0].click()
        assert "post_details" in self.driver.title

        """
        """
    def test_Make_new_Post(self):
        login(self)
        navigate_to_blogsite(self)
        new = self.driver.find_element_by_id("new post")
        new.click()
        title_Field = self.driver.find_element_by_id("id_title")
        text_Field = self.driver.find_element_by_id("id_text")
        title_Field.clear()
        text_Field.clear()
        title_Field.send_keys(new_post_title)
        text_Field.send_keys(new_post_text)
        save_button = self.driver.find_element_by_id("save")
        save_button.click()

    def test_publish_Post(self):
        login(self)
        navigate_to_blogsite(self)
        draft_button = self.driver.find_element_by_id("drafts")
        draft_button.click()
        element = self.driver.find_element_by_xpath("//a[text()='" + draft_name + "']")
        element.click()
        publish_button = self.driver.find_element_by_xpath("//a[text()='Publish']")
        publish_button.click()

    def test_Delete_1st_Post(self):
        login(self)
        navigate_to_blogsite(self)
        elements = self.driver.find_elements_by_id("post")
        elements[0].click()
        delete_Button = self.driver.find_element_by_id("delete")
        delete_Button.click()

    def test_Delete_specified_Post(self):
        login(self)
        navigate_to_blogsite(self)
        element = self.driver.find_element_by_xpath("//a[@id='post'][text()='" + post_name + "']")
        element.click()
        delete_Button = self.driver.find_element_by_id("delete")
        delete_Button.click()

        """


    def tearDown(self):
        self.driver.close()




if __name__ == '__main__':
    unittest.main()
