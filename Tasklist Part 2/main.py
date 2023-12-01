# Names: Dylan Garvey & Trung Ho & Brandon Wong
# Date: 12/01/23
# Desc: CLI todo which utilizes Python classes to hold information of our tasklist and tasks


from tasklist import Tasklist
from check_input import get_int_range

def main_menu() -> int:
    '''
    Prints main menu and asks for user to choose choice
    '''
    print("1. Dislpay current task\n"
          "2. Display all tasks\n"
          "3. Mark current task complete\n"
          "4. Add new task\n"
          "5. Search by date\n"
          "6. Save and quit")
    return get_int_range("Enter a choice: ", 1, 6)

def get_date() -> str:
    '''
    Prompts user multiple times for necessary data for date of task
    '''
    print("Enter due date:")
    month: str = str(get_int_range("Enter month: ", 1, 12))
    if len(month) < 2:
        month = f"0{month}"
    day: str = str(get_int_range("Enter day: ", 1, 31))
    if len(day) < 2:
        day = f"0{day}"
    year: str = str(get_int_range("Enter year: ", 2000, 3000))
    return f"{month}/{day}/{year}"

def get_time() -> str:
    '''
    Prompts user multiple times for necessary data for time of task
    '''
    print("Enter time:")
    hour: str = str(get_int_range("Enter hour: ", 0, 23))
    if len(hour) < 2:
        hour = f"0{hour}"
    minute: str = str(get_int_range("Enter minute: ", 0, 59))
    if len(minute) < 2:
        minute = f"0{minute}"
    return f"{hour}:{minute}"

def main():
    tasklist: Tasklist = Tasklist()
    while True:
        print(f"-Tasklist-\nTasks to complete: {len(tasklist)}")
        choice = main_menu()
        match choice:
            case 1:
                if len(tasklist):
                    print(f"Current task is:\n{tasklist.get_current_task()}")
                else:
                    print("All tasks are complete!")
            case 2:
                print(f"Tasks:")
                [print(f"{i+1}. {task}") for i, task in enumerate(tasklist)]
            case 3:
                if len(tasklist):
                    print(f"Marking current task as complete: {tasklist.mark_complete()}")
                    if len(tasklist):
                        print(f"New current task is: {tasklist.get_current_task()}")
                    else:
                        print("No new current tasks")
                else:
                    print("No more tasks to complete!")
            case 4:
                tasklist.add_task(input("Enter a task: "), get_date(), get_time())
            case 5:
                date: str = get_date()
                print(f"Tasks due on {date}:")
                tasks = [t for t in tasklist if t.date == date]
                if not tasks:
                    print(f"No tasks due on {date}")
                else:
                    [print(f"{i+1}. {t}") for i, t in enumerate(tasks)]
            case 6:
                tasklist.save_file()
                print("Saving List...")
                break
        print()

main()