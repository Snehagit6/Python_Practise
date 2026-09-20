from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import unittest

from Sanfoundry_programs.Basic_Programs.web_automation_framework.selenium_lib import load_browser

class FB_login(unittest.TestCase):

    def setUp(self):
        self.driver=load_browser.initialize_browser("Chrome")
    # def assert_true(self,cdn,msg):
    #     if cdn:
    #         return True
    #     else:
    #         print (msg)
    #     return True
    def test_launch_app(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
        # self.assert_true("Flipkart" in self.driver.title,"Incorrect_webpage")
        file = "G:\\Pythonautomation_softwares\\Sanfoundry_programs\\facebook.png"
        if os.path.exists(file):
            os.remove(file)


        pyautogui.screenshot().save(file)

        print("Screenshot captured")


       # WebDriverWait(self.driver,20).until(EC.presence_of_element_located(By.XPATH,
        self.driver.find_element_by_xpath("//input[@type='email' and @name='email']").send_keys(os.environ["USERNAME"])
        self.driver.find_element_by_xpath("//input[@type='password' and @name='pass']").send_keys(os.environ["PASSWORD"])

    def tearDown(self):
        self.driver.close()

if '__name__'=='__main__':
    unittest.main()