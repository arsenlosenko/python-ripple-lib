from ripple_api.json_rpc import RippleRPCClient
from ripple_api.data_api import RippleDataAPIClient


class Account(RippleRPCClient):
    def __init__(self, node, seed):
        super(Account, self).__init__(node)
        self.seed = seed

    def send_xrp(self, issuer: str, taker: str, amount: str) -> dict:
        """
        Send XRP from one account to another
        :param issuer:  address of account, from which you send xrp
        :param taker: address of account which receives xrp
        :param amount: amount of xrp that will be sent
        :return:  transaction data (tx_id, taker, issuer, amount)
        """
        payment_json = dict(
            Account=issuer,
            Amount=dict(
                currency="XRP",
                issuer=issuer,
                value=amount
            ),
            Destination=taker,
            TransactionType="Payment"

        )
        tx_info = self.sign(tx_json=payment_json, secret=self.seed)
        tx_blob = tx_info.get('tx_blob')
        self.submit(tx_blob=tx_blob)
        return self.tx(tx=tx_blob)

