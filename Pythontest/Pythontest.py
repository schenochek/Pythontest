#   Операторы Python (арифметика)
"""
3 + 4 == 7 #        Сложение
3 - 4 == -1 #       Вычитание
3 * 4 == 12 #       Умножение
3 / 4 == 0.75 #     Деление
3 ** 4 == 81 #      Возведение в степень
3 // 4 == 0 #       Деление без остатка
3 % 4 == 3 #        Остаток от деления
"""
#   Операторы Python (сравнение)
"""
    3 < 4 == True #     Меньше
    3 > 4 == False #    Больше
    3 <= 4 == True #    Меньше или равно
    3 >= 4 == False #   Больше или равно
    3 == 4 == False #   Равенство
    3 != 4 == True #    Неравенство
"""
#   Операторы Python (присваивание)
"""
x = 3 (x == 3) #    Присваивание
x = 1
x += 3 (x == 4) #   Плюс присваивание
x = 1
x -= 3 (x == -2) #  Минус присваивание
# и так далее...
"""
#   Операторы Python (логика)
"""
True and False == False #   Конъюнкция
True or False == True #     Дизъюнкция
True xor False == True #    Исключающая дизъюнкция
not(True) == False #        Отрицание
"""
#   Операторы Python (тождество)
"""
'2' is '2' == True #        Тождественно
2 is not '2' == True #      Не тождественно 
"""
#   Операторы Python (битовые)
"""
2 & 3 == 2 #    Побитовая конъюнкция 
3 & 4 == 0 #    Побитовая конъюнкция ( 011 & 100 == 000 )
2 | 3 == 3 #    Побитовая дизъюнкция ( 10 | 11 == 11 )
2^3 == 1 #      Побитовая исключающая ( 10 ^ 11 == 01 )
~ -3 == 2 #     Инвертирование ( ~00000010 == 11111101 )
2 << 2 == 8 #   Бинарный сдвиг влево (10<<10 == 1000)
3 >> 2 == 0 #   Бинарный сдвиг вправо (3>>2 == 00)
3 >> 1 == 1 #   (3 >> 1 == 01)
"""



#   Подмена переменных без буфера
"""
swap1 = 8
swap2 = 9
swap1,swap2 = swap2, swap1
"""
#   Типы данных
"""
a = None
print(type(a))
a = 1
print(type(a))
a = 1.0
print(type(a))
a = 1+1j
print(type(a))
a = '1'
print(type(a))
a = [1, 1, 'a']
print(type(a))
a = (1, 1, 'a')
print(type(a))
a = {1, 1, 'a'}
print(type(a))
a = {'a':1, 'b':2}
print(type(a))
a = True
print(type(a))
"""
#   Конвертация типов
"""
x = '5'
x = int(x)
print(type(x))
"""
#   Проверка на целочисленность дроби (Пример)
"""
x = float(input('Введите число    '))
if x == int(x): print('da')
else: print('net')
"""



#   Условные операторы
"""
x = int(input("Введите число "))
if x>0 :
    print('Число положительное')
elif x<0 :
    print('Число отрицательное')
else:
    print('Число равно нулю')
"""
#   Инициализация булевых переменных
"""
x = 1
boolean = x == 2
print (boolean)
"""
#   Проверка ввода (обработка исключений)
"""
x = input('Введите число ')
try: 
    int(x)
except:
    print('Это не число')
    exit(0)
print('Это число')
print(int(x)+1)
"""
#   Открываем сайт из командной строки))))
"""
import os # импортируем пакет методов системы
site = input('Введите адрес сайта: ')

if 'https://' in site:
    os.system('start ' + site)
elif 'www.' in site:
    site = 'https://' + site
    os.system('start ' + sayt)
else:
    site = 'https://www.' + site
    os.system('start ' + site)
"""
#   Пробуем библиотеку time и os
"""
import time
import os

time.sleep(5) # Ожидание в секундах

os.startfile('C://Program Files/FACEIT AC/faceitclient.exe')
# запускаем файл из данной директории
"""



#   Цикл while
"""
x = 0
while x <= 5:
    print(x)
    x+=1
"""
#   Подсчет факториала (пример вложенный цикл)
"""
while True:
    x = int(input('Введите число: '))
    count = 1
    result = 1;
    while count <= x:
        result *= count
        count+=1
    print(result)
"""
#   Пример номер 2
"""
x = ''
z = int(input('Введите длину слова: '))
while len(x) < z: # len() - длина строки, массива и вообще чего угодно
    y = input('Ввод данных: ')
    x += y
else:
    print(x)
"""
#   Пример номер 3
"""
sum = 0
while True:
    x = input('Введите слогаемое: ')
    if x == 'end':
        break; # Выход из цикла
    x=int(x)
    if x <= 0:
        print('Только положительные числа!!!')
        continue # Возврат в начало цикла
    else:
        sum+=x
        print(sum)
"""



#   Цикл for
"""
m = [1,2,3,4,5]
for i in m:
    print(i)
"""
#   Пример поиска символа в строке
"""
while True:
    m = input('Введите строку:\n')
    if m == 'end':
        break;
    j = input('Введите символ:\n')
    counter = 0
    for i in m:
        if i == j:
            print('Найдено соответствие')
            counter += 1;
    print('Total counter is: ', counter)
"""
#   Тип данных list ( массив )
"""
m = [1, 2, 1, 3, 4] # индексы начинаются с нуля 
print(m[0])
print(m[len(m)-1]) # так можно взять последний элемент из списка
print(m[-1]) # или так
h = [1, 2, ['a','b'], 4]
print(h[2]) # выводим подсписок
print(h[2][0]) # выводим элемент подсписка
b = list('prikol') # превращаем тип данных (к примеру строку) в список
d = list(range(10)) # range генерирует последовательность целых чисел 0 1 2 3...
"""
#   Заполнение списка
"""
n = range(10)
m = [] # инициализация пустого списка
for i in n:
    m += [i]
else:
    print(m)
"""
#   Методы списков
"""
x = [1, 2, 3]
x.append(4) # добавляет в элемент в конец списка
x.insert(1, 7)  # вставляет на место индекса <аргумент 1> элемент <аргумент 2>
x.count(1) # считает колличество элементов <аргумент 1> в массиве
x.sort() # сортирует список по возрастанию
x.reverse() # отзеркаливает список
x.pop(2) # удаляет элемент индекса <аргумент 1> в списке
x.remove(3) # удаляет элемент <аргумент 1> в списке
x.clear() # очищает список
x.extend([1,2,3,4]) # добавляет подсписок <аргумент 1> в конец списка 
h = x.copy() # копируем список в новую переменную
"""
#   Пример ( создание и редактирование списков )
"""
x = []
while True:
    temp = input('Введите команду:\n')
    if temp == 'add':
        temp1 = int(input('Введите элемент:\n'))
        x.append(temp1)
    elif temp == 'insert':
        temp1 = int(input('Введите элемент:\n'))
        temp2 = int(input('Введите номер элемента замены:\n'))
        x.insert(temp2-1, temp1)
    elif temp == 'delete':
        temp1 = input('Введите номер элемента удаления:\n')
        x.pop(int(temp1)-1)
    elif temp == 'sort':
        x.sort()
    else:
        break;
    print(x)
"""
#   Тип данных tuple (кортеж)
#   Делаем проводник на питоне
"""
import os
import time

arr = []
for path, dirs, files in os.walk('C:\\'):
    for file in files:
        full = os.path.join(path, file)
        if '.exe' in file:
           arr.append(file)
print(arr)
"""
