# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
        with open(config_filename) as f:
                access_dict = {}
                trunk_dict = {}
                for line in f:
                        line = line.strip()
                        if line.startswith('interface Fast'):
                                int = line.split()[-1]
                                access_dict[int] = 1
                        elif 'switchport access vlan' in line:
                                vlan = line.split()[-1]
                                access_dict[int] = vlan
                        elif line.startswith('switchport trunk allowed'):
                                vlans = line.split()[-1].split(',')
                                trunk_dict[int] = [v for v in vlans]
                                del access_dict[int]
                result_tuple = (access_dict, trunk_dict)
                return result_tuple

print(get_int_vlan_map('config_sw2.txt'))
