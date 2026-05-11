'''def by_3(x):
    return x * 3

def is_odd(x):
    return x % 2

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = map(by_3, my_numbers)
print(list(result))'''

collection = [3, 1, 4, 1, 5, 9, 2, 6]

list_comp_1 = [x * 3 for x in collection]
print(list_comp_1)

list_comp_2 = [x * 2 for x in collection if x > 5]
print(list_comp_2)

list_comp_3 = [x * 3 for x in collection if x % 2]
print(list_comp_3)

list_comp_4 = [x * 2 if x >2 else x * 10 for x in collection]
print(list_comp_4)

collection1 = ['A', 1, 4, 'B', 5, 'C', 2, 6]
result1 = [x if type(x) == str else x * 5 for x in collection1]
print(result1)

collection2 = [2, 7, 1, 8, 2, 8, 1, 8]
result2 = [x * y for x in collection for y in collection2]
print(result2)

result3 = [x * y for x in collection for y in collection2 if x % 2]
print(result3)

result4 = [x * y for x in collection for y in collection2 if x % 2 and y // 2]
print(result4)

mnojestvo = {x for x in collection}
print('mnojestvo', mnojestvo)

dictionary = {x: x ** 2 for x in collection}
print('dictionary', dictionary)