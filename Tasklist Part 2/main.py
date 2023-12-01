# Names: Brandon Wong & Trung Ho
# Date: 9/26/2023
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
          "5. Save and quit")
    return get_int_range("Enter a choice: ", 1, 5)

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
                print(f"Current task is:\n{tasklist[0]}")
            case 2:
                print(f"Tasks:")
                [print(task) for task in tasklist]
            case 3:
                if len(tasklist) >= 1:
                    print(f"Marking current task as complete: {tasklist[0]}")
                    tasklist.mark_complete()
                    if len(tasklist) > 0:
                        print(f"New current task is: {tasklist[0]}")
                    else:
                        print("No new current tasks")
                else:
                    print("No more tasks to complete!")
            case 4:
                tasklist.add_task(input("Enter a task: "), get_date(), get_time())
            case 5:
                tasklist.save_file()
                break
        print()

main()