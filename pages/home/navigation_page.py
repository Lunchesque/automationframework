import logging
import utilities.custom_logger as cl
from base.basepage import BasePage

#pytest -s -v tests/home/login_test.py


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _my_courses = "//a[contains(text(),'My Courses')]"
    _all_courses = "//a[contains(text(),'All Courses')]"
    _practice = "//a[contains(text(),'Practice')]"
    _user_settings = "//a[contains(@class, 'open-my-profile-dropdown')]"

    def navigateToAllCourses(self):
        self.elementClick(self._all_courses)

    def navigateToMyCourses(self):
        self.elementClick(self._practice)

    def navigateToPracticePage(self):
        self.elementClick(self._all_courses)

    def openUserSettings(self):
        self.elementClick(self._user_settings)
