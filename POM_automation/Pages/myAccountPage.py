class MyAccountPage():

    def __init__(self, driver):
        self.driver = driver
        self.sign_out_button_xpath = '//*[@class="logout"]'

    def sign_out_click(self):
        self.driver.find_element_by_xpath(self.sign_out_button_xpath).click()
