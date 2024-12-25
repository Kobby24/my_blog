import json
import os

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__),'data','data.json')
ADMINS_FILE_PATH = os.path.join(os.path.dirname(__file__),'data','admins.json')

def load_data():
    with open(DATA_FILE_PATH,'r') as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE_PATH,'w') as file:
        json.dump(data,file,indent=4)

def load_admins():
    with open(ADMINS_FILE_PATH,'r') as ad_file:
        return json.load(ad_file)