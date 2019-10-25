import base64
import json

from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


class RippleRPCClient(object):
    def __init__(self, node: str, username: str = None, password: str = None):
        """
        :param node: URL of rippled node
        :param username: username of admin in rippled node
        :param password: password of admin in rippled node
        """
        self.node = node
        self.username = username
        self.password = password

    def __repr__(self):
        return '<RippleRPCClient node=%r>' % self.node

    @property
    def request_headers(self):
        headers = {'Content-Type': 'application/json'}
        if self.username and self.password:
            string = '{}:{}'.format(self.username, self.password)
            base64string = base64.standard_b64encode(
                string.encode('utf-8')).decode('utf-8')
            headers.update({'Authorization': 'Basic {}'.format(base64string)})
        return headers

    def _call(self, method: str, params: dict) -> dict:
        """Base method which sends requests to node
        :param method: JSON-RPC method of rippled
        :param params: parameters of the request
        """
        payload = json.dumps({
            "method": method,
            "params": [
                params
            ]
        }).encode('utf-8')
        req = Request(method='POST', url=self.node,
                      data=payload, headers=self.request_headers)
        try:
            with urlopen(req) as res:
                res_json = json.loads(res.fp.read().decode('utf-8'))
                if res.status == 200 and res_json.get('result'):
                    return res_json.get('result')
                return res_json
        except HTTPError as err:
            if err.code == 403:
                return {"status": "error",
                        "msg": "{} {}".format(err.code, err.reason),
                        "text": "Admin methods are only allowed on nodes with admin access."}
            return {"status": "error", "msg": err}
        except URLError as err:
            return {"status": "error",
                    "msg": err}

    def account_info(self, account: str, strict: bool = True,
                     ledger_index: str = 'current', queue: bool = True) ->dict:
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

    def account_channels(
            self, account: str, destination_account: str,
            ledger_index: str = 'validated') ->dict:
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

    def account_currencies(
            self, account: str, account_index: int = 0,
            ledger_index: str = "validated", strict: bool = True) ->dict:
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

    def account_objects(
            self, account: str, ledger_index: str = "validated", limit: int = 10,
            type: str = "state") ->dict:
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
         Method retrieves a list of offers made by a given account that are outstanding
         as of a particular ledger version.
         Reference: https://developers.ripple.com/account_offers.html
        """
        return self._call('account_offers', params=dict(account=account))

    def account_tx(self, account: str, binary: bool = False, forward: bool = False,
                   ledger_index_max: int = -1, ledger_index_min: int = -1,
                   limit: int = 0) ->dict:
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

    def gateway_balances(
            self, account: str, hotwallet: list = None,
            ledger_index: str = "validated", strict: bool = True) ->dict:
        """
        Method calculates the total balances issued by a given account, optionally excluding amounts held by
        operational addresses.
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

    def noripple_check(
            self, account: str, ledger_index: str = 'current', limit: int = 2,
            role: str = "gateway", transactions: bool = True) ->dict:
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

    def ledger(
            self, ledger_index: str = 'validated', accounts: bool = False,
            full: bool = False, transactions: bool = False, expand: bool = False,
            owner_funds: bool = False) ->dict:
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

    def ledger_data(self, ledger_hash: str, binary: bool = True,
                    limit: int = 5) -> dict:
        """
        Method retrieves contents of the specified ledger. You can iterate through several calls to retrieve the entire
        contents of a single ledger version.
        Reference: https://developers.ripple.com/ledger_data.html
        """
        params = dict(
            ledger_hash=ledger_hash,
            binary=binary,
            limit=limit
        )
        return self._call('ledger_data', params)

    def ledger_entry(
            self, account_root: str, ledger_index: str = "validated",
            type: str = "account_root") ->dict:
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

    def sign(self, tx_json: dict = None, secret: str = '',
             offline: bool = False, fee_mult_max: int = 1000) -> dict:
        """
        The sign method takes a transaction in JSON format and a secret key,
        and returns a signed binary representation of the transaction. The result is always different,
        even when you provide the same transaction JSON and secret key.
        Reference: https://developers.ripple.com/sign.html
        """
        tx_json = {} if tx_json is None else tx_json
        params = dict(
            offline=offline,
            secret=secret,
            tx_json=tx_json,
            fee_mult_max=fee_mult_max
        )
        return self._call('sign', params)

    def sign_for(
            self, account: str, seed: str, key_type: str = "ed25519",
            tx_json: dict = None) ->dict:
        """
        Method provides one signature for a multi-signed transaction.
        Reference: https://developers.ripple.com/sign_for.html
        """
        params = dict(
            account=account,
            seed=seed,
            key_type=key_type,
            tx_json=tx_json
        )
        return self._call('sign_for', params)

    def submit(self, tx_blob: str, fail_hard: bool = False) -> dict:
        """
        Method applies a transaction and sends it to the network to be confirmed and included in future ledgers.
        Reference: https://developers.ripple.com/submit.html
        """
        params = dict(
            tx_blob=tx_blob,
            fail_hard=fail_hard
        )
        return self._call('submit', params)

    def submit_mutlisigned(self, tx_json: dict = None):
        """
        Method applies a multi-signed transaction and sends it to the network to be included in future ledgers.
        (You can also submit multi-signed transactions in binary form using the submit command in submit-only mode.)
        Reference: https://developers.ripple.com/submit_multisigned.html
        """
        tx_json = {} if tx_json is None else tx_json
        return self._call('submit_multisigned', params=dict(tx_json=tx_json))

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

    def tx(self, tx: str, binary: bool = False) -> dict:
        """
        Method retrieves information on a single transaction
        Reference: https://developers.ripple.com/tx.html
        """
        params = dict(
            transaction=tx,
            binary=binary
        )
        return self._call('tx', params)

    def tx_history(self, start: int = 0) -> dict:
        """
        Method retrieves some of the most recent transactions made.
        This method is deprecated, and may be removed without further notice.
        Reference: https://developers.ripple.com/tx_history.html
        """
        return self._call('tx_history', params=dict(start=start))

    def book_offers(self, taker: str, issuer: str,
                    taker_gets_currency: str = "XRP",
                    taker_pays_currency: str = "USD", limit: int = 10) ->dict:
        """
        Method retrieves a list of offers, also known as the order book, between two currencies.
        If the results are very large, a partial result is returned with a marker so that later requests
        can resume from where the previous one left off.
        Reference: https://developers.ripple.com/book_offers.html
        """
        params = dict(
            taker=taker,
            taker_gets=dict(
                currency=taker_gets_currency
            ),
            taker_pays=dict(
                currency=taker_pays_currency,
                issuer=issuer
            ),
            limit=limit
        )
        return self._call('book_offers', params)

    def ripple_path_find(self, destination_account: str, currency: str,
                         issuer: str, value: str, source_account: str,
                         source_currencies: list = None) ->dict:
        """
        The ripple_path_find method is a simplified version of the path_find method that provides
        a single response with a payment path you can use right away. It is available in both the WebSocket
        and JSON-RPC APIs. However, the results tend to become outdated as time passes.
        Instead of making multiple calls to stay updated, you should instead use the path_find method
        to subscribe to continued updates where possible.
        Reference: https://developers.ripple.com/ripple_path_find.html
        """
        source_currencies = [] if source_currencies is None else source_currencies
        params = dict(
            destination_account=destination_account,
            destination_amount=dict(
                currency=currency, issuer=issuer, value=value),
            source_account=source_account,
            source_currencies=[dict(currency=currency)
                               for currency in source_currencies])
        return self._call('ripple_path_find', params)

    def channel_authorize(self, channel_id: str,
                          secret: str, amount: str) -> dict:
        """
        Method creates a signature that can be used to redeem a specific amount of XRP from a payment channel.
        Reference: https://developers.ripple.com/channel_authorize.html
        """
        params = dict(
            channel_id=channel_id,
            secret=secret,
            amount=amount

        )
        return self._call('channel_authorize', params)

    def channel_verify(self, channel_id: str, signature: str,
                       public_key: str, amount: str) -> dict:
        """
        Method checks the validity of a signature that can be used to redeem a specific amount of XRP
        from a payment channel.
        Reference: https://developers.ripple.com/channel_verify.html
        """
        params = dict(
            channel_id=channel_id,
            signature=signature,
            public_key=public_key,
            amount=amount
        )
        return self._call('channel_verify', params)

    def fee(self) -> dict:
        """
        Method reports the current state of the open-ledger requirements for the transaction cost.
        This requires the FeeEscalation amendment to be enabled.
        Reference: https://developers.ripple.com/fee.html
        """
        return self._call('fee', params=dict())

    def server_info(self) -> dict:
        """
        Method asks the server for a human-readable version of various information
         about the rippled server being queried.
        Reference: https://developers.ripple.com/server_info.html
        """
        return self._call('server_info', params=dict())

    def server_state(self) -> dict:
        """
        Method asks the server for various machine-readable information about the rippled server's current state.
        Same as server_info method, but more readable.
        Reference: https://developers.ripple.com/server_state.html
        """
        return self._call('server_state', params=dict())

    def ping(self) -> dict:
        """
        Method returns an acknowledgement, so that clients can test the connection status and latency.
        Reference: https://developers.ripple.com/ping.html
        """
        return self._call('ping', params=dict())

    def random(self) -> dict:
        """
        Method provides a random number to be used as a source of entropy for random number generation by clients.
        Reference: https://developers.ripple.com/random.html
        """
        return self._call('random', params=dict())

    def validation_create(self, secret: str) -> dict:
        """
        Method generates the keys for a rippled validator.
        Similar to the wallet_propose method, this command makes no real changes,
        but only generates a set of keys in the proper format.
        This request is an admin method that cannot be run by unprivileged users!
        Reference: https://developers.ripple.com/validation_create.html
        """
        return self._call('validation_create', params=dict(secret=secret))

    def wallet_propose(self, seed: str='', passphrase: str='', key: str="secp256k1") -> dict:
        """
        Method to generate a key pair and XRP Ledger address.
        This command only generates key and address values, and does not affect the XRP Ledger itself in any way.
        This request is an admin method that cannot be run by unprivileged users!
        Reference: https://developers.ripple.com/wallet_propose.html
        """
        params = dict(
            key=key
        )
        if seed:
            params['seed'] = seed
        if passphrase:
            params['passphrase'] = passphrase
        return self._call('wallet_propose', params)

    def can_delete(self, can_delete: int) -> dict:
        # TODO: implement needed config to tests the method
        """
        With online_delete and advisory_delete configuration options enabled, the can_delete method
        informs the rippled server of the latest ledger which may be deleted.
        This request is an admin method that cannot be run by unprivileged users!
        Reference: https://developers.ripple.com/can_delete.html
        """
        return self._call('can_delete', params=dict(can_delete=can_delete))

    def connect(self, ip: str, port: int = 6561) -> dict:
        """
        Method forces the rippled server to connect to a specific peer rippled server.
        This request is an admin method that cannot be run by unprivileged users!
        Reference: https://developers.ripple.com/connect.html
        """
        params = dict(
            ip=ip,
            port=port
        )
        return self._call('connect', params)

    def stop(self) -> dict:
        """
        Method gracefully shuts down the server.
        This request is an admin method that cannot be run by unprivileged users!
        Reference: https://developers.ripple.com/stop.html
        """
        return self._call('stop', params=dict())

    def consensus_info(self) -> dict:
        """
        Method provides information about the consensus process for debugging purposes.
        This request is an admin method that cannot be run by unprivileged users
        Reference: https://developers.ripple.com/consensus_info.html
        """
        return self._call('consensus_info', params=dict())

    def feature(self, feature: str, vetoed: bool) -> dict:
        """
        Method returns information about amendments this server knows about, including whether
        they are enabled and whether the server is voting in favor of those amendments in the amendment process.
        The feature method is an admin method that cannot be run by unprivileged users.
        Reference: https://developers.ripple.com/feature.html
        """
        params = dict(
            feature=feature,
            vetoed=vetoed
        )
        return self._call('feature', params)

    def fetch_info(self, clear: bool) -> dict:
        """
        Method returns information about objects that this server is currently fetching from the network,
        and how many peers have that information. It can also be used to reset current fetches.
        The fetch_info method is an admin method that cannot be run by unprivileged users.
        Reference: https://developers.ripple.com/fetch_info.html
        """
        return self._call('fetch_info', params=dict(clear=clear))

    def get_counts(self, min_count: int) -> dict:
        """
        Method provides various stats about the health of the server, mostly the number of objects of different types
        that it currently holds in memory.
        The get_counts method is an admin method that cannot be run by unprivileged users.
        Reference: https://developers.ripple.com/get_counts.html
        """
        return self._call('get_counts', params=dict(min_count=min_count))

    def peers(self) -> dict:
        """
        Method returns a list of all other rippled servers currently connected to this one,
        including information on their connection and sync status.
        The peers request is an admin method that cannot be run by unprivileged users!
        Reference: https://developers.ripple.com/peers.html
        """
        return self._call('peers', params=dict())

    def print(self) -> dict:
        """
        Method returns the current status of various internal subsystems, including peers,
        the ledger cleaner, and the resource manager.
        The print request is an admin method that cannot be run by unprivileged users!
        Reference: https://developers.ripple.com/print.html
        """
        return self._call('print', params=dict())

    def validator_list_sites(self) -> dict:
        """
        Method returns status information of sites serving validator lists.
        The validator_list_sites request is an admin method that cannot be run by unprivileged users!
        Reference: https://developers.ripple.com/validator_list_sites.html
        """
        return self._call('validator_list_sites', params=dict())

    def validators(self) -> dict:
        """
        Method returns human readable information about the current list of published and trusted validators used
        by the server.
        The validators request is an admin method that cannot be run by unprivileged users!
        Reference: https://developers.ripple.com/validators.html
        """
        return self._call('validators', params=dict())
