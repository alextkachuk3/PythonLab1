from xml.etree.ElementTree import parse, Element, ElementTree, SubElement
from metro import Metro
from xml_util import time_to_xml_str


def parse_metro(xml_path: str) -> Metro:
    result = Metro()
    my_tree = parse(xml_path)
    root = my_tree.getroot()

    for child in root:
        result.add_line(id=child.attrib.get('id'), color=child.attrib.get('color'))
        for station in child.iter('station'):
            result.add_station_to_line(
                id=station.get('id'),
                line_id=child.attrib.get('id'),
                name=station.get('name'),
                open=station.get('open'),
                close=station.get('close'))

    return result


def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def write_metro(xml_path: str, metro: Metro):
    root = Element('metro_lines')
    for line in metro.lines:
        line_el = SubElement(root, 'metro_line', id=line.id, color=line.color)
        for station in line.stations:
            SubElement(line_el,
                       'station',
                       id=station.id,
                       name=station.name,
                       open=time_to_xml_str(station.open),
                       close=time_to_xml_str(station.close))

    indent(root)
    tree = ElementTree(root)
    tree.write(xml_path)
