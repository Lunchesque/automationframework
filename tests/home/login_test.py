from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class LoginTests():

    def test_valid_login(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        loginLink = driver.find_element(By.XPATH, "//a[@href='/sign_in']")
        loginLink.click()

        userEmail = driver.find_element(By.XPATH, "//input[@id='user_email']")
        userEmail.send_keys("test@email.com")

        userPassword = driver.find_element(By.XPATH, "//input[@id='user_password']")
        userPassword.send_keys("abcabc")

        loginBtn = driver.find_element(By.XPATH, "//input[@type='submit']")
        loginBtn.click()

        userSettings = driver.find_element(By.XPATH, "//a[contains(@class, 'open-my-profile-dropdown')]")
        if userSettings is not None:
            print("login seccessfull")
        else:
            print("login not seccessfull")

        ActionChains(driver).pause(2).perform()

ff = LoginTests()
ff.test_valid_login()
