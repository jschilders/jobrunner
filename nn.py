from jobrunner import select_devices, run_job, hello_world_1, hello_world_2
from nornir_utils.plugins.functions import print_result

# hostname, task, parameters
jobs = {
    'pe1.gs':    [ hello_world_1, 'parm1', 'parm2' ],
    'pe1.eqam7': [ hello_world_2, 'parm3', 'parm4' ],
    'br1.gs':    [ hello_world_1, 'parm5', 'parm6' ]
}

selection = select_devices(joblist=jobs)
results = selection.run(task=run_job)
print_result(results)
