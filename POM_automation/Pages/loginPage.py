from POM_automation.Locators.locators import Locators


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox_id = Locators.email_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_xpath = Locators.login_button_xpath
        self.auth_failed_message = Locators.auth_failed_message

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def check_auth_failed_message(self):
        msg = self.driver.find_element_by_xpath(self.auth_failed_message).text
        return msg