from pprint import pprint

def get_data_from_inventory(selection):

    print('-'*30)
    print('Defaults')
    print('-'*30)  

    pprint(selection.inventory.defaults.data, indent=2)

    print('-'*30)  
    print('Groups')
    print('-'*30)  

    for name, group in selection.inventory.groups.items():
        print(name, end=': ')
        pprint(group.extended_data(), indent=2)

    print('-'*30)
    print('Hosts')
    print('-'*30)  

    for name, host in selection.inventory.hosts.items():
        print(name, end=': ')
        pprint(host.extended_data(), indent=2)

    print('-'*30)  
