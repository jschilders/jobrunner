from netbox.confabulator.jobrunner.configger import select_devices, run_job
from nornir_utils.plugins.functions import print_result

jobs = {
    'pe1.gs':    { 'parm1': 'test', 'parm2': 'test' },
    'pe1.eqam7': { 'parm3': 'test', 'parm4': 'test' },
    'br1.gs':    { 'parm5': 'test', 'parm6': 'test' }
}

selection = select_devices(joblist=jobs)
results = selection.run(task=run_job)
print_result(results)


