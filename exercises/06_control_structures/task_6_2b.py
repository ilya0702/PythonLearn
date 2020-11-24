while True:
	ip = input('Enter ip-address: ')
	octlist = ip.split('.')
	ipchk = ''
	for oct in octlist:
		if len(octlist) == 4 and oct.isdigit():
			if 0 <= int(oct) <= 255:
				ipchk += oct + '.'
	if ipchk[:-1] == ip:
		break
	else:
		print('Incorrect ip-address! Enter again. \n')
		continue
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

