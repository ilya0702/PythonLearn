nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
natnew = nat.replace('Fast', 'Gigabit')
print(natnew)

