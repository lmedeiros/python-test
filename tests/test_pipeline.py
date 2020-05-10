import unittest

from pipeline.manager import PipelineManager
from pipeline.pipes import (load, output, summarize, validate)
from helpers.args import COL_SIZE
from datetime import datetime


class TestCheckline(unittest.TestCase):

    def setUp(self):
        self.file_ok = './data/captable.csv'
        self.file_nok = './data/captable_error.csv'
        self.file_empty = './data/captable_empty.csv'
        self.date_ok = '2020-02-01'
        self.date_nok = 'asdijf4902'
        self.date_past = '2011-01-01'
        self.date_future = '2059-01-01'

    def test_fileok(self):
        pm = PipelineManager(self.file_ok, self.date_ok)
        pm.start()

        self.assertTrue('cash_raised' in pm.raw_data,
                        "cash_raised not present")

        self.assertTrue('date' in pm.raw_data,
                        "date not present")

        self.assertEqual(pm.raw_data['date'], '02/01/2020')

        self.assertEqual(pm.raw_data['total_number_of_shares'], 9500)
        self.assertEqual(len(pm.raw_data['ownership']), 4)

        for owner in pm.raw_data['ownership']:
            if owner['investor'] == 'Don Valentine':
                self.assertEqual(owner['ownership'], 31.58)
                self.assertEqual(owner['shares'], 3000)

    def test_datenok(self):
        pm = PipelineManager(self.file_ok, self.date_nok)

        self.assertRaises(ValueError, pm.start)

    def test_datepast(self):
        pm = PipelineManager(self.file_ok, self.date_past)
        pm.start()

        self.assertEqual(pm.raw_data['date'], '01/01/2011')
        self.assertEqual(len(pm.raw_data['ownership']), 0)
        self.assertEqual(pm.raw_data['total_number_of_shares'], 0)

    def test_fileempty(self):
        pm = PipelineManager(self.file_empty, self.date_ok)

        self.assertRaises(FileNotFoundError, pm.start)

    def test_fileerror(self):
        pm = PipelineManager(self.file_nok, self.date_ok)

        with self.assertRaises(TypeError) as cm:
            pm.start()

        self.assertTrue(
            'Invalid type for line 1, col 0: date' in cm.exception.__str__())
