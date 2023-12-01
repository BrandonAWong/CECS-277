class Task:
    def __init__(self, desc: str, date: str, time: str):
        self._description: str = desc
        self._date: str = date
        self._time: str = time

    @property
    def date(self):
        return self._date

    def __str__(self):
        return f"{self._description} - Due: {self.date} at {self._time}"

    def __repr__(self):
        return f"{self._description},{self.date},{self._time}"

    def __lt__(self, other):
        taskDate = [int(x) for x in self.date.split('/')]
        otherDate = [int(x) for x in other.date.split('/')]
        taskTime = [int(x) for x in self._time.split(':')]
        otherTime = [int(x) for x in other._time.split(':')]
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
            return self._description.lower() < other._description.lower()
        
        