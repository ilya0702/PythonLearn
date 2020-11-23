# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Enter Ip Address:')
ip = ip.replace('/', '.')
list1 = ip.split('.')
print('Network:')
print('{:10}{:10}{:10}{:10}'.format(*list1))
print('{:08b}  {:08b}  {:08b}  {:08b}'.format(int(list1[0]), int(list1[1]), int(list1[2]), int(list1[3])))
print('\n')
print('Mask:')
print('/' + list1[-1])
mask = int(list1[-1])
ones = mask * '1'
zeros = (32 - mask) * '0'
fullmask = ones + zeros
oct1 = fullmask[0:8]
oct2 = fullmask[8:16]
oct3 = fullmask[16:24]
oct4 = fullmask[24:32]
print('{:<10}{:<10}{:<10}{:<10}'.format(int(oct1, 2), int(oct2, 2), int(oct3, 2), int(oct4, 2)))
print('{:<10}{:<10}{:<10}{:<10}'.format(oct1, oct2, oct3, oct4))




