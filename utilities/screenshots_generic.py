from datetime import datetime

class TakeScreenshot():

    def takeScreenshot(self, driver):
        time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        fileName = time + ".png"
        screenshotDirectory = "/home/sergey/Desktop/"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved --> " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")