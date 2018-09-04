from test import BaseTestClass


class TestLedgerMethods(BaseTestClass):

    def test_ledger(self):
        info = self.rpc.ledger()
        print(info)
        self.assertTrue(info['validated'])
        self.assertIn('ledger', info)

    def test_incorrect_ledger(self):
        info = self.rpc.ledger(ledger_index='hjdfkgkjs')
        self.assertIn('error', info)

    def test_ledger_closed(self):
        info = self.rpc.ledger_closed()
        self.assertEqual(info['status'], 'success')
        self.assertIn('ledger_hash', info)

    def test_ledger_current(self):
        info = self.rpc.ledger_current()
        self.assertIn('ledger_current_index', info)

    def test_legder_data(self):
        test_ledger_hash = 'FA3CFE25A190FA3CD55FD3AADF27872110D25B183D38E4DF547586163357CC70'
        info = self.rpc.ledger_data(test_ledger_hash)
        self.assertEqual(info['ledger_hash'], test_ledger_hash)
        self.assertIn('state', info)

    def test_ledger_entry(self):
        test_account_root = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        info = self.rpc.ledger_entry(test_account_root)
        self.assertIn('ledger_index', info)
        self.assertIn('node', info)

    def test_incorrect_ledger_entry(self):
        incorrect_account_root = '19cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        info = self.rpc.ledger_entry(incorrect_account_root)
        self.assertEqual(info['error'], 'malformedAddress')

