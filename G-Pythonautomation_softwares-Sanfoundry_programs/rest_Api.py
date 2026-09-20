# import requests
#
# content = requests.get("https://gorest.co.in/public/v2/users")
#
# print(content.json())
#
# data_ls = content.json()
#
# active_names = [x['name']  for x in data_ls if x['status'] == 'active']
#
# print(sorted(active_names))


from random import randint
from time import sleep
import threading
import datetime
a = datetime.datetime.now()

def work(id):
    print("work-{} started".format(id))
    sleep(5)
    print("work-{} ended".format(id))

__ = [work(i) for i in range(5)]
# for i in range(5):
#     thread_start = threading.Thread(target = work, args=(i,))
#     thread_start.start()
#     thread_start.join()

b = datetime.datetime.now()
c = b - a
print("Time taken ",c.seconds)
