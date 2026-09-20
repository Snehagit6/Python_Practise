from os import environ
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def email(self):
        '''
        Prop
        :return: WebElement
        '''
        return WebDriverWait(self.driver).find_element_by_xpath("//input[@type='email' and @name='email']").\
            send_keys(environ["USERNAME"])

    @property
    def password(self):
            '''
            Prop
            :return: WebElement
            '''
            return self.driver.find_element_by_xpath("//input[@type='password' and @name='pass']"). \
                send_keys(environ["PASSWORD"])

    def login(self,usernmae,password):
        '''

        :return:
        '''

        self.email.send_keys(environ["USERNAME"])
        self.driver.find_element_by_xpath(self.password).send_keys(environ["PASSWORD"])



print(LoginPage(driver="kl").password)