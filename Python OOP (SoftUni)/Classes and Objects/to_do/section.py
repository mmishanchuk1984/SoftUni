from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.comleded_tasks = 0

    def add_task(self, new_task: Task):
        if new_task not in Task.tasks:
            Task.tasks.append(new_task)
            return f"Task {Task.details(new_task)} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        if task_name in Task.tasks:
            Task.completed = True
            self.comleded_tasks += 1
            Task.tasks.remove(task_name)
            return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        return f"Cleared {self.comleded_tasks} tasks."

    def view_section(self):
        nl = "\n"
        to_do = f"Section {self.name}:{nl}{nl.join([Task.details(i) for i in Task.tasks])}"
        return to_do


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())

