# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

with open('ospf.txt', 'r') as file:
	for line in file:
		line = line.replace('via', ',').replace('O', '').replace(',', '').strip().split()
		print('{:20}{:20}'.format('Prefix', line[0]))
		print('{:20}{:20}'.format('AD/Metric', line[1]))
		print('{:20}{:20}'.format('Next-Hop', line[2]))
		print('{:20}{:20}'.format('Last update', line[3]))
		print('{:20}{:20}'.format('Outbound Interface', line[4]))
		print()
		
