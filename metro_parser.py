from xml.etree.ElementTree import parse
from metro import Metro


def parse_metro(xml_path: str) -> Metro:

    result = Metro()
    my_tree = parse(xml_path)
    root = my_tree.getroot()
    print(root)
    for child in root:
        print(child.tag, child.attrib.get('id'))

    for station in root.iter('station'):
        print(station.attrib)
        print(station.get('name'))

    return result
