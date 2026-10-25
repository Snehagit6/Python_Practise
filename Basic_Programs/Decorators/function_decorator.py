import time
from functools import wraps
def timetest(input_func):
    #wraps decorator retain the originality of the wrapped function
    @wraps(input_func)
    def timed(*args,**kwargs):
        '''function is referenced as timed'''
        start_time = time.time()
        result = input_func(*args, **kwargs)
        end_time = time.time()
        print("Method Name -{name},Args-{args},Kwargs -{kwargs},Execution Time -{time}".format(name=input_func.__name__,args=args,
                                                                                 kwargs=kwargs,time=round((end_time-start_time),4)))
        return result
    return timed

# Function decorator:@timetest decorates the function "Function" without modifying its true nature.
@timetest
def function(*args, **kwargs):
    '''This is the actual function'''
    time.sleep(5)
    print("Inside function")
    print(args, kwargs)
function(['d','l'])
# args:['apple','cake'],a=2,b=9
print(function.__name__)
print(function.__doc__)


#Decorating list
def modify(fn):
    def inner():
        l = fn()
        for i in range(len(l)):
            l[i]=[((''.join(l[i][0].split('_'))).title())]
        return l


    return inner
@modify
def alter():
    return [['sarah_s'],['clara_c'],['jacinth_j']]

print("Decorated function",alter())

#Decorator with arguments

def wrap(*args, **kwargs):
    print("Inside decorator")
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print("Inside inner function")
            func_vcall = func(*args, **kwargs)
            print("Start step:", args[0])
            return func_vcall
        return inner
    return decorator


@wrap("Step 1")
def func():
    return

print(func())

