# использование данных из модуля (листа *.py)
#import secondModuleToLections as m2
#from secondModuleToLections import a
#from secondModuleToLections import *
from Module4.secondModuleToLections import sey_hi as sh
import sys

print("Привет, я из модуля 2")
#m2.sey_hi()
#print(a)
#main()
#print(m2.__name__)
sh()

# Модули. Способы импортирования кода

b = 10

for path in sys.path:
    print(path)

# Создание пакетов и компилированные файлы
