import logging
from nornir.core.task import Task, Result, MultiResult
from nornir_jinja2.plugins.tasks import template_file, template_string

def config_cisco_ios(task: Task, **kwargs) -> Result:
    template = task.run(task=string_from_template, **kwargs)
    print(type(template))
    return template


def config_junos(task: Task, **kwargs) -> Result:
    template = task.run(task=string_from_template, **kwargs)[1].result
    
    #print(type(template[0].result))
    
    step_1_result = task.run(task=step_1, **kwargs)
    
    step_2_result = task.run(task=step_2, **kwargs)
    
    return Result(
        host=task.host,
        result=f"Configured host {task.host.name} with template {template}"
    )


def string_from_template(task: Task, **kwargs):

    template_from_file     = kwargs.pop('template', None)
    template_from_string   = kwargs.pop('template_str', None)
    template_path          = kwargs.pop('path', '')

    if template_from_string:
        result = task.run(task=template_string, 
                        template=template_from_string, 
                        task_name=task.name, 
                        task_host=task.host, 
                        **kwargs
                    )

    elif template_from_file:
        result = task.run(task=template_file, 
                        template=template_from_file, 
                        path=template_path,
                        task_name=task.name, 
                        task_host=task.host, 
                        **kwargs
                    )
        
    return Result(
        severity_level=logging.DEBUG,
        host=task.host,
        result=result
    )
    
    
def step_1(task: Task, **kwargs) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} performed step 1"
    )

def step_2(task: Task, **kwargs) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} performed step too!"
    )

