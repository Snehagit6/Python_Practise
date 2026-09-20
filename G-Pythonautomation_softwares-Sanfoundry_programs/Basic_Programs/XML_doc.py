import xml.etree.ElementTree as ET
import csv
tree=ET.parse("C:\\Users\\hp\\Desktop\\XML_file.xml")
root=tree.getroot()
#Parsing contents of xml file
# for r in root:
#     for ele in r:
#         print(ele.text)
#Converting xml file to csv file
header=[]
contents=[]

with open(".\Csv_data.csv",'w') as csv_file:
    csvwriter=csv.writer(csv_file)
    def writing_header():
        count=0
        for elements in root.findall('books'):
            for subelements in elements:
                if count==0:
                    header.append(subelements.tag)
            count+=1
        csvwriter.writerow(header)    
   
    def writing_data():
        writing_header()
        for elements in root.findall('books'):
            for subelements in elements:

                contents.append(subelements.text)
            csvwriter.writerow(contents)
            contents.clear()


    writing_data()     
        
        
    
    
    
   