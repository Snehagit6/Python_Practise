from functools import partial,wraps
def partial_result(func=None,*,prefix='I can code '):
    if func is None:
        return partial(partial_result,prefix=prefix)
    @wraps(func)
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        print(f'{prefix}{result}')
        return result
    return wrapper
@partial_result(prefix='Forever')
def add(a,b):

    return a+b

add(2,3)