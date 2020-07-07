import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as custlog
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    logger = custlog.customLogger(logging.INFO)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators

    _my_courses = 'My Courses'
    _all_courses = 'All Courses'
    _practice = 'Practice'
    _user_icon = "//img[@class='gravatar']"

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses,locatorType='link')

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType='link')

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType='link')

    def navigateToUserOptions(self):
        self.webwait(locator=self._user_icon,LocatorType='xpath')
        self.elementClick(locator=self._user_icon, locatorType='xpath')






