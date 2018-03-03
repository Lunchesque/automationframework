from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):

        loginLink = self.driver.find_element(By.XPATH, "//a[@href='/sign_in']")
        loginLink.click()

        userEmail = self.driver.find_element(By.XPATH, "//input[@id='user_email']")
        userEmail.send_keys(username)

        userPassword = self.driver.find_element(By.XPATH, "//input[@id='user_password']")
        userPassword.send_keys(password)

        loginBtn = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        loginBtn.click()
