from pages.courses.register_courses_page import RegistreCoursePage
from utilities.teststatus import StatusTest
import pytest
import unittest
import time

class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegistreCoursePage(self.driver)
        self.ts = StatusTest(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enrollCourse(courseName="JavaScript",direction="down",
                                    cardnumber="1234123412341234", date="1212", cvv="123")
        assert self.courses.verifyNotEnroll() == True
        time.sleep(3)
