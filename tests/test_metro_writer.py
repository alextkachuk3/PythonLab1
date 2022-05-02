import unittest

import metro_xml
from xml_util import is_two_xml_equal


class TestWriter(unittest.TestCase):
    def test_writer(self):
        metro = metro_xml.parse_metro('test_data_for_writer.xml')
        metro_xml.write_metro('test_writer_output.xml', metro)
        self.assertEqual(is_two_xml_equal('test_data_for_writer.xml', 'test_writer_output.xml'), True)


if __name__ == '__main__':
    unittest.main()
