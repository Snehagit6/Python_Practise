from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  Basic_Programs.automation_framework import *


webpage="http://demo.guru99.com/test/write-xpath-table.html" #WebURL

driver=webdriver.Firefox(executable_path="G:\\AutomationSoftware\\geckodriver-v0.22.0-win64\\geckodriver.exe")
driver.get(webpage)
cell_text=driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td[1]").text
table="/html/body/center/table/tbody"
rows=WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, table+"/tr")))
# print(cell_text) --print cell text
try:
#Printing all cell value
    for row in range(1,len(rows)+1):
        for column in range(1,len(WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,f"{table}/tr[{row}]/td"))))+1):
            print(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,f"{table}/tr[{row}]/td[{column}]")
                                                                                 )).text,end='\t')
        print('\n')
finally:
    driver.quit()


