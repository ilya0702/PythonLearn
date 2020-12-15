access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

def generate_access_config(intf_vlan_mapping, access_template, psecurity = None):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    result = []
    for key, value in intf_vlan_mapping.items():
        result.append(key)
        for comm in access_template:
            if comm.startswith('switchport access vlan'):
                comm = comm + ' ' + str(value)
                result.append(comm)
            else:
                result.append(comm)
        if psecurity:
            for coms in psecurity:
                result.append(coms)
    return result

res = generate_access_config(access_config, access_mode_template, port_security_template)
print(res)

