import datetime as dt
dt1=dt.datetime.now()
print(dt1.month)
dt2=dt1+dt.timedelta(days=10)
print("Datetime after 10 days from now is:{}".format(dt2))
