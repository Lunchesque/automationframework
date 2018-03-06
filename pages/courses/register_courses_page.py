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
    _another_card_btn = "//button[text()='Use another card']"
    _iframe_card_enter = "__privateStripeFrame4"
    _cardnumber_field = "//div[@id='root']/form//input[@name='cardnumber']"
    _date_iframe = "__privateStripeFrame5"
    _date_field = "//div[@id='root']/form//input[@name='exp-date']"
    _cvv_iframe = "__privateStripeFrame6"
    _ccv_field = "//div[@id='root']/form//input[@name='cvc']"
    _back_to_saved_card = "//div[@class='cc__back-to-existing']"
    _submit_enroll_btn = "//button[@id='confirm-purchase']"
    _url_to_verify = "https://sso.teachable.com/secure/42299/checkout/342639/complete-javascript-guide"


    def enterCourseName(self, courseName):
        self.sendKeys(courseName, self._search_field)

    def searchCourse(self):
        self.elementClick(self._search_btn)

    def clickCourseBanner(self):
        self.elementClick(self._course_banner)

    def enrollBtnClick(self):
        self.elementClick(self._enroll_btn)

    def scrollDown(self, direction):
        self.webScroll(direction)

    def anotherCardBtn(self):
        self.elementClick(self._another_card_btn)

    def enterCardNumber(self, cardnumber):
        self.iframeSwitch(self._iframe_card_enter)
        self.sendKeys(cardnumber, self._cardnumber_field)
        self.switchParentPage()

    def enterExpirationDate(self, date):
        self.iframeSwitch(self._date_iframe)
        self.sendKeys(date, self._date_field)
        self.switchParentPage()

    def enterCVV(self, cvv):
        self.iframeSwitch(self._cvv_iframe)
        self.sendKeys(cvv, self._ccv_field)
        self.switchParentPage()

    def enterCardCreds(self, cardnumber, date, cvv):
        self.enterCardNumber(cardnumber)
        self.enterExpirationDate(date)
        self.enterCVV(cvv)

    def backToSavedCArd(self):
        self.elementClick(self._back_to_saved_card)

    def submitEnroll(self):
        self.elementClick(self._submit_enroll_btn)

    def enrollCourse(self, courseName="", direction="", cardnumber="", date="", cvv=""):
        self.enterCourseName(courseName)
        self.searchCourse()
        self.clickCourseBanner()
        self.enrollBtnClick()
        self.scrollDown(direction)
        self.anotherCardBtn()
        self.enterCardCreds(cardnumber, date, cvv)
        self.backToSavedCArd()
        self.submitEnroll()

    def verifyNotEnroll(self):
        result = self.getCurrentUrl()
        return result == self._url_to_verify
