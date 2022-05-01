from lxml import etree
import time


def validate(xml_path: str, xsd_path: str) -> bool:
    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)
    return result


def xml_str_to_time(time_string: str) -> time.struct_time:
    try:
        result = time.strptime(time_string, '%H:%M:%S')
    except ValueError:
        print('Time should be in format HH:MM:SS')
        quit()
    return result


def time_to_xml_str(_time: time.struct_time):
    return time.strftime('%H:%M:%S', _time)
