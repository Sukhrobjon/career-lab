def server_time_check(task_config, task_times):
    """Determines how many tasks can be done in a given number of minutes
    NOTE: tasks must be done in a given order!
    Args:
        task_config(list): number of tasks and the max total execution time
        task_times(list): times takes for each task submitted
    Returns:
        number of tasks(int): number of tasks can be done in a given time
    """
    # converting user input into lists
    # comment this out if the input is given by user on terminal
    # task_config = task_config.split(" ")
    # task_times = task_times.split(" ")

    max_min = int(task_config[1])
    total_task_mins = 0
    tasks = []
    for index, task in enumerate(task_times, 1):
        total_task_mins += int(task)
        tasks.append(task)
        if total_task_mins <= max_min:
            continue
        else:
            print(f"index: {index-1}")
            print(f"Tasks before removing last item: {tasks}")
            tasks.pop()
            print(f"Tasks after removing last item: {tasks}")
            return


task_config = [10, 200]
task_times = [20, 70, 40, 30, 10, 27, 2, 3, 10, 5]

server_time_check(task_config, task_times)
