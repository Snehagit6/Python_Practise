import requests,csv

def post(data):

    with open(file,'r+') as fo:
        header = next(csv.reader(fo))
        data = [csv.reader(fo)]

    data = requests.post("https://ytryt",data).json()
    return


with ThreadPool_executor(workers = 35) as exec:
    exec.map(post(data))

    #

    '''
    Excel
    '''