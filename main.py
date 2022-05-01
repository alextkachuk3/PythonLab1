import time

import metro_parser
import xml_util
from metro import Metro
from metro_line import MetroLine

test = Metro()

test.add_line(id="l1", color='blue')
test.add_line(id="l3", color='green')
test.add_line(id="l2", color='red')

# test.delete_line(3)

print(xml_util.validate('data.xml', 'data.xsd'))


test.update_color("l3", 'pink')

test.add_station_to_line('l2', name='Zoloti Vorota', open='12:00:00', close='23:00:11')

meow = metro_parser.parse_metro('data.xml')

print('end')
