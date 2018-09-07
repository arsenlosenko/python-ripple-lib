from tests import BaseTestClass


class TestPathAndOrderBook(BaseTestClass):
    def test_book_offers(self):
        test_taker_account = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        test_issuer_account = 'rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B'
        get_currency = 'XRP'
        pay_currency = 'USD'
        info = self.rpc.book_offers(taker=test_taker_account, issuer=test_issuer_account,
                                    taker_gets_currency=get_currency, taker_pays_currency=pay_currency)
        self.assertIn('offers', info)
        self.assertEqual(info['status'], 'success')

    def test_incorrect_book_offers(self):
        incorrect_taker_account = '19cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        test_issuer_account = 'rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B'
        get_currency = 'XRP'
        pay_currency = 'USD'
        info = self.rpc.book_offers(taker=incorrect_taker_account, issuer=test_issuer_account,
                                    taker_gets_currency=get_currency, taker_pays_currency=pay_currency)
        self.assertIn('error', info)
        self.assertEqual(info['error'], 'invalidParams')

    def test_ripple_path_find(self):
        destination_account = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        destination_account_currency = 'USD'
        destination_account_issuer = 'rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B'
        destination_account_value = '0.001'
        source_account = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        source_currencies = ['XRP', 'USD']
        info = self.rpc.ripple_path_find(destination_account=destination_account, currency=destination_account_currency,
                                         issuer=destination_account_issuer, value=destination_account_value,
                                         source_account=source_account, source_currencies=source_currencies)
        self.assertIn('alternatives', info)
        self.assertEqual(info['status'], 'success')

    def test_ripple_path_find_no_currencies(self):
        destination_account = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        destination_account_currency = 'USD'
        destination_account_issuer = 'rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B'
        destination_account_value = '0.001'
        source_account = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
        source_currencies = []
        info = self.rpc.ripple_path_find(destination_account=destination_account, currency=destination_account_currency,
                                         issuer=destination_account_issuer, value=destination_account_value,
                                         source_account=source_account, source_currencies=source_currencies)
        self.assertIn('error', info)
        self.assertEqual(info['error'], 'srcCurMalformed')
