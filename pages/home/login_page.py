from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl

#pytest -s -v tests/home/login_test.py


class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _login_link = "//a[@href='/sign_in']"
    _email_field = "//input[@id='user_email']"
    _password_field = "//input[@id='user_password']"
    _login_btn = "//input[@type='submit']"

    def clickLoginLink(self):
        self.elementClick(self._login_link)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password,self. _password_field)

    def clickLoginBtn(self):
        self.elementClick(self._login_btn)

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()
