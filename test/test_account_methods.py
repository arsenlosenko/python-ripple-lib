import unittest

from api.json_rpc import RippleRPCClient


class TestAccountMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rpc = RippleRPCClient('http://s1.ripple.com:51234/', 'testnet')
        cls.valid_address = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        cls.invalid_long_address = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk591313'
        cls.invalid_address = '19cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'

    def test_account_info(self):
        info = self.rpc.account_info(self.valid_address)
        self.assertEqual(info['account_data']['Account'], self.valid_address)
        self.assertEqual(info['status'], 'success')
        self.assertIn('Balance', info['account_data'])

    def test_incorrect_account(self):
        info = self.rpc.account_info(self.invalid_address)
        self.assertEqual(info['status'], 'error')

    def test_account_lines(self):
        info = self.rpc.account_lines(self.valid_address)
        self.assertEqual(info['account'], self.valid_address)
        self.assertIn('lines', info)

    def test_incorrect_account_lines(self):
        info = self.rpc.account_lines(self.invalid_address)
        self.assertIn('error', info)
        self.assertEqual(info['status'], 'error')


if __name__ == '__main__':
    unittest.main()