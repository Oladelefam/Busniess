from datetime import datetime
#gET THE day, month, year in different variables and add all of them together in to one and put it in the time parameter

def Date_validation(Time):
    Valid = True
    Date_format = "%d/%m/%Y"
    try:
        Check_date = bool(datetime.strptime(Time, Date_format))

    except ValueError as Error:

        print(f"Incorrect date format try again. {Error}.")
        Valid = False
    
    return Valid