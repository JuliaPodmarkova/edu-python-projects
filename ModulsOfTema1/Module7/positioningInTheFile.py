from pprint import pprint

from Module7.readFilesMode import file1

#name = 'sample2.txt'
#file = open(name, 'a')
#file.seek(26)
#pprint(file.tell())
#file.write('\nThere you can write your new text')
#pprint(file.tell())
#file.close()

name = 'sample3.txt'
file = open(name, 'w')
file.write('Привет, я новый текст\nВторая строка нового текста')
file.close()

file1 = open(name, 'r', encoding='utf-8')
pprint(file1.read())
pprint(file1.tell())
print(file1.readable()) # можно ли читать файл
print(file1.writable()) # можно ли делать запись в файле
print(file1.seekable()) # можно ли в файле перемещать строки
print(file1.name) # имя файла
print(file1.buffer) # наличие буфера
print(file1.closed) # закрыт ли файл