from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pages.home.login_page import LoginPage
import unittest
import pytest

class LoginTests(unittest.TestCase):

    baseUrl = "https://letskodeit.teachable.com"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseUrl)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):

        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifySeccessfulLogin()

        assert result == True

        ActionChains(self.driver).pause(1).perform()
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.driver.get(self.baseUrl)
        self.lp.login()
        result = self.lp.verifyFailedLogin()

        assert result == True

        ActionChains(self.driver).pause(1).perform()
