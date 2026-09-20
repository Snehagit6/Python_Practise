#!/usr/bin/python3.5
import re
import sys


def extract_names(fname):
    '''
    Fetches data from the file.
    :return:the data from the file as a single list in the below format --
    the year string at the start of the list followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Abagail 895', 'Aaron 57', ...]
    '''
    input_file, data, l = fname, " ", []
    with open(input_file, "r+") as r:
        data = r.read()
    # print("Data in the file %s"%data)
    year = re.search("Popularity in (\d+)",data)
    l.append(year.group(1))
    nm_rank = re.findall("<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>",data)
    print("Nm rank %s" %nm_rank)
    # print(nm_rank)
#     d = {}
#
#     for tup in nm_rank:
#         if tup[1] not in d:
#             d[tup[1]] = tup[0]
#             d[tup[2]] = tup[0]
#         names = sorted(list(d. keys()))
#     print(d)
#     for n in names:
#
#         name_rank = n+" "+d[n]
#
#         l.append(name_rank)
#
#     return l
#
# def main():
#     args = sys.argv[1:]
#     if not args:
#         print('usage: [--summaryfile] file [file ...]')
#         sys.exit(1)
#     for fname in args:
#         names = extract_names(fname)
#         text = '\n'.join(names)
#         with open(fname,".summary","w") as fo:
#             fo.write(text+"\n")
#
#
#
#
# if __name__ == "__main__":
#     main()
#
extract_names("D://Python_Practise_Programs//Praccy_Progs//Basic_Programs//\
Automate_Boringstuff//Google_baby_names//baby1990.html")