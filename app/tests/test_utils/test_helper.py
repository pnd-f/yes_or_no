from unittest import TestCase
from app.utils import get_yes_or_no_locally
import unittest


class GetYesOrNoLocallyTestCase(TestCase):
    def test_get_yes_or_no_locally_with_default_value(self):
        result = get_yes_or_no_locally()
        print(result)
        self.assertIsInstance(result, str)

    def test_get_yes_or_no_locally_use_maybe_false(self):
        result = get_yes_or_no_locally(use_maybe=False)
        print(result)
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
