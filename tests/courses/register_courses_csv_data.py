import time
import unittest
import pytest
from utilities.teststatus import TestStatus
from pages.courses.register_courses_pages import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):
    """
    Do everything simsilar to LoginTests
    Examples:
        import page class, Test Status class
        Use fixtures
    """

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        #self.navigator = NavigationPage(self.driver)

    def setUp(self):
        self.driver.get("https://letskodeit.teachable.com/courses")


    @data(*getCSVData("C:/Users/Jacob/PycharmProjects/letskodeit2/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV, ccZip):
        """
        call required methods from page class to perform the test

        Enter course name

        select course

        Enroll in course

        Verify error message

        Test Status.markFinal()

        """
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollMaadi()
        #self.courses.webScroll('down')
        self.courses.enrollCourse(ccNum, ccExp, ccCVV, ccZip)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal('test_invalidEnrollment', result, 'Regarding Enroll Button')
        #self.driver.find_element_by_link_text("All Courses").click()
        self.setUp()

