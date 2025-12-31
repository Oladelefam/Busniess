#Done
from Edit_file import Change_file
from Date_validation import Date_validation
from File import read_file, write_file
from rich.table import Table
from File_exist import check_file_exist
from Table import Table_write
from Date_log import Log

print(str("===== Task Manager ====\n").center(30))

print("""1.) Add Task
2.) List Tasks
3.) Delete Task
4.) Edit task
5.) Quit\n""")

print("==========================")


def add_task(title, Prior, due_date, descripition):


    Task = {"Title": title,
            "Descripition": descripition,
            "Priority": Prior,
            "Due_date": due_date,
            "Completion": False}
     
    check_file_exist('Task.json')
    file_read = read_file("Task.json")
    
    file_read.append(Task) 
    write_file("Task.json", file_read) 
    Log('Date_log.txt', title, "added")
    print("Task added!!")


def Del_task():

    check_file_exist('Task.json')
    input_user = input("Would you rather delete all the task - type yes - or delete a specific task (type no): ").strip().lower()

    file_read = read_file("Task.json")

    if input_user == 'yes':
        file_read.clear()
        write_file("Task.json", file_read)
        print("All tasks deleted.")
    elif input_user == 'no':
        Del_input = input("What task do you want delete (enter number or exact title): ").strip()

        # try treating input as a number first
        try:
            num = int(Del_input)
            if 0 <= num < len(file_read):
                removed = file_read.pop(num)

                write_file("Task.json", file_read)
                print(f"You've removed a task: {removed.get('Title')}")


            else:
                print("Invalid task number.")
        except ValueError:
            for item in list(file_read):
                if item.get('Title') == Del_input:
                    file_read.remove(item)
                    write_file("Task.json", file_read)
                    print("You've removed a task.")
                    break
            else:
                print("Task not found.")
        Log('Date_log.txt', Del_input, 'Deleted')
    else:
        print("No changes made.")


def main():

    while True:
        User_input = input("\nEnter the number of the choice or type quit to exit: ")

        if User_input == '1' or str(User_input).capitalize() == "Add task": # the new line of code brings up an error.

            try:
                Title = input("\nEnter task title: ").capitalize()

                while len(Title) == 0:
                    Title = input("\nEnter task title: ").capitalize()
                
                Desc = input("\nEnter the descripition of your task: ").capitalize()

                while len(Desc) == 0:
                    Desc = input("\nEnter the descripition of your task: ").capitalize()


                priority = input("\nEnter priority level for task - Low, Mid, High: ").strip().capitalize()
                
                while priority not in ("High", "Mid", "Low"):
                    print("Make sure it's either High, Mid, or Low")
                    priority = input("\nEnter priority level for task - Low, Mid, High: ").strip().capitalize()
        

                due = True
                Due_date = input("\nEnter the due date- D/M/YYYY: ")

                while due:
                    Time = Date_validation(Due_date)

                    if Time == True:
                        due = False
                    else:
                        Due_date = input("\nEnter the due date- D/M/YYYY: ")


                add_task(Title, priority, Due_date, Desc)
            except Exception as Exe:
                print(f"The python code just discovered a {Exe}")

        elif User_input == '2' or str(User_input).capitalize() == "List task":
            Table_write()
        elif User_input == '3' or str(User_input).capitalize() == "Delete task":
            Del_task()
        elif User_input == '4' or str(User_input).capitalize() =="Edit task":
            print("""What do you want to edit?
        1. Title
        2. Description
        3. Priority
        4. Due Date
        5. Mark Complete / Incomplete
        6. Edit everything
        7. Cancel
        """)
            change_input = input("Enter what you would like to edit or type cancel to exit the program: ")
            Change_file(change_input)
       
        elif User_input == 'quit':
            exit("Bye")
        else:
            print("Invalid input")
main()        
