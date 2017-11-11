#!/usr/bin/python -u

# usage: $ python csv2xml.py <file_with_translations>.csv

import csv
from lxml import etree
import sys
import os

path_file_csv = raw_input("Path to CSV file : ")

reader = csv.reader(open(path_file_csv, "rb"))
translations = []
roots = []
current_path = os.getcwd()

for row in reader:
    if row[0] == "arbotena":
        translations = row
        translations.pop(0)
        break

for translation in translations:
    roots.append(etree.Element("resources"))

translations.remove("_ios")
translations.remove("_android")
translations.remove("_sketch")
translations.remove("detail")

for row in reader:
    if row[0] != "arbotena":
        if row[0] != "General":
            number_of_translations = len(row) - 1
            for i in range(0, number_of_translations):
                string_resource = etree.SubElement(roots[i], "string")
                string_resource.set("name", row[0])
                string_resource.text = row[i + 1].decode('utf-8')
                if number_of_translations == 1:
                    string_resource.set("translatable", "false")

xml_file_header = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"

for i in range(0, len(translations)):
    android_dir = current_path + "/app/src/main/res/values"
    if translations[i] != "en" : 
        android_dir += "-"+translations[i].lower()
    if not os.path.exists(android_dir):
        os.makedirs(android_dir)
    xml_string = etree.tostring(roots[i], encoding='unicode', method='xml', pretty_print=True, xml_declaration=False)
    pretty_xml_string = xml_file_header
    pretty_xml_string += xml_string 
    xml_file = open(android_dir + "/strings.xml", "w")
    xml_file.write(pretty_xml_string.encode('utf-8'))
    xml_file.close()