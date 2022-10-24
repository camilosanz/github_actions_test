import argparse
from helpers.args_processor import valid_date
import unittest


def test_valid_date_string_true():
    test_date = "2022-9-11"
    assert_msj = "Test date doesn't match"
    assert valid_date(test_date) == test_date, assert_msj


class ArgsTestProcessor(unittest.TestCase):

    def test_valid_date_exception_throw_false(self):

        test_date = "2022-99-11"
        assert_msj = "Test date doesn't match"
        with self.assertRaises(argparse.ArgumentTypeError):
            valid_date(test_date), assert_msj
