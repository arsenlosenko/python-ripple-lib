from test import BaseTestClass


class TestKeyGeneration(BaseTestClass):
    node = 'http://localhost:5005/'

    def test_validation_create(self):
        test_secret = 'BAWL MAN JADE MOON DOVE GEM SON NOW HAD ADEN GLOW TIRE'
        info = self.rpc.validation_create(secret=test_secret)
        self.assertEqual(info['status'], 'success')
        self.assertIn('validation_public_key', info)
        self.assertIn('validation_seed', info)

    def test_wallet_propose(self):
        test_seed = 'snoPBrXtMeMyMHUVTgbuqAfg1SUTb'
        info = self.rpc.wallet_propose(seed=test_seed)
        self.assertEqual(info['status'], 'success')
        self.assertIn('account_id', info)
        self.assertIn('public_key', info)
