from tests import BaseTestClass


class TestStatusDebuggingMehods(BaseTestClass):
    node = 'http://localhost:5005/'

    def test_consensus_info(self):
        info = self.rpc.consensus_info()
        self.assertEqual(info['status'], 'success')
        self.assertIn('ledger_seq', info['info'])
        self.assertIn('our_position', info['info'])

    def test_feature(self):
        test_feature = '4C97EBA926031A7CF7D7B36FDE3ED66DDA5421192D63DE53FFB46E43B9DC8373'
        test_vetoed = False
        info = self.rpc.feature(feature=test_feature, vetoed=test_vetoed)
        self.assertEqual(info['status'], 'success')
        self.assertIn(test_feature, info)
        self.assertIn('name', info[test_feature])

    def test_fetch_info(self):
        clear = False
        info = self.rpc.fetch_info(clear=clear)
        self.assertEqual(info['status'], 'success')
        self.assertIn('info', info)

    def test_get_counts(self):
        min_count = 100
        info = self.rpc.get_counts(min_count=min_count)
        self.assertEqual(info['status'], 'success')
        self.assertIn('write_load', info)
        self.assertIn('uptime', info)

    def test_peers(self):
        info = self.rpc.peers()
        self.assertEqual(info['status'], 'success')
        self.assertIn('cluster', info)
        self.assertIn('peers', info)

    def test_print(self):
        info = self.rpc.print()
        self.assertEqual(info['status'], 'success')
        self.assertIn('app', info)
        self.assertIn('peers', info['app'])

    def test_validator_list_sites(self):
        info = self.rpc.validator_list_sites()
        self.assertEqual(info['status'], 'success')
        self.assertIn('validator_sites', info)
        self.assertIn('uri', info['validator_sites'][0])

    def test_validators(self):
        info = self.rpc.validators()
        self.assertEqual(info['status'], 'success')
        self.assertIn('publisher_lists', info)
        self.assertIn('trusted_validator_keys', info)






