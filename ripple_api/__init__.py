from decimal import Decimal

from ripple_api.json_rpc import RippleRPCClient
from ripple_api.data_api import RippleDataAPIClient


class Account(RippleRPCClient):
    def __init__(self, node: str, account: str, seed: str) -> None:
        super(Account, self).__init__(node)
        self.account = account
        self.seed = seed
        self.xrp_base = Decimal(1000000)

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
            Amount=int(Decimal(amount) * self.xrp_base),
            Destination=taker,
            TransactionType="Payment"
        )
        tx_info = self.sign(tx_json=payment_json, secret=self.seed)
        tx_blob = tx_info.get('tx_blob')
        return self.submit(tx_blob=tx_blob)

    def send_currency(self, issuer: str, taker: str, currency: str, amount: str) -> dict:
        """
        Send amount of some currency from one account to another
        :param issuer:  address of account, from which you send xrp
        :param taker: address of account which receives xrp
        :param currency: name of the currency which will be sent
        :param amount: amount of xrp that will be sent
        :return:  transaction data (tx_id, taker, issuer, amount)
        """
        payment_json = dict(
            Account=issuer,
            Amount=dict(
                currency=currency,
                issuer=issuer,
                value=int(Decimal(amount) * self.xrp_base),
            ),
            Destination=taker,
            TransactionType="Payment"
        )
        tx_info = self.sign(tx_json=payment_json, secret=self.seed)
        tx_blob = tx_info.get('tx_blob')
        return self.submit(tx_blob=tx_blob)
