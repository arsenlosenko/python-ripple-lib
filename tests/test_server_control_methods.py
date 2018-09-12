from tests import BaseTestClass


class TestServerControl(BaseTestClass):
    node = 'http://localhost:5005/'

    def test_connect(self):
        test_ip = "192.170.145.88"
        test_port = 51235
        info = self.rpc.connect(ip=test_ip, port=test_port)
        self.assertEqual(info['status'], 'success')
        self.assertIn('message', info)

    def test_stop(self):
        info = self.rpc.stop()
        self.assertEqual(info['status'], 'success')
        self.assertEqual(info['message'], "ripple server stopping")