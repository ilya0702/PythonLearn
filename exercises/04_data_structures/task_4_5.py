command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
list1 = command1.split()
list2 = command2.split()
set1 = set(list1[-1].split(','))
set2 = set(list2[-1].split(','))
print(list(set1&set2))
