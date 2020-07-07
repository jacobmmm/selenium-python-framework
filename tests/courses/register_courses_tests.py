import time
import unittest
import pytest
from utilities.teststatus import TestStatus
from pages.courses.register_courses_pages import RegisterCoursesPage

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
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



    def test_invalidEnrollment(self):
        """
        call required methods from page class to perform the test

        Enter course name

        select course

        Enroll in course

        Verify error message

        Test Status.markFinal()

        """

        self.courses.enterCourseName('JavaScript')
        self.courses.selectCourseToEnroll('JavaScript for beginners')
        self.courses.enrollMaadi()
        #self.courses.webScroll('down')
        self.courses.enrollCourse('1209 4367 9809 4576','09/22','236','90203')
        result=self.courses.verifyEnrollFailed()
        self.ts.markFinal('test_invalidEnrollment',result,'Regarding Enroll Button')