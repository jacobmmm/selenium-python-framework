import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as custlog
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    logger = custlog.customLogger(logging.INFO)


    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.nav=NavigationPage(driver)




    #Locators

    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = "//input[@name='commit']"



    def clickLoginLink(self):
        self.elementClick(self._login_link,locatorType="link")

    def enterEmail(self,email):
        self.sendKeys(email,self._email_field)

    def enterPassword(self,password):
        self.sendKeys(password,self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button,locatorType="xpath")

    def login(self,username="",password=""):
        self.clickLoginLink()
        self.clearFields()
        self.driver.implicitly_wait(12)
        self.enterEmail(username)
        self.enterPassword(password)
        time.sleep(14)
        self.clickLoginButton()

    def verifyLoginSuccessful(self,locator,locatorType):
        result=self.isElementPresent(locator, locatorType)
        return result

    def verifyLoginFailed(self,locator,locatorType):
        result=self.isElementPresent(locator,locatorType)
        return result

    def clearFields(self):
        emailField=self.getElement(self._email_field)
        emailField.clear()
        passwordField=self.getElement(self._password_field)
        passwordField.clear()

    def verifyLoginTitle(self):

        return self.verifyPageTitle("Google")

    def logout(self):

        self.nav.navigateToUserOptions()
        self.waitImplicitly()
        self.elementClick(locator="//a[@href='/sign_out']",locatorType='xpath')



