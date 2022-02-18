import os
from strings import msc, cont

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


def make_flask(app_name, curr_file):
    filename = f"./{app_name}/{curr_file}"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'a') as f:
        f.write("from flask import Flask\n")
        f.write("app = Flask(__name__)\n")
        f.write('app.secret_key = "shhhhhh"\n')
    filename = f"./{app_name}/server.py"
    os.makedirs(os.path.dirname(filename), exist_ok=True) 
    with open(filename, 'a') as f:
        f.write(f"from {app_name} import app\n")

make_model('friend', ['id', 'first_name', 'last_name', 'occupation', 'created_at', 'updated_at'])
