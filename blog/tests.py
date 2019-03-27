from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest


#adding title and text for making a new post
Global_new_post_title = "New Post Automated"
Global_new_post_text = "lorem ipsum"

#select post for deleting
Global_post_name = "New Post Automated" #specific post to delete

#select draft for publishing
Global_draft_name = "df"

#sending username and password for failing login
Global_failing_login_username = "dz"
Global_failing_login_password = "ze"



def fill_in_field_by_id(self,text,locator_string):
    Field = self.driver.find_element_by_id(locator_string)
    Field.clear()
    Field.send_keys(text)

def Find_xpath(self,string):
    button = self.driver.find_element_by_xpath(string)
    button.click()

def Find_id(self,string):
    button = self.driver.find_element_by_id(string)
    button.click()

def navigate_to_blogsite(self):
    Find_xpath(self,"//a[text()='View site']")

def publish(self,title):
    Find_id(self,"drafts")
    Find_xpath(self,"//a[text()='" + title + "']")
    Find_xpath(self,"//a[text()='Publish']")
    Find_xpath(self,"//a[text()='Django Girls Blog']")

def make_new_post(self):
    Find_id(self,"new post")
    fill_in_field_by_id(self,Global_new_post_title,"id_title")
    fill_in_field_by_id(self,Global_new_post_text,"id_text")
    Find_id(self,"save")

def make_new_post2(self,title,text):
    Find_id(self,"new post")
    fill_in_field_by_id(self,title,"id_title")
    fill_in_field_by_id(self,text,"id_text")
    Find_id(self,"save")
    Find_id(self,"drafts")
    Find_xpath(self,"//a[text()='" + title + "']")
    Find_xpath(self,"//a[text()='Publish']")
    Find_xpath(self,"//a[text()='Django Girls Blog']")

def deleteAllPosts(self):
    posts = self.driver.find_elements_by_id("post")
    count = len(range(len(posts)))
    while count > 0:
        posts[0].click()
        Find_id(self,"delete")
        posts = self.driver.find_elements_by_id("post")
        count = count-1

def add_user(self,username,password):
    Find_xpath(self,"//a[@href='/admin/auth/user/add/']")
    fill_in_field_by_id(self,username,"id_username")
    fill_in_field_by_id(self,password,"id_password1")
    fill_in_field_by_id(self,password,"id_password2")
    Find_xpath(self,"//input[@type='submit'][@name='_save']")
    Find_id(self,"id_is_staff")
    Find_id(self,"id_user_permissions_add_all_link")
    Find_xpath(self,"//input[@type='submit'][@name='_save']")
    Find_xpath(self,"//a[text()='Home']")

def delete_user(self,username):
    Find_xpath(self,"//a[@href='/admin/auth/user/']")
    Find_xpath(self,"//a[text()='" + username + "']")
    Find_xpath(self,"//a[text()='Delete']")
    Find_xpath(self,"//input[@type='submit']")

def login(self,username,password):
    self.driver.get("http://127.0.0.1:8000/admin/")
    fill_in_field_by_id(self,username,"id_username")
    fill_in_field_by_id(self,password,"id_password")
    Find_xpath(self,"//input[@value='Log in']")

def logout(self):
    Find_xpath(self,"//a[text()='Log out']")

def change_password(self,old_password,new_password):
    Find_xpath(self,"//a[text()='Change password']")
    fill_in_field_by_id(self,old_password,"id_old_password")
    fill_in_field_by_id(self,new_password,"id_new_password1")
    fill_in_field_by_id(new_password,"id_new_password2")
    Find_xpath(self,"//input[@value='Change my password']")



#Testcase for logout, addUser & deleteUser op admin page
class Python_Selenium_AdminTests(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome('/Users/student/Documents/djangogirls/chromedriver',chrome_options=options)


        #self.driver = webdriver.Chrome('/Users/student/Documents/djangogirls/chromedriver')

    def test_post_list(self):
        login(self,"simon","p@ssword")
        Find_xpath(self,"//a[text()='Posts']")
        count = self.driver.find_element_by_class_name("paginator")
        count_value = count.text
        button = self.driver.find_element_by_class_name("addlink")
        button.click()
        fill_in_field_by_id(self,"makeNewPostTest","id_title")
        fill_in_field_by_id(self,"lorem ipsum","id_text")
        selector = Select(self.driver.find_element_by_id("id_author"))
        selector.select_by_visible_text("NewUser")
        Find_xpath(self,"//input[@value='Save']")
        count2 = self.driver.find_element_by_class_name("paginator")
        count2_value = count2.text
        assert count_value != count2_value

    def test_change_password(self):
        login(self,"NewUser","TestPassword2")
        change_password(self,"TestPassword2","TestPassword")
        logout(self)
        login(self,"NewUser","TestPassword")
        assert "Site administration | Django site admin" in self.driver.title
        change_password(self,"TestPassword","TestPassword2")

    def test_Title_False(self):
        login(self,"simon","p@ssword")
        assert "Not_the_Title" in self.driver.title

        #log in and logout test
    def test_logout(self):
        login(self,"simon","p@ssword")
        logout(self)
        text = self.driver.find_element_by_xpath("//h1[text()='Logged out']")
        assert text.text == "Logged out"

        #atm works indefinitely after creating the testuser 1 time
        #deletes a user if it already exists and adds it again and tests if it is indeed added through login
    def test_user_bijmaken_met_staff_permissies(self):
        username = "NewUser5"
        password = "TestPassword"
        login(self,"simon","p@ssword")
        delete_user(self,username)
        add_user(self,username,password)
        logout(self)
        login(self,username,password)
        assert "Site administration | Django site admin" in self.driver.title

        #atm only works if testuser doesn't exist yet
        #makes a user and then deletes it and tests if it is indeed deleted through login
    def test_delete_user(self):
        username = "NewUser4"
        password = "TestPassword"
        login(self,"simon","p@ssword")
        add_user(self,username,password)
        delete_user(self,username)
        logout(self)
        login(self,username,password)
        assert self.driver.find_element_by_class_name("errornote")

    def test_make_new_post_adminsite(self):
        login(self,"simon","p@ssword")
        Find_xpath(self,"//a[text()='Posts']")
        assert "Select post to change" in self.driver.title
        button = self.driver.find_element_by_class_name("addlink")
        button.click()
        fill_in_field_by_id(self,"makeNewPostTest","id_title")
        fill_in_field_by_id(self,"lorem ipsum","id_text")
        selector = Select(self.driver.find_element_by_id("id_author"))
        selector.select_by_visible_text("NewUser")
        Find_xpath(self,"//input[@value='Save']")
        assert "Select post to change" in self.driver.title

    def tearDown(self):
        self.driver.close()


        """
class Python_Selenium_AddTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/student/Documents/djangogirls/chromedriver')

    def test_Make_new_Post_fails_when_no_title_or_text(self):
        login(self,"simon","p@ssword")
        navigate_to_blogsite(self)
        Find_id(self,"new post")
        fill_in_field_by_id(self,"","id_title")
        fill_in_field_by_id(self,"","id_text")
        Find_id(self,"save")
        assert "post_details" in self.driver.title

    def test_Make_new_Post(self):
        login(self,"simon","p@ssword")
        navigate_to_blogsite(self)
        make_new_post(self)
        assert "post_details" in self.driver.title
        new_post_name = self.driver.find_element_by_tag_name("h2")
        assert new_post_name.text != ""

    def tearDown(self):
        self.driver.close()

class Python_Selenium_DeleteTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/student/Documents/djangogirls/chromedriver')

    def test_Delete_1st_Post_deletes_first_post(self):
        login(self,"simon","p@ssword")
        navigate_to_blogsite(self)
        deleteAllPosts(self)
        make_new_post2(self,Global_new_post_title,Global_new_post_text)
        make_new_post2(self,"different Title", "other text")
        elements = self.driver.find_elements_by_id("post")
        first_post_before = elements[0]
        elements[0].click()
        Find_id(self,"delete")
        elements = self.driver.find_elements_by_id("post")
        first_post_after = elements[0]
        assert first_post_before != first_post_after


    def test_Delete_specified_Post_deletes_that_post(self):
        login(self,"simon","p@ssword")
        navigate_to_blogsite(self)
        deleteAllPosts(self)
        make_new_post2(self,Global_new_post_title,Global_new_post_text)
        make_new_post2(self,"Specific Title","lorem ipsum")
        Find_xpath(self,"//a[@id='post'][text()='Specific Title']")
        Find_id(self,"delete")
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_xpath("//a[@id='post'][text()='Specific Title']")
        element_after = self.driver.find_element_by_xpath("//a[@id='post'][text()='" + Global_new_post_title + "']")
        assert element_after.text != ""

    def test_geen_delete_wanneer_geen_posts_meer(self):
        login(self,"simon","p@ssword")
        navigate_to_blogsite(self)
        deleteAllPosts(self)
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_xpath("//a[@id='post'][text()='" + Global_post_name + "']")


    def tearDown(self):
        self.driver.close()


class Python_Selenium_otherTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/student/Documents/djangogirls/chromedriver')

    def test_login_wrong_user_and_password_gives_errornote(self):
        self.driver.get("http://127.0.0.1:8000/admin/")
        fill_in_field_by_id(self,Global_failing_login_username,"id_username")
        fill_in_field_by_id(self,Global_failing_login_password,"id_password")
        Find_xpath(self,"//input[@value='Log in']")
        assert self.driver.find_element_by_class_name("errornote")

    def test_Title_False(self):
        login(self,"simon","p@ssword")
        navigate_to_blogsite(self)
        assert "Not_the_Title" in self.driver.title

    def test_Title(self):
        login(self,"simon","p@ssword")
        navigate_to_blogsite(self)
        assert "list" in self.driver.title

    def test_Click_on_Post_Shows_Post_Details_page(self):
        login(self,"simon","p@ssword")
        navigate_to_blogsite(self)
        deleteAllPosts(self)
        make_new_post2(self,Global_new_post_title,Global_new_post_text)
        publish(self,Global_new_post_title)
        elements = self.driver.find_elements_by_id("post")
        elements[0].click()
        assert "post_details" in self.driver.title

    def test_publish_Post(self):
        login(self,"simon","p@ssword")
        navigate_to_blogsite(self)
        deleteAllPosts(self)
        make_new_post2(self,Global_new_post_title,Global_new_post_text)
        Find_id(self,"drafts")
        Find_xpath(self,"//a[text()='" + Global_new_post_title + "']")
        Find_xpath(self,"//a[text()='Publish']")
        assert "post_details" in self.driver.title
        post_name = self.driver.find_element_by_tag_name("h2")
        assert post_name.text != ""

    def tearDown(self):
        self.driver.close()

        """

if __name__ == '__main__':
    unittest.main()
