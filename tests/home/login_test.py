import pytest
import unittest
from selenium import webdriver
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifySeccessfulLogin()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login()
        result = self.lp.verifyFailedLogin()
        assert result == True
