import unittest

from ripple_api.json_rpc import RippleRPCClient


class BaseTestClass(unittest.TestCase):
    node = 'http://s1.ripple.com:51234/'

    @classmethod
    def setUpClass(cls):
        cls.rpc = RippleRPCClient(cls.node)
        cls.valid_address = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        cls.invalid_long_address = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk591313'
        cls.invalid_address = '19cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'