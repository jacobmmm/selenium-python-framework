from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl



class TestStatus(SeleniumDriver):

    log=cl.customLogger(logging.INFO)

    def __init__(self,driver):

        """
        inits checkpoint class
        """
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL::+"+resultMessage)

                else:
                    self.resultList.append("FAIL")
                    self.log.info("### VERIFICATION FAILED::+"+resultMessage)
                    self.screenShot(resultMessage)

            else:
               self.resultList.append("FAIL")
               self.log.error("### VERIFICATION FAILED::+" + resultMessage)
               self.screenShot(resultMessage)

        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occured !!!")
            self.screenShot(resultMessage)




    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result,resultMessage)


    def markFinal(self, testName, result, resultMessage):

        self.setResult(result,resultMessage)

        if 'FAIL' in self.resultList:
            self.log.error(testName+'### Test FAILED')
            self.resultList.clear()
            assert True==False

        else:
            self.log.info(testName+'### Test Successful')
            self.resultList.clear()
            assert True == True

