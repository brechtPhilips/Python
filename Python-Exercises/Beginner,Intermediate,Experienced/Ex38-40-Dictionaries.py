#Acces the last name of the second employee
import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

#Answer
print(d["employees"][1]["lastName"])

#Please update the dictionary by changing the last name of the second employee
# from Smith to Smooth or to whatever takes your fancy.
d["employees"][1]["lastName"] = "Smooth"
print(d["employees"][1]["lastName"])

#Please add a new employee to the dictionary.

d["employees"].append({"firstName": "Albert","lastName": "bert"})
#or
d["employees"].append(dict(firstName= "Bronn", lastName = "Grey"))

for emp in d["employees"]:
    print(emp["firstName"]+','+emp['lastName'])

#Store the dictionary in a json file.
#sort_keys=True  tells Python to preserve the order of the dictionary thrown in the file.
with open("Files/DicToJson.json",'w') as file:
    json.dump(d,file,indent=4,sort_keys=True)