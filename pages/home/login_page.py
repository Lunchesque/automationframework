import logging
import utilities.custom_logger as cl
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage
import time

#pytest -s -v tests/home/login_test.py


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    #locators
    _page_title = "Let's Kode It"
    _login_link = "//a[@href='/sign_in']"
    _email_field = "//input[@id='user_email']"
    _password_field = "//input[@id='user_password']"
    _login_btn = "//input[@type='submit']"
    _user_settings = "//a[contains(@class, 'open-my-profile-dropdown')]"
    _invalid_creds_alert = "//div[@class='alert alert-danger']"
    _logout_btn = "//a[@href='/sign_out']"

    def clickLoginLink(self):
        self.elementClick(self._login_link)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password,self. _password_field)

    def clickLoginBtn(self):
        self.elementClick(self._login_btn)

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()

    def verifySeccessfulLogin(self):
        result = self.isElementPresent(self._user_settings)
        return result

    def verifyFailedLogin(self):
        result = self.isElementPresent(self._invalid_creds_alert)
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle(self._page_title)

    def logout(self):
        self.nav.openUserSettings()
        time.sleep(1)
        self.elementClick(self._logout_btn)
