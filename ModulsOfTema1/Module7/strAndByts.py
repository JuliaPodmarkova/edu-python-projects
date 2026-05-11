from encodings.utf_16 import decode

print('hello')
print('Номер символа "А" в таблице кодировки символов ASCII: ', ord('A'))
print('Номер символа "a" в таблице кодировки символов ASCII: ', ord('a'))

a = 'hello'
chars = []
for i in a:
    chars.append(ord(i))
print(f'Список символов "{a}" в таблице кодировки символов ASCII: ' )
print(chars)

s = ""
for i in chars:
    s += chr(i)
print(f'Кодировки символов ASCII - перевод набора символов {chars} в слово: ')
print(s)

for i in range(1, 128):
    print(f'Вывод символов кодировки ASCII: {i} = ', chr(i))

for i in range(1000, 1201):
    print(f'Вывод символов с позиций 1000 - 1200 кодировка Unicode: {i} = ', chr(i))

print("Перевод символа 'h' в байты")
print(hex(ord("h")))
bb = b'\x68'
print(type(bb))
print(bb.decode())