from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import utilities.custom_logger as custlog
import traceback
import logging
import time
import os

class SeleniumDriver():
    logger = custlog.customLogger(logging.INFO)

    def __init__(self,driver):
        self.driver=driver

    def getTitle(self):
        return self.driver.title



    def screenShot(self, resultMessage):

        fileName=resultMessage + "." + str(round(time.time()*1000))+".png"
        screenshotDirectory="../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory=os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory,relativeFileName)
        destinationDirectory = os.path.join(currentDirectory,screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)

            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: "+destinationFile)

        except:
            self.log.error("### Exception Occured")
            print_stack()





    def getByType(self,locatorType):
        locatorType=locatorType.lower()
        if locatorType=="id":
            return By.ID

        elif locatorType=="xpath":
            return By.XPATH

        elif locatorType=="css":
            return By.CSS_SELECTOR
        elif locatorType=="class":
            return By.CLASS_NAME
        elif locatorType=="link":
            return By.LINK_TEXT
        elif locatorType=="name":
            return By.NAME


        else:
            self.logger.info("locator type"+locatorType+"not supported")


        return False

    def getElement(self,locator,locatorType="id"):
        element=None
        try:
           locatorType=locatorType.lower()
           byType=self.getByType(locatorType)
           element=self.driver.find_element(byType,locator)
           self.logger.info('Element Found with Locator '+locator+' and locatorType '+locatorType)

        except:
            self.logger.info('Element not found with Locator '+locator+' and locatorType '+locatorType)
        return element

    def elementClick(self,locator="",locatorType='id',element=None):
        """
        CLick on element --> MODIFIED
        Either provide element or a combination of locator and LocatorType
        """


        try:
            if locator:
               element=self.getElement(locator,locatorType)

            element.click()
            self.logger.info("clicked on element with locator"+locator+" locatorType: "+locatorType)

        except:
           self.logger.info('Cannot click on element with locator '+locator+" locatorType: "+locatorType)
           print_stack()

    def sendKeys(self,data, locator="", locatorType='id', element=None):
        """
        Send Keys to an element --> MODIFIED
        Either provide element or a combination of locator and LocatorType
        """
        try:

           if locator:
               element=self.getElement(locator,locatorType)
           element.send_keys(data)
           self.logger.info("Sent data on element with locator"+locator+" locatorType: "+locatorType)

        except:
           self.logger.info('Cannot send data on element with locator '+locator+" locatorType: "+locatorType)
           print_stack()

    def sendKeysWhenReady(self,data,locator,locatorType='id'):

        try:
            byType=self.getByType(locatorType)
            self.log.info("Waiting for maximum:: "+str(20)+" :: seconds for element to be visible")
            wait=WebDriverWait(self.driver, timeout=20, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])

            element=wait.until(EC.visibility_of_element_located((byType,locator)))
            self.log.info("Element with locator: "+locator+"locatorType: "+locatorType+" appeared on web page")
            element.click()
            element.send_keys(data)

            if element.get_attribute("value") !=data:
                self.log.debug("Text is not sent by xpath in field so i will try to send string char by char!")
                element.clear()

                for i in range(len(data)):
                    element.send_keys(data[i]+"")
            self.log.info("Sent data on element with locator: "+locator+" locatorType: "+locatorType)

        except:
            self.log.info("Element with locator: "+locator+"locatorType: "+locatorType+" not appeared on the web page")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))



    def getText(self,locator="",locatorType="id", element=None, info=""):
        """
        NEW METHOD
        Get Text on an element
        """
        try:
            if locator:
                self.logger.debug("In Locator condition")
                element=self.getElement(locator,locatorType)

            self.logger.debug("Before finding Text")
            text=element.text
            self.logger.debug("After finding element, size is"+str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text)!=0:
                self.log.info("Getting text on element ::"+ info)
                self.log.info("The text is ::'"+text+"'")
                text=text.strip()

        except:
            self.log.error("Failed to get text on element"+info)
            print_stack()
            text=None
        return text




    def isElementPresent(self,locator="",locatorType='id', element=None):
        """
        Check if element is present-->MODIFIED
        Either provide element or a combination of locator, locatorType
        """




        try:
           if locator:
               element = self.getElement(locator, locatorType)

           if element is not None:
               self.logger.info("Element found with locator "+locator+" LocatorType "+locatorType)
               return True

           else:
               self.logger.info("Element not found with locator " + locator + " LocatorType " + locatorType)
               return False

        except:
            print("Element not found")
            return False


    def isElementDisplayed(self, locator="",locatorType='id', element=None):
        """
        NEW METHOD
        Check if element is displayed
        """
        isDisplayed=False

        try:
            if locator:
                element=self.getElement(locator,locatorType)

            if element is not None:
                isDisplayed=element.is_displayed()
                self.logger.info("Element is displayed with locator" + locator + "LocatorType" + locatorType)

            else:
                self.logger.info("Element is not displayed with locator" + locator + "LocatorType" + locatorType)
            return isDisplayed

        except:
            print("Element not found")
            return False








    def elementPresenceCheck(self,locator,byType):
        element=None
        try:
            elementList=self.driver.find_elements(byType,locator)
            if len(elementList)>0:
                self.logger.info("Element present with locator" + locator + "LocatorType" + str(byType))
                return True

            else:
                self.logger.info("Element not present with locator" + locator + "LocatorType" + str(byType))
                return False
        except:
            print("No elements found")
            return False

    def webwait(self, locator, LocatorType='id'):

        element = None
        try:
            print("searching for " + locator)
            byType = self.getByType(LocatorType)
            print("locator type is" + byType)
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType,locator)))
            print("Element with locator"+locator+"locatorType"+LocatorType+"appeared on webpage")

        except:
            print("Exception")
        return element

    def getElementList(self,locator,locatorType='id'):
        """
        NEW METHOD
        Get List Of Elements
        """


        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.logger.info('Element list Found with Locator ' + locator + ' and locatorType ' + locatorType)

        except:
            self.logger.info('Element list not found with Locator ' + locator + ' and locatorType ' + locatorType)
        return element


    def webScroll(self, direction="up"):
        """
        NEW METHOD
        """

        if direction == 'up':
            self.driver.execute_script("window.scrollBy(0,-1000);")
            self.logger.info('Scrolled up')

        if direction == 'down':
            self.driver.execute_script("window.scrollBy(0,1000);")
            self.logger.info('Scrolled down')


    def isElementEnabled(self,locator,locatorType='id',element=None):

        isEnabled = False

        try:
            if locator:
                element = self.getElement(locator, locatorType)
                isEnabled = element.is_enabled()

            if isEnabled:

                self.logger.info("Element is enabled with locator" + locator + "LocatorType" + locatorType)

            else:
                self.logger.info("Element is disabled with locator" + locator + "LocatorType" + locatorType)
            return isEnabled

        except:
            print("Element with locator" + locator + "LocatorType" + locatorType + "not found")
            return False

    def switchToFrame(self,id="",name="",index=None):

        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switchToDefaultContent(self):


        self.driver.switch_to.default_content()


    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):

        if locator:
            element=self.getElement(locator=locator,locatorType=locatorType)
        value=element.get_attribute(attribute)
        return value

    def isEnabled(self,locator,locatorType="id",info=""):

        element=self.getElement(locator, locatorType=locatorType)
        enabled=False
        try:
            attributeValue=self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled=element.is_enabled()

            else:
                value=self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value from Application Web UI -->::"+value)
                enabled=not("disabled" in value)

            if enabled:
                self.log.info("Element ::'"+info+"' is enabled")

            else:
                self.log.info("Element ::'"+info+"'is not enabled")

        except:
            self.log.error("Element ::'"+info+"'state could not be found")

        return enabled


    def switchFrameByIndex(self,locator,locatorType='xpath'):

        result=False
        try:
            iframe_list=self.getElementList("//iframe",locatorType='xpath')
            self.log.info("Length of iframe list:")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                iframe_name=iframe_list[i].get_attribute('name')
                self.log.info("Iframe name is "+iframe_name)
                #self.switchToFrame(index=iframe_list[i])
                self.switchToFrame(index=i)
                result=self.isElementPresent(locator,locatorType)
                if result:
                    self.log.info("iframe index is:")
                    self.log.info(str(i))
                    break
                self.switchToDefaultContent()
            return result

        except:
            print("iframe idex not found")
            return result


    def waitImplicitly(self):
        self.driver.implicitly_wait(14)












