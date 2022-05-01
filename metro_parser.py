from xml.etree.ElementTree import parse
from metro import Metro


def parse_metro(xml_path: str) -> Metro:

    result = Metro()
    my_tree = parse(xml_path)
    root = my_tree.getroot()
    # print(root)
    # for child in root:
    #     print(child.tag, child.attrib.get('id'))

    # for station in root.iter('station'):
    #     print(station.attrib)
    #     print(station.get('name'))

    for child in root:
        result.add_line(id=child.attrib.get('id'), color=child.attrib.get('color'))
        # for station in child.iter('station'):
        #     print(station.get('name'))
        for station in child.iter('station'):
            result.add_station_to_line(
                id=station.get('id'),
                line_id=child.attrib.get('id'),
                name=station.get('name'),
                open=station.get('open'),
                close=station.get('close'))

    return result
