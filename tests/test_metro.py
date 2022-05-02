import unittest

import metro_xml
import xml_util
from xml_util import is_two_xml_equal


class TestMetro(unittest.TestCase):
    def test_adding_line(self):
        metro = metro_xml.parse_metro('test_data_for_add_del.xml')
        metro.add_line('green')
        metro_xml.write_metro('output_add_line.xml', metro)
        self.assertEqual(is_two_xml_equal('output_add_line.xml', 'correct_data_after_adding_line.xml'), True)

    def test_adding_station(self):
        metro = metro_xml.parse_metro('test_data_for_add_del.xml')
        metro.add_station_to_line('l-2', 'Demiivska', '06:00:00', '23:56:00')
        metro.add_station_to_line('l-2', 'Lybidska', '06:00:00', '23:56:00')
        metro_xml.write_metro('output_add_station.xml', metro)
        self.assertEqual(is_two_xml_equal('output_add_station.xml', 'correct_data_after_adding_station.xml'), True)

    def test_deleting_line(self):
        metro = metro_xml.parse_metro('test_data_for_add_del.xml')
        metro.delete_line('l-2')
        metro_xml.write_metro('output_delete_line.xml', metro)
        self.assertEqual(is_two_xml_equal('output_delete_line.xml', 'correct_data_after_deleting_line.xml'), True)

    def test_deleting_station(self):
        metro = metro_xml.parse_metro('test_data_for_add_del.xml')
        metro.delete_station('s-1-1')
        metro.delete_station('s-2-3')
        metro.delete_station('s-2-5')
        metro_xml.write_metro('output_delete_station.xml', metro)
        self.assertEqual(is_two_xml_equal('output_delete_station.xml', 'correct_data_after_deleting_station.xml'), True)

    def test_search_station(self):
        metro = metro_xml.parse_metro('test_data_for_add_del.xml')
        station = metro.find_station('s-2-4')
        self.assertEqual(station.id, 's-2-4')
        self.assertEqual(station.name, 'Vasylkivska')
        self.assertEqual(station.open, xml_util.xml_str_to_time('06:00:00'))
        self.assertEqual(station.close, xml_util.xml_str_to_time('23:45:00'))


if __name__ == '__main__':
    unittest.main()
