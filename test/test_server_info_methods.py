from test import BaseTestClass


class TestServerInfoMethods(BaseTestClass):
    def test_fee(self):
        info = self.rpc.fee()
        self.assertIn('drops', info)
        self.assertIn('levels', info)
        self.assertEqual(info['status'], 'success')

    def test_server_info(self):
        info = self.rpc.server_info()
        self.assertIn('build_version', info['info'])
        self.assertIn('server_state', info['info'])
        self.assertEqual(info['status'], 'success')

    def test_server_state(self):
        info = self.rpc.server_state()
        self.assertIn('build_version', info['state'])
        self.assertIn('server_state', info['state'])
        self.assertEqual(info['status'], 'success')

    def test_ping(self):
        info = self.rpc.ping()
        self.assertEqual(info['status'], 'success')

    def test_random(self):
        info = self.rpc.random()
        self.assertIn('random', info)
        self.assertEqual(info['status'], 'success')
