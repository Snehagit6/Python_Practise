from
spec=Spec("G://Pythonexceldata.xlsx")
@spec.data
def read_data(param,**kwargs):
    print(param['ID'])
read_data(6)

