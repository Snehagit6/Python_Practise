a=9
try:
    a=9/0
except ZeroDivisionError:
    print("Zerodivision error")

try:
    from selenium import webdriver
except ImportError:
    print("Cannot import selenium.webdriver")

try:
    assert 7>9,'Comparison is True'
except AssertionError:
    print("Comparison is False")

try:
    list=[8,9,0,'a']
    try:
        z=list[7]
    except (IndentationError,IndexError) as p:
        print("List out of range")
except:
    print("Wrong values")



a=a*2
print(a//3)

'''User defined exceptions'''
#User defined exceptions is created by deriving classes from the standard built-in exceptions.

class ComparisonError(Exception):


    def __init__(self, arg):

        self.args = arg

try:
    7>9
    raise ComparisonError("Comparison returns false")
except ComparisonError as e:
    print(''.join(e.args))

class RadiusInputError(Exception):

    def __init__(self,arg):
        self.args = arg

class Circle():

    def __init__(self, radius):
        self.radius = radius


try:
    argument = int(input('Enter input'))
    c = Circle(argument)

    raise RadiusInputError(f"{argument} is not a number")
except RadiusInputError as e:
    print(''.join(e.args))






