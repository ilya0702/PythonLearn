# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


from sys import argv

file = argv[1]
ignore = ["duplex", "alias", "Current configuration"]
with open(file, 'r') as f:
	for line in f:
		for skip in ignore:
			if line.startswith('!') or skip in line:
				break
		else:
			print(line.strip())
