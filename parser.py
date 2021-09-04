from xml_parser import *


def parser(file1, file2=None):
    if file1.endswith('.xml'):
        parsing_xml(file1)


parser('file1.xml')