import metro_line
import metro_xml
import xml_util

print(xml_util.validate('data.xml', 'data.xsd'))
metro = metro_xml.parse_metro('data.xml')
metro_xml.write_metro('output.xml', metro)
print('end')
print(str(metro_line.get_last_number('tefeaaer314feafae12365')))