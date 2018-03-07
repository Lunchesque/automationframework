import pytest, unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from utilities.teststatus import StatusTest
from pages.home.navigation_page import NavigationPage
from pages.courses.register_courses_page import RegistreCoursePage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegistreCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegistreCoursePage(self.driver)
        self.ts = StatusTest(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, cNum, cDate, cCVV):
        self.courses.searchForCourse(courseName)
        self.courses.goToEnrollPage()
        self.courses.enterCardCreds(cardnumber = cNum, date = cDate, cvv = cCVV)
        self.courses.enrollCourse()
        result = self.courses.verifyNotEnroll()
        assert result == True
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment verifycation failed")
