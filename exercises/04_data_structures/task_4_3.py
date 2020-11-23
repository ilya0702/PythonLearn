config = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlans = config.split()
print(vlans[-1].split(','))
