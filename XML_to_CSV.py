import xml.etree.ElementTree as ET
import csv

filexml = raw_input("> ") #enter file name in format name.xml

tree = ET.parse(filexml)
root = tree.getroot()

items_data = open('parsed_xml.csv', 'w') #parsed_xml.csv is default name for result csv, you may change it

csvwriter = csv.writer(items_data)

for items in root.findall('item'): #item is a name for parrental block
    for item1 in items.findall('item1'): #item1 is name for subling block
        item1_head = []

        it = items.get('name') #here we want take atribute name from subling item1
        item1_head.append(it.encode("utf-8")) # if you using ASCII delete .encode("utf-8") part

        csvwriter.writerow(item1_head)


items_data.close()
