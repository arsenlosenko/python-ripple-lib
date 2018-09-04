from test import BaseTestClass


class TestTransactionMethods(BaseTestClass):

    def test_transaction_entry(self):
        test_tx_hash = '115BBD273697E0200AB66EA853F91D88E03A8A07F4F16F9EAFE966EE166F9521'
        test_ledger_index = 39514735
        info = self.rpc.transaction_entry(tx_hash=test_tx_hash, ledger_index=test_ledger_index)
        self.assertEqual(info['ledger_index'], test_ledger_index)

    def test_tx(self):
        # TODO: find a valid tx_hash for testing
        test_tx_hash = '115BBD273697E0200AB66EA853F91D88E03A8A07F4F16F9EAFE966EE166F9521'
        info = self.rpc.tx(test_tx_hash)
        self.assertIn('Amount', info)
        self.assertIn('Paths', info)

    def test_tx_history(self):
        info = self.rpc.tx_history()
        self.assertIn('txs', info)

    def test_submit(self):
        return NotImplemented

    def test_sign(self):
        return NotImplemented

    def test_sign_for(self):
        return NotImplemented

    def test_submit_multisigned(self):
        return NotImplemented
