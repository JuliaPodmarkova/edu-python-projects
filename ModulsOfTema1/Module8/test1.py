def greet_person(person_name):
    if person_name == "VolanDeMort":
        raise Exception(f"We don't like you, {person_name}")
    print("Hello " + person_name)

greet_person("Dear student")
#greet_person("VolanDeMort")

try:
    raise NameError("Hello There")
except NameError as exc:
    print(f"The exeption type '{exc}' fly away. His parametres = {exc}")

class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

def f(a, b):
    if b == 0:
        raise ProZero("don't divide by zero", {'a': a, 'b': b})
    return a / b

try:
    result = f(5, 0)
    print(result)
except ProZero as exc:
    print("Not a good day - we have a mistake")
    print(f"Message about mistake: {exc}")
    print(f"Mor information: {exc.extra_info}")