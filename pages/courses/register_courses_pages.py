import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log=cl.customLogger(logging.DEBUG)

    _search_box = "search-courses"
    _search_icon="search-course-button"
    _course="JavaScript for beginners"
    _all_courses=""
    _enroll_button="enroll-button-top"
    _cc_num = "//div[@class='CardNumberField CardNumberField--ltr']"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _zip ="postal"
    _submit_enroll="//button[@class='btn btn-primary spc__button is-disabled']"
    _agree_to_terms_checkbox="agreed_to_terms_checkbox"
    _enroll_error_message=""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    def enterCourseName(self, name):
        self.webwait(self._search_icon)
        self.sendKeys(name,self._search_box)
        self.elementClick("search-course-button")

    def selectCourseToEnroll(self, fullCourseName):
        xpath=f'//div[@title="{fullCourseName}"]'
        self.elementClick(xpath,locatorType="xpath")

    def enrollMaadi(self):

        self.elementClick("enroll-button-top")


    
    def enterCardNum(self, num):
        #self.switchToFrame(name="__privateStripeFrame16")
        self.waitImplicitly()
        self.switchFrameByIndex(self._cc_num,locatorType="xpath")
        self.sendKeysWhenReady(num,locator=self._cc_num,locatorType="xpath")
        #self.sendKeys(num,self._cc_num,locatorType='xpath')
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        #self.switchToFrame(name="__privateStripeFrame17")
        self.switchFrameByIndex(self._cc_exp, locatorType="name")
        self.sendKeysWhenReady(exp, locator=self._cc_exp, locatorType="name")
        #self.sendKeys(exp,self._cc_exp,locatorType='name')

        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        #self.switchToFrame(name="__privateStripeFrame18")
        self.switchFrameByIndex(self._cc_cvv, locatorType="name")
        self.sendKeysWhenReady(cvv, locator=self._cc_cvv, locatorType="name")
        #self.sendKeys(cvv,locator=self._cc_cvv,locatorType="name")
        self.switchToDefaultContent()

    def enterZip(self, zip):
        #self.switchToFrame(name="__privateStripeFrame19")
        self.switchFrameByIndex(self._zip, locatorType="name")
        self.sendKeysWhenReady(zip, locator=self._zip, locatorType="name")
        #self.sendKeys(zip,self._zip,locatorType="name")
        self.switchToDefaultContent()

    def clickAgreeToTermsCheckBox(self):
        self.elementClick(self._agree_to_terms_checkbox)


    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")


    """
    def enterCreditCardInformation(self,num,exp, cvv):
        #Call all three methods to enter card details
    """

    def enrollCourse(self, num="", exp="",cvv="",zip=""):
        """
        Click on enroll button
        Scroll down
        Enter credit card information
        Click Enroll in course button
        """
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterZip(zip)
        self.clickAgreeToTermsCheckBox()


    def verifyEnrollFailed(self):

        """
        Verify the element for error message is displayed,
        not just present.
        You need to verify if it is displayed
        
        Hint: The element is not instantly displayed, it takes some time to display
        You need to wait for it to display
        """

        result=self.isElementEnabled("confirm-purchase")
        return result



        
