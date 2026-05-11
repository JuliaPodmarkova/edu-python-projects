import io
from pprint import pprint

name = 'sample3.txt'

# Формула работы с with
# with EXPR as TARG:
#       ACTION

with open(name, encoding='utf-8') as file:
    for line in file:
        #print(line, end='') # end убирает расстояние между строками
        for char in line:
            print(char, end='')
