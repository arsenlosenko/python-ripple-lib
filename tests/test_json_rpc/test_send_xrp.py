from tests import BaseTestClass


class TestSendXRP(BaseTestClass):
    def test_send_xrp(self):
        issuer = 'hjfgkdfgdf'
        taker = 'afjkgfkdjgkgf'
        amount = '1000'
        tx_info = self.rpc.send_xrp(issuer=issuer, taker=taker, amount=amount)
        self.assertIn('tx_id', tx_info)
        self.assertIn('issuer', tx_info)
        self.assertIn('taker', tx_info)
        self.assertIn('amount', tx_info)