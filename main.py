import metro_line
import metro_xml
import xml_util

print(xml_util.validate('data.xml', 'data.xsd'))
metro = metro_xml.parse_metro('data.xml')
metro_xml.write_metro('output.xml', metro)

print('end')

import re

new_str = "73 Japan Germany Paris 36"
output = re.findall(r'\d+', new_str)[-1]
print("Last number in string:", output)

new_string = "Elijah Oliva 89"  # Another method
result = re.search(r"\d", new_string)
if result:
    print("Number found at index", result.start())
else:
    print("Number not found")

print(str(metro_line.get_last_number('tefeaaer314feafae12365')))