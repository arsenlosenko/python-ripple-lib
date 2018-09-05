from test import BaseTestClass


class TestLoggingAndDataManagement(BaseTestClass):
    def test_can_delete(self):
        test_ledger_num = 11320417
        info = self.rpc.can_delete(can_delete=test_ledger_num)
        return NotImplemented