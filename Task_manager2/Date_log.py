from datetime import datetime
import time

def Log(filename, Item, action):
    log_time = datetime.now()
    with open(filename, 'w') as file:
        file.write(f"{Item} was {action} at: {log_time}.\n ")
    print("The item was recorded.")

