import json
from File import read_file, write_file
from File_exist import check_file_exist
from Table import Table_write
from Date_validation import Date_validation
from Date_log import Log


def _choose_task(file_read):
    """Helper: show tasks and return selected index or None."""
    if not file_read:
        print("No tasks found.")
        return None

    Table_write()
    try:
        selection = int(input("Enter task number to edit: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return None

    idx = selection - 1
    if idx < 0 or idx >= len(file_read):
        print("Invalid task number.")
        return None
    return idx


def Change_file(User_input):
    """Edit a task field based on the user's choice."""
    check_file_exist('Task.json')
    file_read = read_file('Task.json')

    choice = str(User_input).strip().lower()

    if choice in ('7', 'cancel'):
        print("Edit cancelled.")
        return

    # Map textual choices to handlers
    if choice in ('1', 'title'):
        idx = _choose_task(file_read)
        if idx is None:
            return
        new_title = input("Enter new title: ").strip().capitalize()
        if not new_title:
            print("Title cannot be empty.")
            return
        old = file_read[idx].get('Title')
        file_read[idx]['Title'] = new_title
        Check_input = input("Are you sure you want to save changes(y/n): ").lower()
        if Check_input == "y":
            write_file('Task.json', file_read)
            Log('Date_log.txt', new_title, 'edited title')
            print(f"Title updated: '{old}' -> '{new_title}'")
        else:
            print('Bye')
        return

    if choice in ('2', 'description', 'descripition'):
        idx = _choose_task(file_read)
        if idx is None:
            return
        new_desc = input("Enter new description: ").strip().capitalize()
        if not new_desc:
            print("Description cannot be empty.")
            return
        file_read[idx]['Descripition'] = new_desc
        Check_input = input("Are you sure you want to save changes(y/n): ").lower()
        if Check_input == "y":
            write_file('Task.json', file_read)
            Log('Date_log.txt', file_read[idx].get('Title', ''), 'edited description')
            print("Description updated.")
        else:
            print("Bye")
        return

    if choice in ('3', 'priority'):
        idx = _choose_task(file_read)
        if idx is None:
            return
        priority = input("Enter priority (High, Mid, Low): ").strip().capitalize()
        while priority not in ("High", "Mid", "Low"):
            print("Make sure it's either High, Mid, or Low")
            priority = input("Enter priority (High, Mid, Low): ").strip().capitalize()
        file_read[idx]['Priority'] = priority
        write_file('Task.json', file_read)
        Log('Date_log.txt', file_read[idx].get('Title', ''), 'edited priority')
        print("Priority updated.")
        return

    if choice in ('4', 'due', 'due date'):
        idx = _choose_task(file_read)
        if idx is None:
            return
        Due_date = input("Enter the due date - D/M/YYYY: ").strip()
        while not Date_validation(Due_date):
            Due_date = input("Enter the due date - D/M/YYYY: ").strip()
        file_read[idx]['Due_date'] = Due_date
        Check_input = input("Are you sure you want to save changes(y/n): ")
        if Check_input == 'y':
            write_file('Task.json', file_read)
            Log('Date_log.txt', file_read[idx].get('Title', ''), 'edited due date')
            print("Due date updated.")
        else:
            print("Bye")
        return

    if choice in ('5', 'complete', 'completion'):
        idx = _choose_task(file_read)
        if idx is None:
            return
        current = file_read[idx].get('Completion', False)
        new = input("Mark task as complete? (yes/no): ").strip().lower()
        if new in ('yes', 'y'):
            file_read[idx]['Completion'] = True
        elif new in ('no', 'n'):
            file_read[idx]['Completion'] = False
        else:
            print("No changes made to completion status.")
            return
        Check_input = input("Are you sure you want to save changes(y/n): ").lower()
        if Check_input == "y":
            write_file('Task.json', file_read)
            status = 'complete' if file_read[idx]['Completion'] else 'incomplete'
            Log('Date_log.txt', file_read[idx].get('Title', ''), f'marked {status}')
            print(f"Task marked {status}.")
        else:
            print("Bye")

        return

    if choice in ('6', 'edit everything', 'everything'):
        idx = _choose_task(file_read)
        if idx is None:
            return
        # Edit title
        new_title = input("Enter new title (leave blank to keep current): ").strip().capitalize()
        if new_title:
            file_read[idx]['Title'] = new_title
        # Edit description
        new_desc = input("Enter new description (leave blank to keep current): ").strip().capitalize()
        if new_desc:
            file_read[idx]['Descripition'] = new_desc
        # Edit priority
        priority = input("Enter priority (High, Mid, Low) (leave blank to keep current): ").strip().capitalize()
        if priority:
            while priority not in ("High", "Mid", "Low"):
                print("Make sure it's either High, Mid, or Low")
                priority = input("Enter priority (High, Mid, Low): ").strip().capitalize()
            file_read[idx]['Priority'] = priority
        # Edit due date
        Due_date = input("Enter the due date - D/M/YYYY (leave blank to keep current): ").strip()
        if Due_date:
            while not Date_validation(Due_date):
                Due_date = input("Enter the due date - D/M/YYYY: ").strip()
            file_read[idx]['Due_date'] = Due_date
        Check_input = input("Are you sure you want to save changes(y/n): ")
        if Check_input == 'y':
            write_file('Task.json', file_read)
            Log('Date_log.txt', file_read[idx].get('Title', ''), 'edited everything')
            print("Task updated.")
        else:
            print("Bye")
        return

    print("Unknown choice. No changes made.")
            