import os
print('Текущая директорияЖ ', os.getcwd())
#print('Создание новой папки в текущей директории ', os.mkdir('second')) # создание новой папки
# проверка наличия директории и создания ее в случае отсутствия таковой
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
print('Текущая директорияЖ ', os.getcwd())
# создание подпапок важен символ r и слэш
# os.makedirs(r'third\fours')
print(os.getcwd())
# просмотр содержимого директории
print(os.listdir())
for i in os.walk('.'):
    print(i)
# сортировка содержимого директории
os.chdir(r'D:\UrbanUniversity\Urban-University-Home-Work\Urban-University-Home-Work\HomeWork1\Module7')
print('Текущая директорияЖ ', os.getcwd())
print(os.listdir())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)
print(file)
# Запуск файлов и сбор информации о них
#os.startfile(file[6]) #Запуск файла
print(os.stat(file[6]))
#Выполнение команд в командной строке
#print(os.system('pip install --upgrade pip'))
#print(os.system('pip install random2'))