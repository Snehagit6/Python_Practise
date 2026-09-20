import csv
import datetime
import requests

#Slower performance Program contained in Debugging...txt Notepad
# time ./program.py
# Slower: real    0m13.548s
# user    0m5.360s
# sys     0m0.220s
#
#
#
# Faster :real    0m9.170s
# user    0m0.248s
# sys     0m0.028s

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)


def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""
    lines = []
    # Download the file over the internet
    response = requests.get(url, stream=True)

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines


def get_same_or_newer(start_date, d):
    """Returns the employees that started on the given date, or the closest one."""

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    # min_date = datetime.datetime.today()
    min_date_employees = []
    search_date = start_date.strftime('%Y-%m-%d')
    for key in d:
        if d[key][0] == search_date:
            min_date_employees.append("{}".format(d[key][1]))

    return start_date, min_date_employees


def list_newer(start_date):

    data = get_file_lines(FILE_URL)
    print(len(data[1:]))
    reader = csv.reader(data[1:])
    keys,values = range(len(data[1:])),[(l[3],l[0]+" "+l[1]) for l in reader]
    d = {k:v for(k,v) in zip(keys,values)}

    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date,d)
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)


def main():
    start_date = get_start_date()
    list_newer(start_date)


if __name__ == "__main__":
    main()