import logging
import utilities.custom_logger as cl
from base.basepage import BasePage
import time

class RegistreCoursePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _search_field = "//input[@id='search-courses']"
    _search_btn = "//button[@id='search-course-button']"
    _course_banner = "//div[@class='course-listing']"
    _enroll_btn = "//button[@id='enroll-button-top']"

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_field)

    def searchCourse(self):
        self.elementClick(self._search_btn)

    def clickCourseBanner(self):
        self.elementClick(self._course_banner)

    def enrollBtnClick(self):
        self.elementClick(self._enroll_btn)

    def scrollDown(self):
        self.webScroll("down")


    def enrollCourse(self, name=""):
        self.enterCourseName(name)
        self.searchCourse()
        self.clickCourseBanner()
        self.enrollBtnClick()
        self.scrollDown()
