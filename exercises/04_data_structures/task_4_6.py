# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
list1 = ospf_route.replace('via', '').replace(',', '').strip().split()
print('{:20}{:20}'.format('Prefix', list1[0]))
print('{:20}{:20}'.format('AD/Metric', list1[1][1:-1]))
print('{:20}{:20}'.format('Next-Hop', list1[2]))
print('{:20}{:20}'.format('Last update', list1[3]))
print('{:20}{:20}'.format('Outbound Interface', list1[4]))
