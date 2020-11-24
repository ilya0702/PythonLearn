# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip = input('Enter ip-address: ')
octlist = ip.split('.')
ipchk = ''
for oct in octlist:
	if len(octlist) == 4 and oct.isdigit():
		if 0 <= int(oct) <= 255:
			ipchk += oct + '.'
if ipchk[:-1] == ip:
	if ip == '0.0.0.0':
		print('unassigned')
	elif ip == '255.255.255.255':
		print('local broadcast')
	elif 1 <= int(octlist[0]) <= 223:
		print('unicast')
	elif 224 <= int(octlist[0]) <= 239:
		print('multicast')
	else:
		print('unused')
else:
	print('Неправильный IP-адрес')

