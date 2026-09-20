class Person:
    all_employees = []
    all_employees.append('d')
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def change_name(self):
        if self.fname.startswith('J'):
            self.fname=self.fname.replace('J','M')
        print(self.fname)
class Employee(Person):

    def __init__(self,fname,lname,empid):
        super().__init__(fname,lname)
        super().change_name()

        

    # def ch(self):
    #     self.change_name()
e1=Employee('Jack','Dawson',123456)
e1.change_name()
print(e1.all_employees)
# print(e1.fname ,e1.lname ,e1.empid)


