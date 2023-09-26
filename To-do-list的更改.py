from datetime import datetime


class Task:
    """
    Represents a task with a description, priority, and deadline.

    """

    def __init__(self, description, priority, deadline):
        """Initializes a Task object with description, priority, and deadline.

        param description: the description of the task
        type description: str
        param priority: the priority of the task
        type priority: int
        param deadline: the deadline of the task
        type deadline: datetime or None
        """
        if not isinstance(description, str):
            raise TypeError("Sorry,task description must be a string")
        elif not isinstance(priority, int):
            raise TypeError("Sorry,task priority must be a integer")
        elif not isinstance(deadline, datetime) and deadline is not None:
            raise TypeError("Sorry,task deadline must be year,month,day")
        # Raise exception if the format of input is wrong, the exception-handling method is used all the codes here
        self.__description = str(description)
        self.__priority = int(priority)
        self.__deadline = deadline

    def get_description(self):
        """Returns the description of a Task object."""
        return self.__description

    def set_description(self, description):
        """Sets the description of a Task object."""
        if not isinstance(description, str):
            raise TypeError("Sorry,task description must be a string")
        self.__description = str(description)

    def get_priority(self):
        """Returns the priority of a Task object."""
        return self.__priority

    def set_priority(self, priority):
        """Sets the priority of a Task object."""
        if not isinstance(priority, int):
            raise TypeError("Sorry,task priority must be an integer")
        self.__priority = int(priority)

    def get_deadline(self):
        """Returns the deadline of a Task object."""
        return self.__deadline

    def set_deadline(self, deadline):
        """Sets the deadline of a Task object."""
        if not isinstance(deadline, datetime) and deadline is None:
            raise TypeError("Sorry,task deadline must be year,month,day")
        else:
            self.__deadline = deadline

    def __str__(self):
        """Returns a string representation of a Task object."""
        return f'Executing task: Description: {self.__description}, Priority: {self.__priority}, Deadline: {self.__deadline} '


class PriorityQueue:
    """Represents a task queue sorted by priority and deadline"""

    def __init__(self):
        """Initializes an empty PriorityQueue object"""
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the PriorityQueue object"""
        if not isinstance(task, Task):
            raise TypeError('Sorry,task must be a Task object')
        self.tasks.append(task)
        # Sort the tasks in the queue by priority and deadline, with the highest priority and earliest deadline first
        self.tasks = sorted(self.tasks, key=lambda x: (-x.get_priority(), x.get_deadline()))

    def remove_task(self):
        """Removes and returns the task with the highest priority and earliest deadline"""
        if not self.tasks:
            return None
        else:
            return self.tasks.pop(0)

    def peek_task(self):
        """Returns the task with the highest priority and earliest deadline"""
        if not self.tasks:
            return None
        else:
            return self.tasks[0]

    def get_tasks(self):
        """Returns all tasks currently in the PriorityQueue object"""
        return self.tasks

    def clear_tasks(self):
        """An improvement that can clear all tasks"""
        self.tasks = []


class Scheduler:
    """Represents a task scheduler used to add, remove, rearrange, and execute tasks"""

    def __init__(self):
        """Initializes a Scheduler object with a PriorityQueue object as the task queue"""
        self.__queue = PriorityQueue()

    def add_task(self, task):
        """Adds a task to the task queue using PriorityQueue's add_task method"""
        self.__queue.add_task(task)

    def remove_task(self):
        """Removes a task from the task queue using PriorityQueue's remove_task method"""
        return self.__queue.remove_task()

    def reorder_task(self, task, new_priority, new_deadline):
        """
        Rearranges a task's priority and deadline in the task queue.

        param task: the task to be rearranged
        type task: Task
        param new_priority: the new priority of the task
        type new_priority: int
        param new_deadline: the new deadline of the task
        type new_deadline: datetime or None
        """
        if not isinstance(new_priority, int):
            raise TypeError("Sorry,task priority must be a integer")
        elif not isinstance(new_deadline, datetime) and new_deadline is not None:
            raise TypeError("Sorry,task deadline must be year,month,day")
        else:
            tasks = self.__queue.get_tasks()
            for i in range(len(tasks)):
                if task == tasks[i]:
                    removed_task = tasks.pop(i)
                    removed_task.set_priority(new_priority)
                    removed_task.set_deadline(new_deadline)
                    self.__queue.add_task(removed_task)
                    # Finds the task to be rearranged through the for loop, changes its priority and deadline,
                    # and adds it back to the queue
                    break
            else:
                print("There is no that task")

    def execute_task(self):
        """Pops a task with the highest priority and earliest period from the queue."""
        task = self.__queue.remove_task()
        if task is None:
            print("No tasks to execute")
        else:
            print(task)

    def display_tasks(self):
        """Displays the current tasks in the task queue."""
        tasks = self.__queue.get_tasks()
        if tasks:
            print("Current tasks:")
            for task in tasks:
                print(f"Description: {task.get_description()}, Priority: {task.get_priority()}, "
                      f"Deadline: {task.get_deadline()}")
        else:
            print("No tasks")

    def update_task_description(self, task, new_description):
        """
        An additional method that updates the description of a task.

        param task: the task to be updated
        type task: Task
        param new_description: the new description of the task
        type new_description: str
        """
        tasks = self.__queue.get_tasks()
        for i in range(len(tasks)):
            if task == tasks[i]:
                removed_task = tasks.pop(i)
                removed_task.set_description(new_description)
                self.__queue.add_task(removed_task)
                # Finds the task to be rearranged through the for loop, changes its description,
                # and adds it back to the queue
                break
        else:
            print("There is no that task")

    def size(self):
        """An additional method that can get the numbers of current tasks"""
        return len(self.__queue.get_tasks())

    def clear_tasks(self):
        """An additional method that can clear all tasks in the queue"""
        return self.__queue.clear_tasks()


def main():
    """The basic function test"""
    scheduler = Scheduler()
    task1 = Task("Finish project", 3, datetime(2023, 5, 1))
    task2 = Task("Exam revision", 2, datetime(2023, 7, 1))
    task3 = Task("Buy groceries", 1, None)
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)
    scheduler.display_tasks()
    scheduler.execute_task()
    scheduler.display_tasks()
    scheduler.reorder_task(task3, 4, datetime(2023, 5, 10))
    scheduler.display_tasks()
    while True:
        scheduler.execute_task()
        if not scheduler.size():
            print("No tasks to execute")
            break


def main_additional_methods_test():
    """The additional test of my improvement of the program"""
    scheduler = Scheduler()
    task1 = Task("Finish project", 3, datetime(2023, 5, 1))
    task2 = Task("Exam revision", 2, datetime(2023, 7, 1))
    task3 = Task("Buy groceries", 1, None)
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)
    scheduler.display_tasks()
    scheduler.update_task_description(task2, "Do homework")
    scheduler.display_tasks()
    print(scheduler.size())
    scheduler.clear_tasks()
    scheduler.display_tasks()
    print(scheduler.size())


def interactor():
    """The simulated user interaction by me, use the input of user as command to use the scheduler """
    scheduler = Scheduler()
    print("Welcome to your task scheduler,if you need all commands,please enter 'help'")
    global dic
    while True:
        command = input("Please enter a command: ")
        if command == "add":
            description = input("Please enter the description of the task（format:str): ")
            priority = int(input("Please enter the priority of the task(format:int): "))
            deadline = input("Please enter the deadline of the task:(format:year,month,day): ")
            year, month, day = (deadline.split(","))
            deadline1 = datetime(int(year), int(month), int(day))
            task_name = str(input("Please enter the name of the task that you would like: "))
            # Let user decide the name of the task added with their character, and they can find or reorder it with their name later
            dic = {}
            # Use dictionary to achieve it
            task = Task(description, priority, deadline1)
            dic[task_name] = task
            scheduler.add_task(task)
            print("Successfully added")
            # Give some tips that users have done it
        elif command == "help":
            print("""
                    1.add   #If you would like to add a task

                    2.execute   #If you would like to execute the task with the highest priority

                    3.reorder   #If you would like to change the priority or the deadline of a task

                    4.show  #If you would like to show all the tasks

                    5.quit  #If you would like to exit

                    6.size  #If you would like to know the number of tasks

                    7.update description   #If you would like to change the description of a task

                    8.clear    #If you would like to clear all tasks
                                                                """)
            # Users can type the commands above to achieve what they would like to do
        elif command == "execute":
            if scheduler.remove_task():
                print("Successfully executed")
            else:
                scheduler.remove_task()
        elif command == "reorder":
            name = input("Please enter the name of the task:")
            # Find the task by their name, which was set by the user before
            if name not in dic:
                print("Sorry, there is no that task, please try again")
            else:
                task = dic[name]
                new_priority = int(input("Please enter new task priority: "))
                new_deadline = input("Please enter new task deadline(format:year,month,day): ")
                year, month, day = map(int, new_deadline.split(","))
                deadline = datetime(int(year), int(month), int(day))
                scheduler.reorder_task(task, new_priority, deadline)
                print("Successfully reordered")
        elif command == "show":
            scheduler.display_tasks()
        elif command == "quit":
            break
        elif command == "size":
            print(scheduler.size())
        elif command == "update description":
            name = input("Please enter the name of the task:")
            if name not in dic:
                print("Sorry, there is no that task, please try again")
            else:
                task = dic[name]
                new_description = str(input("Please enter the new description that you would like:"))
                scheduler.update_task_description(task, new_description)
                print("Successfully updated")
        elif command == "clear":
            scheduler.clear_tasks()
        else:
            print("Invalid command,please try again")


if __name__ == '__main__':
    main()
    main_additional_methods_test()
    interactor()

