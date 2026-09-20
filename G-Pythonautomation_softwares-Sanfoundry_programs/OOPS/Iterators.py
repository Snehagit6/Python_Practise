class Iterator:
    def __init__(self,name):
        self.name=name
        self.index=len(name)
    def __iter__(self):
        return self
    def __next__(self):

        if self.index==0:
            raise StopIteration
        self.index-=1
        return self.name[self.index]


ci=Iterator("Rekha")
for ch in ci:
    print(ch)

#Generator

def Rev(name):
    for i in range(len(name)-1,-1,-1):
        yield name[i]
r=Rev("Rekha")
for ch in r:
    print(ch)

