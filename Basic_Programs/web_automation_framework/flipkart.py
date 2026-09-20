from selenium import webdriver
from time import sleep
from os import environ
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import pyautogui,os

d = webdriver.Chrome(executable_path="D:\Automation_software\chromedriver_win32\chromedriver.exe")
# options=Options().add_argument('--disable extension--')
# firefox_capabilities = webdriver.DesiredCapabilities().FIREFOX
# firefox_capabilities['acceptSslCerts'] = True
# d=webdriver.Firefox(executable_path="G:\\AutomationSoftware\\geckodriver-v0.22.0-win64\\geckodriver.exe",capabilities=firefox_capabilities)
# ,capabilities=
# {'accept_insecure_certs':True})
# ,firefox_options=options)

# d.implicitly_wait(10)
d.maximize_window()
d.get("https://www.flipkart.com/")
sleep(3)
try:
    # / html / body / div[2] / div / div / button
    # for i in d.find_elements_by_id("hnuiih"):
    #     i.click()
    #     print("Clicked")

    print(WebDriverWait(d,10).until(EC.presence_of_all_elements_located((By.XPATH,"/ html / body / div[2] / div[1] / div/div[3]"))))

#     sleep(3)
#     # WebDriverWait(d,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[3]/div/a"))).click()
#     #
#     # if WebDriverWait(d,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="Km0IJL col col-3-5"]'))).is_displayed():
#     #     pass
#
#
#     actions=ActionChains(d)
#     actions.click_and_hold(WebDriverWait(d,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div[2]/div/ul/li[7]/span")))).perform()
#
    pyautogui.screenshot().save("./Actions_flipkart.png")
    d.execute_script("arguments[0].click();",WebDriverWait(d, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[title='Literature & Fiction']"))))
    sleep(3)
    WebDriverWait(d,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"img[alt='Suspense and Thrillers']"))).click()
    WebDriverWait(d, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[placeholder = 'Search for products, brands and more']"))).click()
    WebDriverWait(d, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"img[alt = 'Death on the Nile']"))).click()
    print(type(d.window_handles))
    parent_window=d.window_handles[0]
    t=type(parent_window)
    for handle in d.window_handles:
        if handle!=parent_window:
            d.switch_to_window(handle)
            sleep(2)
finally:
    d.quit()