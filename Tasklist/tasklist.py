from task import Task


class Tasklist:
    def __init__(self):
        with open("tasklist.txt", 'r') as f:
            f_list = [[info for info in task.replace('\n', '').split(',')] for task in f.readlines()]
        self.tasklist = sorted([Task(task[0], task[1], task[2]) for task in f_list])
        


    def add_task(self, desc: str, date: str, time: str):
        self.tasklist.append(Task(desc, date, time))
        self.tasklist.sort()

    def mark_complete(self) -> str:
        return self.tasklist.pop(0)

    def save_file(self):
        with open("tasklist.txt", 'w') as f:
            f.write('\n'.join([repr(task) for task in self.tasklist]))
    
    def __repr__(self):
        ...

    def __getitem__(self, index: int):
        return self.tasklist[index]

    def __len__(self):
        return len(self.tasklist)