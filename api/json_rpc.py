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

    def account_info(self, account: str, strict=True, ledger_index='current', queue=True) -> dict:
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

    def account_channels(self, account: str, destination_account, ledger_index='validated') -> dict:
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
        return self._call('account_lines', params)

    def account_currencies(self, account: str, account_index=0, ledger_index="validated", strict=True) -> dict:
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

    def account_objects(self, account: str, ledger_index="validated", limit=10, type="state") -> dict:
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

    def account_tx(self, account: str, binary=False, forward=False,
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

    def gateway_balances(self, account: str, hotwallet=None, ledger_index="validated", strict=True) -> dict:
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

    def tx(self, tx: str, binary=False) -> dict:
        """
        Method retrieves information on a single transaction
        Reference: https://developers.ripple.com/tx.html
        """
        params = dict(
            transaction=tx,
            binary=binary
        )
        return self._call('tx', params)

    def noripple_check(self, account: str, ledger_index='current', limit=2, role="gateway", transactions=True) -> dict:
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
