from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_valid_login(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        userSettings = driver.find_element(By.XPATH,
                                            "//a[contains(@class, 'open-my-profile-dropdown')]")
        if userSettings is not None:
            print("login seccessfull")
        else:
            print("login not seccessfull")

        ActionChains(driver).pause(2).perform()
