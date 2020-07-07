import time
import unittest
import pytest
from utilities.teststatus import TestStatus
from pages.courses.register_courses_pages import RegisterCoursesPage
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):
    """
    Do everything simsilar to LoginTests
    Examples:
        import page class, Test Status class
        Use fixtures
    """

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)


    @data(("JavaScript for beginners","1209 4367 9809 4576","09/22","236","90203"),("Learn Python 3 from scratch","1209 4367 9809 4576","09/22","236","90203"))
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
        self.driver.get("https://letskodeit.teachable.com/courses")