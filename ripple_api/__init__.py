from decimal import Decimal

from ripple_api.json_rpc import RippleRPCClient
from ripple_api.data_api import RippleDataAPIClient


class Account(RippleRPCClient):
    def __init__(self, node: str, account: str, seed: str) -> None:
        super(Account, self).__init__(node)
        self.account = account
        self.seed = seed
        self.xrp_base = Decimal(1000000)

    def __repr__(self):
        return '<Account address={}>'.format(self.account)

    def balance(self, address: str=None) -> Decimal:
        """
        Get balance of XRP, if address is not specified return balance of the main address
        :param address: xrp address
        :return: amount of XRP
        """
        address = self.account if address is None else address
        info = self.account_info(account=address)
        balance = info.get('account_data', {}).get('Balance', 0)
        return Decimal(balance) / self.xrp_base
        
    def sign_and_submit(self, tx_json: dict, secret: str) -> dict:
        """
        Base method that signs transaction and submits it
        :param tx_json: transaction json, formatted accordingly
        :param secret: seed of the account
        :return: transaction data
        """
        tx_info = self.sign(tx_json=tx_json, secret=secret)
        tx_blob = tx_info.get('tx_blob')
        return self.submit(tx_blob=tx_blob)

    def send_xrp(self, issuer: str, taker: str, amount: str, secret: str) -> dict:
        """
        Send XRP from one account to another
        :param issuer:  address of account, from which you send xrp
        :param taker: address of account which receives xrp
        :param amount: amount of xrp that will be sent
        :param secret: seed of the issuer
        :return:  transaction data (tx_id, taker, issuer, amount)
        """
        payment_json = dict(
            Account=issuer,
            Amount=str(int(Decimal(amount) * self.xrp_base)),
            Destination=taker,
            TransactionType="Payment"
        )
        return self.sign_and_submit(tx_json=payment_json, secret=secret)

    def send_currency(self, issuer: str, taker: str, currency: str, amount: str, secret: str) -> dict:
        """
        Send amount of some currency from one account to another
        :param issuer:  address of account, from which you send xrp
        :param taker: address of account which receives xrp
        :param currency: name of the currency which will be sent
        :param amount: amount of xrp that will be sent
        :param secret: seed of the issuer
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
        return self.sign_and_submit(tx_json=payment_json, secret=secret)
