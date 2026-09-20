
class Pet:

    def __init__(self,name):

        self.name=name
        print("Name:%s"%name)


class Cat(Pet):
    cnt = 0

    def __init__(self,name):
        Pet.cnt += 1
        super().__init__(name)
    # def ch(self):
    #     self.change_name()
def main():
    c=Cat("mack")

    d=Cat("deck")

if __name__=='__main__':
    main()
    print(f'{Pet.cnt} objects of Pet class')




