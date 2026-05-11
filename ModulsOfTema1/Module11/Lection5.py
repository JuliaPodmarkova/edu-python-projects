from pprint import pprint
import requests
import inspect

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

attr_name = 'attribute_1'

print(hasattr(some_object, attr_name)) #существует атрибут или нет
print(hasattr(some_object, 'attribute_1'))
print()
#pprint(dir(some_object))
print(getattr(some_object, 'attribute_1'))
print(getattr(some_object, attr_name, 'Этого не может быть!'))
print()
for attr_name1 in dir(requests):
    attr = getattr(requests, attr_name1)
    print(attr_name1, type(attr))
print()
print(callable(some_function))
print(callable(some_string))
print(callable(some_object.attribute_1))
print(callable(some_object.some_class_method))
print()
print(isinstance(some_object, SomeClass))
print(isinstance(some_number, SomeClass))
print()
print(inspect.isclass(requests))
print(inspect.ismodule(requests))
print(inspect.isfunction(requests))
print(inspect.isabstract(requests))
print(inspect.isbuiltin(requests))
print()
some_function_module = inspect.getmodule(some_function)
print(type(some_function_module), some_function_module)