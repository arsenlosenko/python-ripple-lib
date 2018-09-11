from tests import BaseTestClass


class TestPaymentChannelsMethods(BaseTestClass):
    def test_channel_authorize(self):
        channel_id = "5DB01B7FFED6B67E6B0414DED11E051D2EE2B7619CE0EAA6286D67A3A4D5BDB3"
        secret = "fdfksdjfl"
        amount = "10000"
        info = self.rpc.channel_authorize(channel_id=channel_id, secret=secret, amount=amount)
        self.assertEqual(info['status'], 'success')
        self.assertIn('signature', info)

    def test_channel_verify(self):
        channel_id = "5DB01B7FFED6B67E6B0414DED11E051D2EE2B7619CE0EAA6286D67A3A4D5BDB3"
        signature = "fdfksdjfl"
        public_key = 'sdkfdkgjdfgkdfkhj'
        amount = "10000"
        info = self.rpc.channel_verify(channel_id=channel_id, signature=signature, public_key=public_key, amount=amount)
        self.assertEqual(info['status'], 'success')
        self.assertIn('signature_verified', info)


