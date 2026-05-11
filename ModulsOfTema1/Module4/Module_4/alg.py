def bubbleSort(ls):
    #Чтобы цикл сработал хотя бы один раз, задаем значение переменной True
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls)-1):
            if ls[i] > ls[i+1]:
                # Меняем элементы местами
                ls[i], ls[i+1] = ls[i+1], ls[i]
                # Меняем значение переменной swapped для следующего повтора цикла
                swapped = True

def selectionSort(ls):
    # i - количество отсортированных элементов
    for i in range(len(ls)):
        # Изначально считаем минимальным первый элемент
        lowest = i
        # цикл для перебора неотсортированных элементов
        for j in range(i, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        # Самый минимальный элемент меняем местами с первым элементом
        ls[i], ls[lowest] = ls[lowest], ls[i]

def insertionSort(ls):
    for i in range(1, len(ls)):
        temp = ls[i]
        j = i - 1
        while j >= 0 and ls[j] > temp:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = temp