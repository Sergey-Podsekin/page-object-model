from selenium import webdriver
import unittest
import sys
import HtmlTestRunner
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM_automation.Pages.loginPage import LoginPage
from POM_automation.Pages.myAccountPage import MyAccountPage
from POM_automation.Tests.xml_parse import creds


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        login = LoginPage(driver)
        login.enter_email(creds('valid', 'email'))
        login.enter_password(creds('valid', 'password'))
        login.click_login()
        my_account = MyAccountPage(driver)
        my_account.sign_out_click()

    def test_login_invalid_email(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        login = LoginPage(driver)
        login.enter_email(creds('invalid', 'email'))
        login.enter_password(creds('valid', 'password'))
        login.click_login()
        assert login.check_auth_failed_message() == 'Authentication failed.'

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/sergey/Documents/Python_projects'
                                                                  '/automation_practice/page_object_model/reports'))
