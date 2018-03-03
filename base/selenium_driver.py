import logging
from datetime import datetime
from traceback import print_stack
import utilities.custom_logger as cl
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element --" + locator + "-- Found")
        except:
            self.log.info("Element not found")
        return element

    def elementClick(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Element --" + locator + "-- clicked")
        except:
            self.log.info("Cannot click --" + locator + "-- element")

    def sendKeys(self, data, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Send data --" + data + "-- to the --" + locator + "-- element")
        except:
            self.log.info("Cannot send data --" + data + "-- to the --" + locator + "-- element")
            print_stack()

    def isElementPresent(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False


    def waitForElement(self, locator, locatorType="xpath",
                       timeout=10, pollFrequency=0.5):
        element = None

        try:
            byType = self.wrapper.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, 10, poll_frequency=0.5,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             locator)))

            self.log.info("Element appeared on the page")
        except:
            self.log.info("Element not appeared on the page")
            print_stack()

        return element


    def takeScreenshot(self, driver):
        time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        fileName = time + ".png"
        screenshotDirectory = "/home/sergey/Desktop/"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved --> " + destinationFile)
        except NotADirectoryError:
            self.log.info("Not a directory issue")