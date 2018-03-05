import pytest
import unittest
from utilities.teststatus import StatusTest
from selenium import webdriver
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = StatusTest(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title verifyed")
        result2 = self.lp.verifySeccessfulLogin()
        self.ts.markFinal("test_valid_login", result2, "Login was seccessful")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login()
        result = self.lp.verifyFailedLogin()
        assert result == True
