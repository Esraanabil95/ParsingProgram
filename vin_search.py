from flask import Flask, json
import csv

app = Flask(__name__)
"""
steps
get all vin numbers from vehicles file
go to api vin decoder to search with every vin number nd get its data
append this data to the object
"""


@app.route('/vehicles/DecodeVinValues', methods=['GET'])
def vin_number():
    with open('vehicles_file1.csv', "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        vin_list = []
        for lines in csv_reader:
            vin_list.append(lines[2])
        vins = vin_list[1:]
        # for i in vins:


if __name__ == '__main__':
    app.run()  # run our Flask app
