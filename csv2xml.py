import csv
from lxml import etree
import sys
import os

path_file_csv = raw_input("Path to CSV file : ")
reader = csv.reader(open(path_file_csv, "rb"))

xml_file_header = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"
translations = []
roots = []
current_path = os.getcwd()
is_have_arg = False

for row in reader:
    if row[0] == "key":
        translations = row
        translations.pop(0)
        break

if "arg" in translations : 
    is_have_arg = True
    translations.remove("arg")

for translation in translations:
    roots.append(etree.Element("resources"))

def set_name_value_and_comment(count_loop) :
    for i in range(0, count_loop):
            if "#" in row[0]:
                comment_message = row[0].split("#")[1].decode("utf-8")
                comment = etree.Comment("=" * 15 + " "+comment_message + " " +"=" * 15)
                roots[i].append(comment)
            elif len(str(row[0])) > 1:
                string_result = row[i + 1].decode('utf-8')
                result_arg = row[len(row) - 1].split("=")
                arg_traget = "{"+result_arg[0]+"}"
                if is_have_arg and arg_traget in string_result: 
                    string_result = string_result.replace(arg_traget, result_arg[1])
                string_resource = etree.SubElement(roots[i], "string")
                string_resource.set("name", row[0])
                string_resource.text = string_result

for row in reader:
    if row[0] != "key":
        number_of_translations = len(translations)
        set_name_value_and_comment(number_of_translations)

for i in range(0, len(translations)):
    android_dir = current_path + "/app/src/main/res/values"
    if translations[i] != "en" : 
        android_dir += "-"+translations[i].lower()
    if not os.path.exists(android_dir):
        os.makedirs(android_dir)    
    xml_string = etree.tostring(roots[i], encoding='unicode', method='xml', pretty_print=True, xml_declaration=False)
    pretty_xml_string = xml_file_header
    pretty_xml_string += xml_string.replace("<!--=======", "\n  <!--=======")
    xml_file = open(android_dir + "/strings.xml", "w")
    xml_file.write(pretty_xml_string.encode('utf-8'))
    xml_file.close()