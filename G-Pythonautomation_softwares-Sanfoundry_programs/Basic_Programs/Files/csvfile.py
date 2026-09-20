import csv, openpyxl, os, pathlib

SUCCESS_MSG='''
Successful login for {}'''
UNSUCCESS_MSG='''Unsuccessful login for {}'''
# file="G://Pythonexceldata.csv"
file1 = "./Associates_1.csv"
file2 = "./Associates_2.csv"
# file=pathlib.Path("G://Pythonexceldata.csv")
i = 1
# try:
#     if !file.endswith(".xlsx"):
#
#         with open(file) as csv_file:
#             csv_reader = csv.reader(csv_file, delimiter=',')
#             for row in csv_reader:
#                 Username, Password = row
#                 # print(row)
#                 if Username == 'snehaclass12@gmail.com':
#                     msg = SUCCESS_MSG.format(Username)
#                     print(msg)
#                 else:
#                     msg = UNSUCCESS_MSG.format(Username)
# except Exception as e:
#     print(e.args())
# else:
#      print("It is a .xlsx file")
# while(i<=10):
#     with open(file,'w+') as csv_file:
#         reader = csv.reader(csv_file, delimiter=',')
#         csv_writer = csv.writer(csv_file)
#         for row in reader:
#
#             csv_writer.writerow(['Arya@12'+str(i)+'.com','gyg%6'+str(i)])
#             # print(row)
#             i += 1

    #
    # csv_file.close()

wb = openpyxl.Workbook()
ws = wb.active
#Advantage of csv reader module over splitting with comma:
# When a file contains comma-separated substrings,the substrings also get separated which is not desirable.

# print(dir(csv))#To get the functions and classes the csv module contains
d1, d2, header = {}, {}, []


def fetch_data(file):
    # global header
    with open(file) as f:
        try:
            reader = csv.reader(f, delimiter=';')
            header = next(reader)
            ws = [row for row in reader if row]#[:-1]
            d = [dict(zip(header,each))for each in ws]
        except Exception as e:
            print(e.args)
        else:
            print(d)
            return d

d1, d2 = fetch_data(file1),fetch_data(file2)

if len(d1)>len(d2):
    (d2.append(dict(zip(header,[None]*len(header)))))

row =1
for i,j in zip(d1, d2):
  print(f"For Row:{row}")
  for key in i:
    if i[key]==j[key]:
      print("***Matched** Source value :{} \t\tDestination value:{}".format(i[key],j[key]))
    else:
        print("***Mismatched** Source value :{} \t\tDestination value:{}".format(i[key], j[key]))
  row+=1
  print("\n")


# file_n=file.replace('.csv','.xlsx')
#
# if os.path.exists(file_n):
#     os.remove(file_n)
#     print("File already exists,so deleted ")
# wb.save(file_n)
# print("File saved successfully")
