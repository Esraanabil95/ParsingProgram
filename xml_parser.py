import json
import os
import xmltodict
import time


def parsing_xml(xmlfile):
    with open(xmlfile, 'r') as myfile:
        obj = xmltodict.parse(myfile.read())
        dump_data = json.dumps(obj)

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
    cwd = os.getcwd()  # current directory
    os.chdir(cwd)
    timestamp = time.time()

    with open(cwd + "/output/xml/" + '{:.5f}'.format(timestamp) + "_" + os.path.splitext(xmlfile)[0] + ".json", 'w',
              encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(transaction, indent=4))
