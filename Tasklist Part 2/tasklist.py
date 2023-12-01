from task import Task


class Tasklist:
    def __init__(self):
        with open("tasklist.txt", 'r') as f:
            f_list = [[info for info in task.replace('\n', '').split(',')] for task in f.readlines()]
        self._tasklist: list[Task] = sorted([Task(task[0], task[1], task[2]) for task in f_list])
        
    def add_task(self, desc: str, date: str, time: str) -> None:
        '''
        Adds a task into the stack
        '''
        self._tasklist.append(Task(desc, date, time))
        self._tasklist.sort()

    def mark_complete(self) -> None:
        '''
        Completes the list on the top of the stack and gets removed
        '''
        self._tasklist.pop(0)

    def save_file(self) -> None:
        '''
        Tasklist is saved into txt file
        '''
        with open("tasklist.txt", 'w') as f:
            f.write('\n'.join([repr(task) for task in self.tasklist]))
    
    def __getitem__(self, index: int):
        return self._tasklist[index]

    def __len__(self):
        return len(self._tasklist)