from tests import BaseTestClass


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

    def test_sign(self):
        tx_json = {
                "Account": "rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn",
                "Amount": {
                    "currency": "USD",
                    "issuer": "rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn",
                    "value": "1"
                },
                "Destination": "ra5nK24KXen9AHvsdFTKHSANinZseWnPcX",
                "TransactionType": "Payment"
            }
        secret = "v3ry-s3cr3t-cod3"
        info = self.rpc.sign(tx_json=tx_json, secret=secret)
        self.assertEqual(info['status'], 'success')
        self.assertIn('tx_blob', info)

    def test_sign_for(self):
        tx_json = {
            "TransactionType": "TrustSet",
            "Account": "rEuLyBCvcw4CFmzv8RepSiAoNgF8tTGJQC",
            "Flags": 262144,
            "LimitAmount": {
                "currency": "USD",
                "issuer": "rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh",
                "value": "100"
            },
            "Sequence": 2,
            "SigningPubKey": "",
            "Fee": "30000"
        }
        secret = "v3ry-s3cr3t-cod3"
        info = self.rpc.sign_for(tx_json=tx_json, secret=secret)
        self.assertEqual(info['status'], 'success')
        self.assertIn('tx_blob', info)

    def test_submit(self):
        tx_blob = "1200002280000000240000000361D4838D7EA4C6800000000000000000000000000055534400000000004B4E9C06F24296" \
                  "074F7BC48F92A97916C6DC5EA968400000000000000A732103AB40A0490F9B7ED8DF29D246BF2D6269820A0EE7742ACDD45"\
                  "7BEA7C7D0931EDB74473045022100D184EB4AE5956FF600E7536EE459345C7BBCF097A84CC61A93B9AF7197EDB9870220" \
                  "1CEA8009B7BEEBAA2AACC0359B41C427C1C5B550A4CA4B80CF2174AF2D6D5DCE81144B4E9C06F24296074F7BC48F92A97" \
                  "916C6DC5EA983143E9D4A2B8AA0780F682D136F7A56D6724EF53754"
        info = self.rpc.submit(tx_blob=tx_blob)
        self.assertEqual(info['status'], 'success')

