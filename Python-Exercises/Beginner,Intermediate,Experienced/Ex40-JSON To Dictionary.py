#Create from tje json file a dictionary

import json
from pprint import pprint

with open("Files/company1.json") as file:
    d = json.loads(file.read())

pprint(d)

#adding a new employee to the file
with open("Files/company1.json",'r+') as file:
    d = json.loads(file.read())
    d["employees"].append(dict(firstName = "Albertinus", lastName = "Severus"))
    #put the cursor to the beginning of the file
    file.seek(0)
    json.dump(d,file,indent=4,sort_keys=True)
    #deletes everything under the cursor
    file.truncate()