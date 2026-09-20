import requests
r=requests.head("https://www.facebook.com/")
# s=r.text

with open("G:\\Pythonautomation_softwares\\Sanfoundry_programs\\Basic_Programs\\Penetration_testing"
        "\\response.txt",'w+',encoding='utf-8') as fo:
    fo.write(str(r.headers))





