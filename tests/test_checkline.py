import unittest

from helpers.checkline import check_line
from helpers.args import COL_SIZE


class TestCheckline(unittest.TestCase):

    def setUp(self):
        self.line_ok = ['2016-04-03', '1000', '10000.00', 'Sandy Lerner']
        self.line_nok = ['2016d-04-03', '1000', '10000.00', 'Sandy Lerner']

    def test_line_ok(self):
        res = check_line(self.line_ok, 1)
        self.assertEqual(len(res), COL_SIZE)

    def test_line_nok(self):
        self.assertRaises(TypeError, check_line, self.line_nok, 1)
