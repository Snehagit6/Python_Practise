from selenium.webdriver.support.ui import Select


class Utilities:
    def __init__(self,driver):
        self.driver=driver

    def select_element(self,locator,index,text,value):
        '''

        :param locator:
        :param index:
        :param text:
        :param value:
        :return:
        '''
        select=Select(self.driver.find_element_by_name(locator))
        select.select_by_index(index)
        select.select_by_value(value)
        select.select_by_visible_text(text)

class Expect:
    def __init__(self):
        pass