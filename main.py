from lxml import etree
import xml.etree.ElementTree as ET

def validate(xml_path: str, xsd_path: str) -> bool:
    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result


if validate('data.xml', 'data.xsd'):
    print('valid!')
else:
    print('not valid')

mytree = ET.parse('data.xml')
root = mytree.getroot()
print(root)
for child in root:
    print(child.tag, child.attrib)

for station in root.iter('station'):
    print(station.attrib)