# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess


def ping_ip_addresses(ip_address):
	avlist = []
	navlist = []
	restuple = ()
	for ip in ip_address:
		ping = subprocess.run(['ping', '-c', '3', '-n', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
		if ping.returncode == 0:
			avlist.append(ip)
		else:
			navlist.append(ip)
	restuple = (avlist, navlist)
	return restuple

if __name__ == "__main__":
	iplist = ['8.8.8.8', 'a', '8.8.4.4', 'n.n.n', 'g.g']
	print(ping_ip_addresses(iplist))

