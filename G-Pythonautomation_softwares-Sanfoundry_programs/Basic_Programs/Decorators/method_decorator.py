from functools import wraps
def method_decorator(method):
    '''
    Method decorators allow overriding class properties by decorating, without having to find the calling function.
    :param method:
    :return:
    '''
    @wraps(method)
    def inner(city_instance):
        '''

        :param city_instance:
        :return:
        '''
        print(method.__name__)
        if city_instance.name == 'SFO':
            print("It is a cool place to stay")

        else:
            method(city_instance)
    return inner


class City():
    def __init__(self, name):
        self.name = name
    @method_decorator
    def print_test(self):
        '''

        :return:
        '''
        print(self.name)

c1 = City("PKO")
c1.print_test()
print(c1.print_test.__name__)
print(c1.print_test.__doc__)