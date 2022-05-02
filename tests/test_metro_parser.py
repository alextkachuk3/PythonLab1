import metro_xml
import unittest

from xml_util import xml_str_to_time


class TestParsing(unittest.TestCase):
    def test_parsing(self):
        metro = metro_xml.parse_metro('parsing_test_data.xml')
        self.assertEqual(metro.lines[0].id, 'l-1')
        self.assertEqual(metro.lines[1].id, 'l-2')

        self.assertEqual(metro.lines[0].color, 'red')
        self.assertEqual(metro.lines[1].color, 'blue')

        self.assertEqual(metro.lines[0].stations[0].id, 's-1-1')
        self.assertEqual(metro.lines[0].stations[1].id, 's-1-2')
        self.assertEqual(metro.lines[1].stations[0].id, 's-2-1')
        self.assertEqual(metro.lines[1].stations[1].id, 's-2-2')

        self.assertEqual(metro.lines[0].stations[0].name, 'Akademmistechko')
        self.assertEqual(metro.lines[0].stations[1].name, 'Zhytomyrska')
        self.assertEqual(metro.lines[1].stations[0].name, 'Teremky')
        self.assertEqual(metro.lines[1].stations[1].name, 'Ipodrom')

        self.assertEqual(metro.lines[0].stations[0].open, xml_str_to_time('05:58:00'))
        self.assertEqual(metro.lines[0].stations[1].open, xml_str_to_time('05:58:00'))
        self.assertEqual(metro.lines[1].stations[0].open, xml_str_to_time('06:00:00'))
        self.assertEqual(metro.lines[1].stations[1].open, xml_str_to_time('06:00:00'))

        self.assertEqual(metro.lines[0].stations[0].close, xml_str_to_time('23:45:00'))
        self.assertEqual(metro.lines[0].stations[1].close, xml_str_to_time('23:47:00'))
        self.assertEqual(metro.lines[1].stations[0].close, xml_str_to_time('1:00:00'))
        self.assertEqual(metro.lines[1].stations[1].close, xml_str_to_time('0:55:00'))


if __name__ == '__main__':
    unittest.main()
