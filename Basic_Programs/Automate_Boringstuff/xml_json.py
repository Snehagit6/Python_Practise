import xmltodict,json,os

data = xmltodict.parse(open("D:\\XML_doc.xml","r+", encoding="UTF-8").read())

with open("D:\\JSONfile.json","w+") as fo:
    fo.write(json.dumps(data))


