
import operator
def wrapper(f):
    def inner(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return inner
@wrapper
def sort_phone(l):
    print(*sorted(l),sep="\n")





if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)