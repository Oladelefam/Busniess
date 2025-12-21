import json

def read_file(filename):
    with open(filename, 'r') as Read:
        file_read = json.load(Read)
        return file_read

def write_file(filename, cont):
    with open(filename, 'w') as Write:
        json.dump(cont, Write, indent=5)

        