import filecmp
import unittest

import metro_xml


class TestMetro(unittest.TestCase):
    def test_adding_line(self):
        metro = metro_xml.parse_metro('test_data_for_add_del.xml')
        metro.add_line('green')
        metro_xml.write_metro('output_add_line.xml', metro)
        self.assertEqual(filecmp.cmp('output_add_line.xml', 'correct_data_after_adding_line.xml'), True)

    def test_adding_station(self):
        metro = metro_xml.parse_metro('test_data_for_add_del.xml')
        metro.add_station_to_line('l-2', 'Demiivska', '06:00:00', '23:56:00')
        metro.add_station_to_line('l-2', 'Lybidska', '06:00:00', '23:56:00')
        metro_xml.write_metro('output_add_station.xml', metro)
        self.assertEqual(filecmp.cmp('output_add_station.xml', 'correct_data_after_adding_station.xml'), True)

    def test_deleting_line(self):
        metro = metro_xml.parse_metro('test_data_for_add_del.xml')
        metro.delete_line('l-2')
        metro_xml.write_metro('output_delete_line.xml', metro)
        self.assertEqual(filecmp.cmp('output_delete_line.xml', 'correct_data_after_deleting_line.xml'), True)

    def test_deleting_station(self):
        self.assertEqual(True, False)

    def search_station(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
