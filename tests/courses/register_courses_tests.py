from pages.courses.register_courses_page import RegistreCoursePage
from utilities.teststatus import StatusTest
import pytest
import unittest

class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegistreCoursePage(self.driver)
        self.ts = StatusTest(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.searchForCourse(courseName="JavaScript")
        self.courses.goToEnrollPage()
        self.courses.enterCardCreds(cardnumber="1234123412341234", date="1212", cvv="123")
        self.courses.enrollCourse()
        result = self.courses.verifyNotEnroll()
        assert result == True
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment verifycation failed")
