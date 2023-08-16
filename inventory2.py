from pathlib import Path
from nornir import InitNornir
from nornir.core.inventory import Inventory


def select_devices(joblist: dict) -> Inventory:
    """
    Generate a Nornir inventory containing only the needed devices for
    this job and enhance this inventory with job and parameters to 
    be run on this host

    Args:
        joblist (dict): [hostname: str, jobname: str|Callable, parameters, ...]

    Returns:
        Inventory: Nornir inventory object
    """
    
    inventory_dir = Path() / 'inventory' 
    host_file  =    str(inventory_dir / 'hosts.yaml')
    group_file =    str(inventory_dir / 'groups.yaml')
    defaults_file = str(inventory_dir / 'defaults.yaml')

    selection = InitNornir(
        inventory={
            'plugin': 'SimpleInventory',
            'options': {
                'host_file':     host_file,
                'group_file':    group_file,
                'defaults_file': defaults_file
            },
        },
        runner={
            'plugin': 'threaded',
            'options': {
                'num_workers': 10,
            },
        },
        logging={
            'enabled': True,
            'log_file': 'nornir.log',
            'level': 'DEBUG'
        }
    ).filter(filter_func=lambda host: host.name in joblist.keys())

    hosts_list =  selection.inventory.hosts.keys()
    groups_list = selection.inventory.groups.keys()
    
    for name, params in joblist.items():
        if name in hosts_list:
            selection.inventory.hosts[name].data = params
        elif name in groups_list:
            selection.inventory.groups[name].data = params
        elif name == 'defaults':
            selection.inventory.defaults.data = params

    return selection
