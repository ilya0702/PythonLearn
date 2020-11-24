# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv


ip = argv[1]
ip = ip.replace('/', '.')
list1 = ip.split('.')
mask = int(list1[-1])
ones = mask * '1'
zeros = (32 - mask) * '0'
fullmask = ones + zeros
oct1 = fullmask[0:8]
oct2 = fullmask[8:16]
oct3 = fullmask[16:24]
oct4 = fullmask[24:32]
ipbin = '{:08b}{:08b}{:08b}{:08b}'.format(int(list1[0]), int(list1[1]), int(list1[2]), int(list1[3]))
ipbin1 = ipbin[0: mask] + zeros
ioct1 = ipbin1[0:8]
ioct2 = ipbin1[8:16]
ioct3 = ipbin1[16:24]
ioct4 = ipbin1[24:32]
print('Network:')
print('{:<10}{:<10}{:<10}{:<10}'.format(int(ioct1, 2), int(ioct2, 2), int(ioct3, 2), int(ioct4, 2)))
print('{:<10}{:<10}{:<10}{:<10}'.format(ioct1, ioct2, ioct3, ioct4))
print('\n')
print('Mask:')
print('/' + list1[-1])
print('{:<10}{:<10}{:<10}{:<10}'.format(int(oct1, 2), int(oct2, 2), int(oct3, 2), int(oct4, 2)))
print('{:<10}{:<10}{:<10}{:<10}'.format(oct1, oct2, oct3, oct4))

