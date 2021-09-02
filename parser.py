import json
import os
import xmltodict
import time

with open('file1.xml', 'r') as myfile:
    obj = xmltodict.parse(myfile.read())
print(json.dumps(obj))

vehicles_list = []
for key in obj["Insurance"]:
    for i in obj["Insurance"]["Transaction"]['Customer']['Units']['Auto']['Vehicle']:
        vehicle = {
            "id": i['@id'],
            "make": i['Make'],
            "vin_number": i['VinNumber'],
            "model_year": i['ModelYear']
        }

        vehicles_list.append(vehicle)
transaction = {
    "file_name": "xml/file1.xml",
    "transaction": {
        "date": obj["Insurance"]["Transaction"]['Date'],
        "customer": {
            "id": obj["Insurance"]["Transaction"]['Customer']['@id'],
            "name": obj["Insurance"]["Transaction"]['Customer']['Name'],
            "address": obj["Insurance"]["Transaction"]['Customer']['Address'],
            "phone": obj["Insurance"]["Transaction"]['Customer']['Phone']
        },
        "vehicles": vehicles_list
    }
}
print(transaction)

with open('test_file2.json', 'w') as file:
    json.dump(transaction, file)

cwd = os.getcwd()  # current directory
os.chdir(cwd)
timestamp = time.time()
print(os.path.basename(__file__))

with open(cwd + "/output/" + str(timestamp) + "file6.json", "w+") as f:
    json.dump(transaction, f)
