from pprint import pprint

import requests
#help(requests)
'''print(requests.__cake__)
print(requests.__author_email__)
print(requests.__version__)
print(requests.__url__)'''

some_string = 'I am a string'
some_number = 42
some_list = [some_string, some_number]

def some_function(param, param_2 = 'n/a'):
    print('My param is ', param, param_2)

class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1= value
        print(self.attribute_1)

some_object = SomeClass()
func = some_function

print(some_function.__name__)
print(SomeClass.__name__)
print(requests.__name__)
print(func.__name__)
print(type(some_string) is str)
print(type(some_number) is int)
print(type(requests.get))
pprint(dir(some_object))
pprint(dir(some_object))
pprint(dir())