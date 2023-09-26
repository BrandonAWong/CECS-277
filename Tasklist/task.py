class Task:
    def __init__(self, desc: str, date: str, time: str):
        self.description: str = desc
        self.date: str = date
        self.time: str = time

    def __str__(self):
        return f"{self.description} - Due: {self.date} at {self.time}"

    def __repr__(self):
        return f"{self.description},{self.date},{self.time}"

    def __lt__(self, other):
        taskDate = [int(x) for x in self.date.split('/')]
        otherDate = [int(x) for x in other.date.split('/')]
        taskTime = [int(x) for x in self.time.split(':')]
        otherTime = [int(x) for x in other.time.split(':')]
        if taskDate[2] != otherDate[2]:
            return taskDate[2] < otherDate[2]
        elif taskDate[0] != otherDate[0]:
            return taskDate[0] < otherDate[0]
        elif taskDate[1] != otherDate[1]:
            return taskDate[1] < otherDate[1]
        elif taskTime[0] != otherTime[0]:
            return taskTime[0] < otherTime[0]
        elif taskTime[1] != otherTime[1]:
            return taskTime[1] < otherTime[1]
        else:
            return self.description < other.description
        
        