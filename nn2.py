from jobrunner import run_jobs
from nornir_utils.plugins.functions import print_result

# hostname, task, parameters
jobs = {
    'pe1.gs':    [ 'hello_world_1', 'parm1', 'parm2' ],
    'pe1.eqam7': [ 'hello_world_2', 'parm3', 'parm4' ],
    'br1.gs':    [ 'hello_world_1', 'parm5', 'parm6' ]
}

results = run_jobs(jobs)
print_result(results)
