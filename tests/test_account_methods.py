from tests import BaseTestClass


class TestAccountMethods(BaseTestClass):

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

    def test_account_channels(self):
        account = 'rN7n7otQDd6FczFgLdSqtcsAUxDkw6fzRH'
        destination_account = 'rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn'
        info = self.rpc.account_channels(account=account, destination_account=destination_account)
        self.assertEqual(info['account'], account)
        self.assertIn('channels', info)

    def test_incorrect_account_channels(self):
        destination_account = 'rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn'
        info = self.rpc.account_channels(account=self.invalid_address, destination_account=destination_account)
        self.assertIn('error', info)

    def test_account_currencies(self):
        test_account = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        info = self.rpc.account_currencies(test_account)
        self.assertIn('send_currencies', info)
        self.assertIn('receive_currencies', info)
        self.assertIsNot('error', info)

    def test_incorrect_account_currencies(self):
        info = self.rpc.account_currencies(self.invalid_address)
        self.assertIn('error', info)

    def test_account_objects(self):
        test_account = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        info = self.rpc.account_objects(test_account)
        self.assertEqual(info['account'], test_account)
        self.assertIn('account_objects', info)

    def test_incorrect_account_objects(self):
        info = self.rpc.account_objects(self.invalid_address)
        self.assertIn('error', info)

    def test_account_offers(self):
        test_account = 'rpP2JgiMyTF5jR5hLG3xHCPi1knBb1v9cM'
        info = self.rpc.account_offers(test_account)
        self.assertEqual(info['account'], test_account)
        self.assertIn('offers', info)

    def test_incorrect_account_offers(self):
        info = self.rpc.account_offers(self.invalid_address)
        self.assertIn('error', info)

    def test_account_tx(self):
        test_account = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        info = self.rpc.account_tx(test_account)
        self.assertEqual(info['account'], test_account)
        self.assertIn('transactions', info)

    def test_incorrect_account_tx(self):
        info = self.rpc.account_tx(self.invalid_address)
        self.assertIn('error', info)

    def test_gateway_balances(self):
        test_account = 'rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q'
        hotwallet = [
            'rKm4uWpg9tfwbVSeATv4KxDe6mpE9yPkgJ',
            'ra7JkEzrgeKHdzKgo4EUUVBnxggY4z37kt'
        ]
        info = self.rpc.gateway_balances(account=test_account, hotwallet=hotwallet)
        self.assertEqual(info['account'], test_account)
        self.assertIn('assets', info)

    def test_incorrect_gateway_balances(self):
        hotwallet = [
            'rKm4uWpg9tfwbVSeATv4KxDe6mpE9yPkgJ',
            'ra7JkEzrgeKHdzKgo4EUUVBnxggY4z37kt'
        ]
        info = self.rpc.gateway_balances(account=self.invalid_address, hotwallet=hotwallet)
        self.assertIn('error', info)

    def test_noripple_check(self):
        test_account = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        info = self.rpc.noripple_check(account=test_account)
        self.assertIn('problems', info)
        self.assertIn('transactions', info)

    def test_incorrect_noripple_check(self):
        info = self.rpc.noripple_check(self.invalid_address)
        self.assertIn('error', info)
