def calculate_structure_sum(args):
    total_sum = 0

    if isinstance(args, (list, tuple, set)):
        for item in args: # список, множество, кортеж
            total_sum += calculate_structure_sum(item)
    elif isinstance(args, dict):
        for key, value in args.items(): #словарь
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)
    elif isinstance(args, str):
        total_sum += len(args) # строка
    elif isinstance(args, int) or isinstance(args, float):
        total_sum += args # число

    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]),
]

result = calculate_structure_sum(data_structure)
print(result)