import logging
from nornir.core.task import Task, Result
from typing import Callable

from configger_inventory import select_devices
from configger_jobs import hello_world_1, hello_world_2


job_table = {
    "hello_world_1": hello_world_1,
    "hello_world_2": hello_world_2,
}


def get_job(platform: str) -> Callable:
    """
    Get the proper task for a host, based on the platform

    Args:
        platform (str): Platform name

    Returns:
        Callable: Task to execute
    """
    return job_table[platform]


def run_jobs(joblist: dict) -> Result:
    """
    Perform configuration on  hosts, as specified in joblist.

    Args:
        joblist (dict): Dictionary describing what jobs to run on what hosts.

    Returns:
        Result: Nornir Result object
    """
    return select_devices(joblist).run(task=run_job)


def run_job(task: Task) -> Result:
    """
    Perform configuration job for a specific host.

    Args:
        task (Task): Task object from Nornir

    Returns:    
        Result: Object containing result of this task
    """
    params = task.host.data['params']
    job = get_job[task.host.platform]
    
    task.run(task=job, params=params)

    return Result(
        severity_level=logging.DEBUG,
        host=task.host,
        result=f"Running job {job.__name__!r} on host {task.host.name!r} with parameters {params!r}"
    )
