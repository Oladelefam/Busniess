from datetime import datetime
import time

def Log(filename, Item, action):
    log_time = datetime.now()
    with open(filename, 'a') as file:
        file.write(f"\n{Item} was {action} at: {log_time}. ")

    print("The item was recorded.")

