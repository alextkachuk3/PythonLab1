import time

import xml_util
from metro import Metro
from metro_line import MetroLine

test = Metro()

test.add_line(MetroLine("l1", 'blue'))
test.add_line(MetroLine("l3", 'green'))
test.add_line(MetroLine("l2", 'red'))

# test.delete_line(3)

print(xml_util.validate('data.xml', 'data.xsd'))


test.update_color("l3", 'pink')

test.add_station_to_line('l2', name='Zoloti Vorota', open='12:00:00', close='23:00:11')
print('end')
