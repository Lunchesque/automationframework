from traceback import print_stack
from utilities.handy_wrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitType():

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = HandyWrappers(driver)


    def waitForElement(self, locator, locatorType="xpath",
                       timeout=10, pollFrequency=0.5):
        element = None

        try:
            byType = self.wrapper.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, 10, poll_frequency=0.5,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             locator)))

            print("Element appeared on the page")
        except:
            print("Element not appeared on the page")
            print_stack()

        return element