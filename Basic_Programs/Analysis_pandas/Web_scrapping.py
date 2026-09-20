#Install Beautiful soup,lxml,requests
from bs4 import BeautifulSoup
import requests,urllib
import pandas as pd
import requests,webbrowser

from pandas import  Series,DataFrame
#For https webpage:
# webpage=requests.get(url)
#c=webpage.content
# soup=BeautifulSoup(c)#Argument should be  the html document with html tags


# webpage=requests.get("https://www.facebook.com/")#,auth=('snehaclass12@gmail.com','Pleasebeaware6!'))
# # try:
# #     print(webpage.status_code)
# # except:
# #     print("Invalid Authentication ")
# response = urllib.urlopen('http://tutorialspoint.com/python/python_overview.htm')
# # html_doc = response.read()
# response=requests.get("http://localhost:63342/Sanfoundry_programs/Basic_Programs/Analysis_pandas/appendhtml.html")
#
# soup=BeautifulSoup(response.content,'html.parser')
# summary=soup.find('form',{'id':'login_form','action':'https://www.facebook.com/login.php?login_attempt=1&lwv=111'})
# soup=BeautifulSoup(open("G:\\Pythonautomation_softwares\\Sanfoundry_programs\\Basic_Programs\\Analysis_pandas\\appendhtml.html",'r+'),"html.parser").encode("utf-8")
# tables=soup.find_all('table')
# rows=tables[0].find_all('tr')
# for tr in rows:
#     cols=tr.find_all('td')
#     for td in cols:
#         text=td.find(font=True)
#         print(soup.find('font').text)
#         # if td.text=='PASSED':
#         #     r=soup.find('font').td.text
#         #     print(r)

def modify_result_report(filename):
    '''

    :param filename: String
    :return:
    '''
    #Processing html Table data
    soup = BeautifulSoup(open(filename, 'r+'), "html.parser")
    # print(soup.prettify())
    summary = soup.find('table', {'id': 'Datatable'})
    tbody = summary.find_all('tbody')
    trows = tbody[0].find_all('tr')
    theads = summary.find_all('thead')
    # th=[th.find_all('th') for th in theads if th.find_all('th')!]
    for tr in trows:
        cols = tr.find_all('td')

        for td in range(len(cols)):


                if 'FAILED' in cols[td].text:

                    cols[td]['style'] = "color:red;"
                # if td <len(cols)-1 and str(cols[td]).strip() != str(cols[td+1]).strip():
                #     cols[td]['style'] = "color:red;"

                if 'PASSED' in cols[td].text:

                    cols[td]['style'] = "color:green;"
                # elif td < len(cols) - 1 and str(cols[td]).strip() == str(cols[td + 1]).strip():
                #     cols[td]['style'] = "color:green;"

    file = "G:\\Pythonautomation_softwares\\Sanfoundry_programs\\Basic_Programs\\Analysis_pandas\\appendhtml.html"

    with open(file, 'w+') as f:
        f.write(soup.prettify())
        print("Report generated")
    return

url = "https://www.ucop.edu/operating-budget/budgets-and-reports/legislative-reports/2016-17-legislative-session.html"
r = requests.get(url)
status_code = r.status_code
html_content = r.content
soup = BeautifulSoup(html_content, 'html5lib')
if status_code == 200:
    soup.title.string.replace_with("Replaced")
    print(soup.title)
    division = soup.find('div',{'class':'span8 dotted-top'})
    table = (division.find('table',{'id':'report'}))
    # table = soup.find(lambda tag: soup.table.string == 'table' and tag.has_attr('id') or tag['id'] == "Table1")
    # rows = table.findAll(lambda tag: tag.name == 'tr')
    if soup.table.has_attr():
        rows = table.find_all('tr')
    #tagname:tag = soup.tagname(h1|i|b)
    #text for text:soup.tagname.string
    #tag text replacement :tag.string.replace_with('')
    #
    # print(soup.h2.string)
else:
    print(f"WebPage is not launched as expected \n Status_code: {status_code}\n Page: {soup.title.text} \n {soup.prettify()}")






