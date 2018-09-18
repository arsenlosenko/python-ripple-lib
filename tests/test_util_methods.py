import unittest

from ripple_api.utils import generate_seed


class TestUtilMethods(unittest.TestCase):
    def test_generate_seed(self):
        seed = generate_seed()
        self.assertTrue(str(seed))
        self.assertEqual(len(seed), 29)