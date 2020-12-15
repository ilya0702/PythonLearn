access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}


def generate_access_config(intf_vlan_mapping, access_template):
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
    return result


res = generate_access_config(access_config, access_mode_template)
print(res)

