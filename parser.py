from xml_parser import *
from csv_parser import *


def parser(file1, file2=None):
    if file1.endswith('.xml'):
        parsing_xml(file1)
    elif file1.endswith('.csv') and file2.endswith('.csv'):
        parsing_csv(file1, file2)


parser('file1.xml')
parser('customers_file1.csv', 'vehicles_file1.csv')