import metro_xml
import xml_util
print(xml_util.validate('data.xml', 'data.xsd'))
meow = metro_xml.parse_metro('data.xml')
metro_xml.write_metro('output.xml', meow)

print('end')
