from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrappers


#pytest -s -v tests/home/login_test.py


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = HandyWrappers(self.driver)
    #locators
    _login_link = "//a[@href='/sign_in']"
    _email_field = "//input[@id='user_email']"
    _password_field = "//input[@id='user_password']"
    _login_btn = "//input[@type='submit']"

    def getLoginLink(self):
        return self.wrapper.getElement(self._login_link)

    def getEmailField(self):
        return self.wrapper.getElement(self._email_field)

    def getPasswordField(self):
        return self.wrapper.getElement(self._password_field)

    def getLoginBtn(self):
        return self.wrapper.getElement(self._login_btn)

    def clickLoginLink(self):
        self.getLoginLink().click()

    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginBtn(self):
        self.getLoginBtn().click()

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()
