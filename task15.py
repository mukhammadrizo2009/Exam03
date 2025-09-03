class TodoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task: str):
        if task not in self.tasks:
            self.tasks.append(task)
            
    def show_tasks(self):
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")


todo = TodoList()
todo.add_task("Do homework")
todo.add_task("Clean room")
todo.show_tasks()