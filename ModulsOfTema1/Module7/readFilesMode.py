from pprint import pprint

name = 'sample.txt'
file = open(name, 'r') # чтение файла; r - read, w - write, a - append
print(file)
pprint(file.read())
file.close()

name1 = 'sample2.txt'
file1 = open(name1, 'w') #полная замена текста в файле
file1.write('\nHello')
file1.close()

file1 = open(name1, 'r')
print(file1.read())
file1.close()

file2 = open(name1, 'a') #дополнение файла
file2.write(' world!')
file2.write('\nHere I am!')
file2.close()

file2 = open(name1, 'r')
pprint(file2.tell()) #положение курсора до чтения файла
print(file2.read())
pprint(file2.tell()) #положение курсора после чтения файла

pprint(file2.seek(13)) #перемещение курсора к определенному символу (по его номеру)
print(file2.read())
file2.close()