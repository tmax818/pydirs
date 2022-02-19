import os

from strings import msc

def make_model(table_name, table_values = []):
    filename = f"./flask_app/models/{table_name}.py"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'a') as f:
        f.write('from ..config.mysqlconnection import connectToMySQL\n\n')
        f.write(f"class {table_name.capitalize()}:\n\n")
        f.write("    def __init__(self, data):\n")
        for val in table_values:
            f.write(f"        self.{val} = data['{val}']\n")
        

def make_config():
    filename = f"./flask_app/config/mysqlconnection.py"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'a') as f:
        f.write(msc)

def make_controllers():
    filename = f"./flask_app/controllers/friends.py"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'a') as f:
        f.write(cont)


