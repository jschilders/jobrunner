from nornir.core.task import Task, Result

def hello_world_1(task: Task, params: list = None) -> Result:
    """
    Sample task for Nornir

    Args:
        task (Task): Nornir Task object
        params (list, optional): Optional list of parameter. Defaults to None.

    Returns:
        Result: Nornir Result object
    """
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world! {params}"
    )

def hello_world_2(task: Task, params: list = None) -> Result:
    """
    Sample task for Nornir

    Args:
        task (Task): Nornir Task object
        params (list, optional): Optional list of parameter. Defaults to None.

    Returns:
        Result: Nornir Result object
    """
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world too! {params}"
    )
