import requests
# import runpy
# r=requests.get("https://www.facebook.com/",auth=('snehaclass12@gmail.com','Pleasebeaware6!'))
# print(r.status_code)
# print(r.headers)
# #Manipulating requests
# r=requests.get("https://www.facebook.com/",auth=('snehaclass12@gmail.com','Pleasebeaware6!'),headers={'Pragma': 'cache'})
# print(r.status_code)
# print(r.headers)
#Url redirection
url2 = "https://smallpdf.com/jpg-to-pdf"
r = requests.get("http://learn-automation.com/selenium-webdriver-tutorial-for-beginners/redirect-to",\
                 params={url2:"https://smallpdf.com/jpg-to-pdf"})
import ipdb;

ipdb.set_trace()
for x in r.history:

    print(str(r.status_code)+ ':'+ x.url)

