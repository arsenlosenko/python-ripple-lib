import requests


class RippleRPCClient(object):
    def __init__(self, node: str, chain: str):
        """
        :param node: URL of rippled node
        :param chain: chain (mainnet or testnet) that node is connected to
        """
        self.node = node
        self.chain = chain

    def _call(self, method: str, params: dict) -> dict:
        """Base method which sends requests to node
        :param method: JSON-RPC method of rippled
        :param params: parameters of the request
        """
        payload = {
            "method": method,
            "params": [
                params
            ]
        }
        res = requests.post(self.node, json=payload)
        if res.status_code == 200 and res.json().get('result'):
            return res.json().get('result')
        return {"txt": res.text, "status_code": res.status_code}

    def account_info(self, account: str, strict: bool=True, ledger_index: str='current', queue: bool=True) -> dict:
        """
        Method retrieves information about an account, its activity, and its XRP balance.
        All information retrieved is relative to a particular version of the ledger.
        Reference: https://developers.ripple.com/account_info.html
        """
        params = dict(
            account=account,
            strict=strict,
            ledger_index=ledger_index,
            queue=queue
        )
        return self._call('account_info', params)

    def account_lines(self, account: str) -> dict:
        """
        Method returns information about an account's trust lines, including balances in all non-XRP currencies
        and assets. All information retrieved is relative to a particular version of the ledger.
        Reference: https://developers.ripple.com/account_lines.html
        """
        return self._call('account_lines', params=dict(account=account))

    def account_channels(self, account: str, destination_account:str, ledger_index: str='validated') -> dict:
        """
        Method returns information about an account's Payment Channels.
        This includes only channels where the specified account is the channel's source, not the destination.
        (A channel's "source" and "owner" are the same.)
        All information retrieved is relative to a particular version of the ledger.
        Reference: https://developers.ripple.com/account_channels.html
        """
        params = dict(
            account=account,
            destination_account=destination_account,
            ledger_index=ledger_index
        )
        return self._call('account_channels', params)

    def account_currencies(self, account: str, account_index: int=0, ledger_index: str="validated", strict: bool=True) -> dict:
        """
        Method retrieves a list of currencies that an account can send or receive, based on its trust lines.
        (This is not a thoroughly confirmed list, but it can be used to populate user interfaces.)
        Reference: https://developers.ripple.com/account_currencies.html
        """
        params = dict(
            account=account,
            account_index=account_index,
            ledger_index=ledger_index,
            strict=strict
        )
        return self._call('account_currencies', params)

    def account_objects(self, account: str, ledger_index: str="validated", limit: int=10, type: str="state") -> dict:
        """
        Method returns the raw ledger format for all objects owned by an account.
        For a higher-level view of an account's trust lines and balances, see the account_lines method instead.
        Reference: https://developers.ripple.com/account_objects.html
        """
        params = dict(
            account=account,
            ledger_index=ledger_index,
            limit=limit,
            type=type
        )
        return self._call('account_objects', params)

    def account_offers(self, account: str) -> dict:
        """
         Method retrieves a list of offers made by a given account that are outstanding as of a particular ledger version.
         Reference: https://developers.ripple.com/account_offers.html
        """
        return self._call('account_offers', params=dict(account=account))

    def account_tx(self, account: str, binary: bool=False, forward: bool=False,
                   ledger_index_max=-1, ledger_index_min=-1, limit=2) -> dict:
        """
        Method retrieves a list of transactions that involved the specified account.
        Reference: https://developers.ripple.com/account_tx.html
        """
        params = dict(
            account=account,
            binary=binary,
            forward=forward,
            ledger_index_max=ledger_index_max,
            ledger_index_min=ledger_index_min,
            limit=limit
        )
        return self._call('account_tx', params)

    def gateway_balances(self, account: str, hotwallet: list=None, ledger_index: str="validated", strict: bool=True) -> dict:
        """
        Method calculates the total balances issued by a given account, optionally excluding amounts held by operational addresses.
        Reference:https://developers.ripple.com/gateway_balances.html
        """
        hotwallet = [] if None else hotwallet
        params = dict(
            account=account,
            hotwallet=hotwallet,
            ledger_index=ledger_index,
            strict=strict
        )
        return self._call('gateway_balances', params)

    def noripple_check(self, account: str, ledger_index: str='current', limit: int=2,
                       role: str="gateway", transactions: bool=True) -> dict:
        """
        Method provides a quick way to check the status of the DefaultRipple field for an account and
        the NoRipple flag of its trust lines, compared with the recommended settings.
        Reference: https://developers.ripple.com/noripple_check.html
        """
        params = dict(
            account=account,
            ledger_index=ledger_index,
            limit=limit,
            role=role,
            transactions=transactions
        )
        return self._call('noripple_check', params)

    def ledger(self, ledger_index: str='validated', accounts: bool=False, full: bool=False,
               transactions: bool=False, expand: bool=False, owner_funds: bool=False) -> dict:
        """
        Retrieve information about the public ledger.
        Reference: https://developers.ripple.com/ledger.html
        """
        params = dict(
            ledger_index=ledger_index,
            accounts=accounts,
            full=full,
            transactions=transactions,
            expand=expand,
            owner_funds=owner_funds
        )
        return self._call('ledger', params)

    def ledger_closed(self) -> dict:
        """
        Method returns the unique identifiers of the most recently closed ledger.
        (This ledger is not necessarily validated and immutable yet.)
        Reference: https://developers.ripple.com/ledger_closed.html
        """
        return self._call('ledger_closed', params=dict())

    def ledger_current(self) -> dict:
        """
        Method returns the unique identifiers of the current in-progress ledger.
        This command is mostly useful for testing, because the ledger returned is still in flux.
        Reference: https://developers.ripple.com/ledger_current.html
        """
        return self._call('ledger_current', params=dict())

    def ledger_data(self, ledger_hash: str, binary: bool=True, limit: int=5) -> dict:
        """
        Method retrieves contents of the specified ledger. You can iterate through several calls to retrieve the entire contents of a single ledger version.
        Reference: https://developers.ripple.com/ledger_data.html
        """
        params = dict(
            ledger_hash=ledger_hash,
            binary=binary,
            limit=limit
        )
        return self._call('ledger_data', params)

    def ledger_entry(self, account_root: str, ledger_index: str="validated", type: str="account_root") -> dict:
        """
        Method returns a single ledger object from the XRP Ledger in its raw format.
        See ledger format for information on the different types of objects you can retrieve.
        Reference: https://developers.ripple.com/ledger_entry.html
        """
        params = dict(
            account_root=account_root,
            ledger_index=ledger_index,
            type=type
        )
        return self._call('ledger_entry', params)

    def sign(self, offline: bool = False, secret: str = '', tx_json: dict = None, fee_mult_max: int = 1000) -> dict:
        """
        The sign method takes a transaction in JSON format and a secret key,
        and returns a signed binary representation of the transaction. The result is always different,
        even when you provide the same transaction JSON and secret key.
        Reference: https://developers.ripple.com/sign.html
        """
        return NotImplemented

    def sign_for(self, account: str, seed: str, key_type: str = "ed25519", tx_json: dict = None) -> dict:
        """
        Method provides one signature for a multi-signed transaction.
        Reference: https://developers.ripple.com/sign_for.html
        """
        return NotImplemented

    def submit(self, tx_blob: str, fail_hard: bool = False) -> dict:
        """
        Method applies a transaction and sends it to the network to be confirmed and included in future ledgers.
        Reference: https://developers.ripple.com/submit.html
        """
        # TODO: implement submit-only and sign-and-submit
        return NotImplemented

    def submit_mutlisigned(self, tx_json: dict = None):
        """
        Method applies a multi-signed transaction and sends it to the network to be included in future ledgers.
        (You can also submit multi-signed transactions in binary form using the submit command in submit-only mode.)
        Reference: https://developers.ripple.com/submit_multisigned.html
        """
        return NotImplemented

    def transaction_entry(self, tx_hash: str, ledger_index: int) -> dict:
        """
        Method retrieves information on a single transaction from a specific ledger version.
        (The tx method, by contrast, searches all ledgers for the specified transaction.
        We recommend using that method instead.)
        Reference: https://developers.ripple.com/transaction_entry.html
        """
        params = dict(
            tx_hash=tx_hash,
            ledger_index=ledger_index
        )
        return self._call('transaction_entry', params)

    def tx(self, tx: str, binary: bool=False) -> dict:
        """
        Method retrieves information on a single transaction
        Reference: https://developers.ripple.com/tx.html
        """
        params = dict(
            transaction=tx,
            binary=binary
        )
        return self._call('tx', params)

    def tx_history(self, start: int=0) -> dict:
        """
        Method retrieves some of the most recent transactions made.
        This method is deprecated, and may be removed without further notice.
        Reference: https://developers.ripple.com/tx_history.html
        """
        return self._call('tx_history', params=dict(start=start))

    def ping(self) -> dict:
        """
        Method returns an acknowledgement, so that clients can test the connection status and latency.
        Reference: https://developers.ripple.com/ping.html
        """
        return self._call('ping', params=dict())


if __name__ == '__main__':
    test_address = 'r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59'
    rpc = RippleRPCClient('http://s1.ripple.com:51234/', 'testnet')
    print(rpc.noripple_check(test_address))
