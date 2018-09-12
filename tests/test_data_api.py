import unittest

from ripple_api import RippleDataAPIClient


class TestLedgerRequests(unittest.TestCase):
    node = 'https://data.ripple.com'

    @classmethod
    def setUpClass(cls):
        cls.api = RippleDataAPIClient(cls.node)

    def test_get_legder(self):
        identifier = '3170DA37CE2B7F045F889594CBC323D88686D2E90E8FFD2BBCD9BAD12E416DB5'
        query_params = dict(transactions='true')
        info = self.api.get_ledger(ledger_identifier=identifier, **query_params)
        self.assertEqual(info['result'], 'success')
        self.assertIn('account_hash', info['ledger'])
        self.assertIn('tx_count', info['ledger'])

    def test_get_ledger_validations(self):
        ledger_hash = 'A10E9E338BA365D2B768814EC8B0A9A2D8322C0040735E20624AF711C5A593E7'
        query_params = dict(limit=2)
        info = self.api.get_ledger_validations(ledger_hash=ledger_hash, **query_params)
        self.assertEqual(info['result'], 'success')
        self.assertIn('ledger_hash', info)
        self.assertIn('validations', info)

    def test_get_ledger_validation(self):
        ledger_hash = 'A10E9E338BA365D2B768814EC8B0A9A2D8322C0040735E20624AF711C5A593E7'
        pubkey = 'n949f75evCHwgyP4fPVgaHqNHxUVN15PsJEZ3B3HnXPcPjcZAoy7'
        info = self.api.get_ledger_validation(ledger_hash=ledger_hash, pubkey=pubkey)
        self.assertEqual(info['result'], 'success')
        self.assertIn('ledger_hash', info)
        self.assertIn('reporter_public_key', info)

