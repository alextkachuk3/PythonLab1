from lxml import etree
import xml.etree.ElementTree as ET
import time


def validate(xml_path: str, xsd_path: str) -> bool:
    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)
    return result


def xml_str_to_time(time_string: str) -> time.struct_time:
    return time.strptime(time_string, '%H:%M:%S')


def time_to_xml_str(_time: time.struct_time):
    return time.strftime('%H:%M:%S', _time)

def elements_equal(e1, e2):
    if e1.tag != e2.tag:
        return False
    if e1.text != e2.text:
        if  e1.text!=None and e2.text!=None :
            return False
    if e1.tail != e2.tail:
        if e1.tail!=None and e2.tail!=None:
            return False
    if e1.attrib != e2.attrib:
        return False
    if len(e1) != len(e2):
        return False
    return all(elements_equal(c1, c2) for c1, c2 in zip(e1, e2))



def is_two_xml_equal(f1, f2):
    tree1 = ET.parse(f1)
    root1 = tree1.getroot()
    tree2 = ET.parse(f2)
    root2 = tree2.getroot()
    return elements_equal(root1,root2)

