from selenium import webdriver
import unittest
from POM_automation.Pages.loginPage import LoginPage
from POM_automation.Pages.myAccountPage import MyAccountPage


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
        login.enter_email("sergey@test.com")
        login.enter_password("test123")
        login.click_login()

        my_account = MyAccountPage(driver)
        my_account.sign_out_click()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')


if __name__ == '__main__':
    unittest.main()
