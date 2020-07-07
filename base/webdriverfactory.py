from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class WebDriverFactory():

    def __init__(self,browser):

        self.browser=browser

    def getWebDriverInstance(self):

        baseURL = 'https://learn.letskodeit.com/'

        if self.browser == 'firefox':
            driver=webdriver.Firefox()

        elif self.browser == 'iexplorer':
            driver=webdriver.Ie()

        elif self.browser == 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
            #driver=webdriver.Chrome(executable_path="C:\\Users\\Jacob\\PycharmProjects\\driver\\chromedriver.exe")
            #driver.set_window_size(1440, 900)

        else:
            #driver = webdriver.Chrome(executable_path="C:\\Users\\Jacob\\PycharmProjects\\driver\\chromedriver.exe")
            driver = webdriver.Chrome(ChromeDriverManager().install())
            #driver.set_window_size(1440, 900)

        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)
        return driver

