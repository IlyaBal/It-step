class Task:
    def __init__ (self, state, name, about, deadline):
        self.state = state
        self.name = name
        self.about = about
        self.deadline = deadline



class Taskmanager:
    def __init__(self):
        self.tasks = []
    def add(self, task):
        self.tasks.append(task)

    #def delete(self):
       # print(self.tasks.remove())
    def isready(self):
        print("ready")
    def show_list(self):
        for i in self.tasks:
            print(f'name: {i.name}/ about task:{i.about}/ state:{i.state}/ deadline:{i.deadline}')

manager = Taskmanager()
manager.add(Task(True, "buy tea", "buy tea in a shop", 9))
manager.add(Task(False, "write report", "write annual report", 15))
manager.show_list()