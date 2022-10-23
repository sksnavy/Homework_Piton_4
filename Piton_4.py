# Задача №1: Вычислить число Пи c заданной точностью d. Пример:
# при d = 0.001, π = 3.141
# 10^(-1)≤d≤10^(-10)

# Задача №2: Задайте натуральное число N.
#  Напишите программу, которая составит список простых множителей числа N.

# Задача №3: Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Задача №4: Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл text.txt
# многочлен степени k. 
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Задача №5: Даны два файла, в каждом из которых находится запись многочлена. 
# Cформировать файл, содержащий сумму многочленов.

print ('Введите номер задания (1-5): ')
n = int (input ())

if n==1: # № 1
    from math import pi
    print ('Введите число точности вывода числа Пи: ')
    d = int (input ())
    print ( f'Число Пи с точностью {d} = { round (pi, d)}')

elif n==2: # № 2
    print ('Введите натуральное число: ')
    N2 = int (input ())
    q = 2 
    ch = []
    
    while q <= N2:
        if N2 % q == 0:
            ch.append(q)
            N2 //= q
            q = 2
        else:
            q = q+1
    
    print( f"Простые множители: {ch}")
    
elif n==3: # №3
    ch = list (map (int, input("Введите список чисел (через пробел):").split ()))
 
    ch2 = []
    [ch2.append(q) for q in ch if q not in ch2]

    print( f"Список неповторяющихся элементов исходного списка: {ch2}")

elif n==4: # №4

    def file_w (st):  # Запись строки в файл
        with open('text.txt', 'w') as q:
            q.write (st)

    import random

    def ch_rnd (k):  # Генерация случайного списка
        ch = [random.randint(0,100) for i in range (k+1)]
        return ch

    def string_ch (st):  # Получение строки
        ch = st[ ::-1 ]
        st1 = ''
        if len( ch ) < 1:
            st1 = 'x = 0'
        else:
            for i in range (len (ch)):
                if i != len (ch) - 1 and ch [i] != 0 and i != len (ch) - 2:
                    st1 = st1 + f'{ch [i]} x^ {len (ch) - i - 1}'
                    if ch [i+1] != 0:
                        st1 = st1 + ' + '
                elif i == len (ch) - 2 and ch [i] != 0:
                    st1 = st1 + f'{ch [i]} x '
                    if ch [i+1] != 0:
                        st1 = st1 + ' + '
                elif i == len (ch) - 1 and ch [i] != 0:
                    st1 = st1 + f'{ch [i]} = 0'
                elif i == len (ch) - 1 and ch [i] == 0:
                    st1 = st1 + ' = 0'
        return st1

    print ('Введите натуральную степень k: ')
    k = int ( input ())
    spisok = ch_rnd (k)
    file_w (string_ch (spisok))

elif n==5: # №5

    from itertools import * # Подключаем полезный модуль itertools
    import os # Подключаем полезный модуль os

    def make_mch ( n, koef ):  # Создаем полином со степенью n и коэффициентами koef
        ch = ['*x^']*( n-1 ) + ['*x']
        mch = [[ i1, i2, i3 ] for i1, i2, i3 in zip_longest ( koef, ch, range ( n, 1, -1 ), fillvalue='') if i1 != 0]
        
        for q in mch:
            q.append(' + ')
        mch = list (chain ( *mch ))
        mch [-1] = ' = 0'
        return "".join( map( str, mch )).replace(' 1*x', ' x')

    def analiz_mch (ch):  # Анализ многочлена
        ch.replace ( '= 0', '' )
        ch = ch.split (' + ')
        ch = [ i[0] for i in ch ]

        for i in range (len (ch)):
            if ch [i] == 'x':
                ch [i] = '1'
        ch = ch [::-1]

        return ch

    # Тело

    with open ('mch_1.txt', 'w', encoding='utf-8') as file:
        file.write('5*x^3 + 3*x^2 + 4*x + 5 = 0')
    with open ('mch_2.txt', 'w', encoding='utf-8') as file:
        file.write('7*x^3 + 2*x^2 + 2*x + 1 = 0')
    
    with open('mch_1.txt','r') as file:
        st1 = file.readline()
        print(f"Первый многочлен {st1}")
        st1_1 = analiz_mch (st1)
        print (st1_1)
        koef_mch_1 = list( map ( int, analiz_mch (st1)))
        
    with open('mch_2.txt','r') as file:
        st2 = file.readline()
        print(f"Второй многочлен {st2}")
        st2_1 = analiz_mch (st2)
        print (st2_1)
        koef_mch_2 = list( map ( int, analiz_mch (st2)))

    koef_add = list(map( sum, zip_longest ( koef_mch_1, koef_mch_2, fillvalue=0)))
    koef_add = koef_add [::-1]
    print (koef_add)

    itog_mch = make_mch ( len ( koef_add ) - 1, koef_add)
    
    print('Итоговый многочлен: ', itog_mch )
    with open ('itog.txt', 'w', encoding='utf-8') as file:
        file.write (itog_mch)

else:
    print ('Номер задания должен быть от 1 до 5 !!!')


