import csv
import json
import os
import time


def parsing_csv(csv_customer_file, csv_vehicle_file):
    with open(csv_customer_file, encoding='utf-8') as csvf_customers, open(csv_vehicle_file,
                                                                           encoding='utf-8') as csvf_vehicles:
        csvCustomers = csv.DictReader(csvf_customers)
        csvVehicles = csv.DictReader(csvf_vehicles)

        transactions = []
        vehicles_list_for_customer = []
        for rows in csvCustomers:
            for records in csvVehicles:
                if records['owner_id'] == rows['id']:
                    vehicle = {
                        "id": records['id'],
                        "make": records['make'],
                        "vin_number": records['vin_number'],
                        "model_year": records['model_year']
                    }
                    vehicles_list_for_customer.append(vehicle)
            transaction = {
                "file_name": "xml/file1.xml",
                "transaction": {
                    "date": rows['date'],
                    "customer": {
                        "id": rows['id'],
                        "name": rows["name"],
                        "address": rows["address"],
                        "phone": rows["phone"]
                    },
                    "vehicles": vehicles_list_for_customer
                }
            }
            vehicles_list_for_customer = []
            csvf_vehicles.seek(0)
            next(csvVehicles)
            transactions.append(transaction)
        cwd = os.getcwd()  # current directory
        os.chdir(cwd)
        timestamp = time.time()

        cwd + "/output/xml/" + str(timestamp)
    with open(cwd + "/output/csv/" + '{:.5f}'.format(timestamp) + "_" + os.path.splitext(csv_customer_file)[0] + ".json", 'w',
              encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(transactions, indent=4))

