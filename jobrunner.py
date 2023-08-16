import logging
from typing import Callable
from nornir.core.task import Task, Result

from inventory import select_devices
from jobs import hello_world_1, hello_world_2

job_table = {
    "hello_world_1": hello_world_1,
    "hello_world_2": hello_world_2,
}

def build_job_table() -> dict:
    """
    Build a table of Nornir tasks.
    Find callable objects (functions) in globals() that have 
    a parameter 'task' in their annotations which is of type 
    <class 'nornir.core.task.Task'>
    Returns:
        dict [str: function_name:, Callable: function]
    """
    _job_table={}
    for _object in globals().copy().values():
        if _annotated_object := getattr(_object, '__annotations__', None):
            if _annotated_object_class := _annotated_object.get('task', None):
                if isinstance(_object, Callable) and str(_annotated_object_class) == "<class 'nornir.core.task.Task'>" : # Beeeh
                    _job_table[_object.__name__] = _object   
    return _job_table         


def get_function_too(name: str) -> Callable:
    """
    Return the function if supplied with (valid) fuction name.
    Abstracted to easily switch methods

    Args:
        name (str): Name of the function

    Returns:
        Callable: Function
    """
    return build_job_table().get(name)
        
    
def get_function(name: str) -> Callable:
    """
    Return the function if supplied with (valid) fuction name.
    Abstracted to easily switch methods

    Args:
        name (str): Name of the function

    Returns:
        Callable: Function
    """
    return globals().get(name)


def run_jobs(joblist: dict) -> Result:
    """
    Run a jobs on host, as specified in joblist

    Args:
        joblist (dict): Dictionary describing what jobs to run on what hosts.

    Returns:
        Result: Nornir Result object
    """
    return select_devices(joblist).run(task=run_job)


def run_job(task: Task) -> Result:
    """
    Execute sub-task (job) depending on the host we're running against.

    Args:
        task (Task): Task object from Nornir

    Returns:    
        Result: Object containing result of this task
    """
    params = task.host.data['params']
    job = task.host.data['job']
    
    # Check if the actual function is referenced, or just the name as a string
    if not isinstance(job, Callable):
        job = get_function(job)

    task.run(task=job, params=params)

    return Result(
        severity_level=logging.DEBUG,
        host=task.host,
        result=f"Running job {job.__name__!r} on host {task.host.name!r} with parameters {params!r}"
    )
