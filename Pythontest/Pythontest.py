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
#   Создание массива
"""

*z = [1,2,3]

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
while len(x) < z: # len() - длина строки
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
#       