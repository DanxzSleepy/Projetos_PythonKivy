def validate_task_input(task):
    if not task or len(task.strip()) == 0:
        return False
    return True

def format_task_display(task):
    return f"- {task}"