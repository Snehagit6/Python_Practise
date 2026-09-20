import requests
from bs4 import BeautifulSoup
# import pandas as pd
# from covid import Covid
import csv
from datetime import date, timedelta
# covid = Covid()
'''world data 
yesterday, today = date.today()-timedelta(days=1), date.today()
country = "india"
url = f"https://api.covid19api.com/country/{country}/status/confirmed"
params = {"from": str(yesterday), "to": str(today)}
response = requests.get(url, params=params).json()
print(response)
'''
url = "https://www.mohfw.gov.in/"
r = requests.get(url)
with open("./dat.txt","w+", encoding="utf-8") as file:
    file.writelines(r.text)
    print("Written to file")
print(r.headers)
html_content = r.content.decode("UTF-8")
print(r.status_code)  # ,'\n',html_content)
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup)
print("Title of the webpage:%s "%soup.title.text)
data_ls = []
theads = []
if r.status_code == 200:
    state_data_table = soup.find('table').get("tbody")
    print(state_data_table)
with open("./dat.txt","w+",encoding="utf-8") as file:
    file.writelines(str(html_content))
    if hasattr(state_data_table, 'table'):
        theads = state_data_table.find('thead').find('tr').find_all('th')
        theads = [th.text for th in theads]
        tbody = state_data_table.find('tr')
        print(tbody)
        trows = tbody.find_all('tr')
        for tr in trows:
            rows = []
            cols = tr.find_all('td')

            for td in cols:
                td_txt = td.text
                rows.append(td_txt)

            data_ls.append(rows)
            print(data_ls)
data_ls = [l for l in data_ls if len(l) == len(theads) and "" not in l]
print(data_ls)
data_dict = [dict(zip(theads, ds_ls)) for ds_ls in data_ls]
print(data_dict)
active_cases = sum([int(x['Active Cases*']) for x in data_dict])
cured_discharged_migrated_cases = sum([int(x["Cured/Discharged/Migrated*"]) for x in data_dict])
death_cases = sum([int(x["Deaths**"])for x in data_dict])
confirmed_cases = sum([int(x["Total Confirmed cases*"]) for x in data_dict])
dt_tm = str(date.today()) + "_"+str(datetime.now().strftime("%H_%M_%S"))
# data_dict.append(dict(zip(theads, {"Total:", "", active_cases, cured_discharged_migrated_cases, death_cases, confirmed_cases})))
# print([{"Active_cases":active_cases, "Discharged_migrated_cases":cured_discharged_migrated_cases, \
#                         "Death_cases":death_cases, "Confirmed_cases":confirmed_cases}])
file = f"D:\Python_Practise_Programs\G-Pythonautomation_softwares-Sanfoundry_programs\Basic_Programs\Analysis_pandas\
\COVID-19_results\{dt_tm}.csv"
with open(file,"w+") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=theads)
    writer.writeheader()
    writer.writerows(data_dict)
    print("Data written to file")


    # writer.writerows([{"Active_cases":active_cases, "Discharged_migrated_cases":cured_discharged_migrated_cases, \
    #                    "Death_cases":death_cases, "Confirmed_cases":confirmed_cases}])


# print(sum(list(filter(lambda x :int(x['Active Cases*']),data_dict))))
#
#
# df1 = pd.DataFrame(data_ls, columns = theads)
# print(df1)
# df1.to_html("./COVID19_cases.html")
# window = tk.Tk()
# window.configure()
# greeting = tk.Label(window, text="Hello, Tkinter")
# greeting.pack()
# entry = tk.Entry(window)
#
# window.mainloop()
#

