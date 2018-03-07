import pytest, unittest
from ddt import ddt, data, unpack
from utilities.teststatus import StatusTest
from pages.courses.register_courses_page import RegistreCoursePage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegistreCoursePage(self.driver)
        self.ts = StatusTest(self.driver)

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.run(order=1)
    @data(("JavaScript", "1234123412341234", "1212", "123"), ("Learn Python 3 from scratch", "20", "1212", "123"))
    @unpack
    def test_invalidEnrollment(self, courseName, cNum, cDate, cCVV):
        self.courses.searchForCourse(courseName)
        self.courses.goToEnrollPage()
        self.courses.enterCardCreds(cardnumber = cNum, date = cDate, cvv = cCVV)
        self.courses.enrollCourse()
        result = self.courses.verifyNotEnroll()
        assert result == True
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment verifycation failed")
        self.driver.back()
        self.driver.find_element_by_link_text("All Courses").click()
