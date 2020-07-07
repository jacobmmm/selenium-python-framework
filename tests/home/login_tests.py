from selenium import webdriver
from pages.home.login_page import LoginPage
import time
import unittest
import pytest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("setUp","oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)



    @pytest.mark.run(order=2)
    def test_validLogin(self):

        self.lp.login('test@email.com','abcabc')
        result2 = self.lp.verifyLoginTitle()
        self.ts.mark(result2,'Title is incorrect')
        result1=self.lp.verifyLoginSuccessful("//img[@class='gravatar']",'xpath')
        self.ts.markFinal("test_validLogin",result1,"Login was not successful")
        time.sleep(5)


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):

        self.lp.logout()
        self.lp.login('test@email.com','abcabcabcab')

        result=self.lp.verifyLoginFailed("//div[contains(text(),'Invalid email or password')]",'xpath')

        assert result==True


        time.sleep(5)




