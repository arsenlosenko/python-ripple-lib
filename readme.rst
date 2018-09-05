===================
python-ripple-rpc
===================
Description
------------

python-ripple-rpc is a small client library to access Ripple `rippled API <https://developers.ripple.com/rippled-api.html>`_.
Currently it supports public and admin methods (some of them still are work in progress though). List of implemented methods will be displayed below.
Basically, it's just a wrapper on top of http requests made to API.

Installation
-------------

To install the package from PyPi run the following command

::

    pip install ripple-python-rpc

If you want to install package from this repo, use ``setup.py``

::

    python setup.py install

If you want to install package just for development purposes, use another command

::

    python setup.py develop

This command creates symlinks to package files instead of copying it to package directory

API Methods
------------

This client supports either public or admin JSON-RPC methods only (some of the node requests can be only via Websocket API or using CLI):
Methods that are work in progress marked with (WIP)

* `Public methods <https://developers.ripple.com/public-rippled-methods.html>`_
    * `Account Methods <https://developers.ripple.com/account-methods.html>`_
        * `account_channels <https://developers.ripple.com/account_channels.html>`_
        * `account_currencies <https://developers.ripple.com/account_currencies.html>`_
        * `account_info <https://developers.ripple.com/account_info.html>`_
        * `account_lines <https://developers.ripple.com/account_lines.html>`_
        * `account_objects <https://developers.ripple.com/account_objects.html>`_
        * `account_offers <https://developers.ripple.com/account_offers.html>`_
        * `account_tx <https://developers.ripple.com/account_tx.html>`_
        * `gateway_balances <https://developers.ripple.com/gateway_balances.html>`_
        * `no_ripple_check <https://developers.ripple.com/gateway_balances.html>`_
    * `Ledger Methods <https://developers.ripple.com/ledger-methods.html>`_
        * `ledger <https://developers.ripple.com/ledger.html>`_
        * `ledger_closed <https://developers.ripple.com/ledger_closed.html>`_
        * `ledger_current <https://developers.ripple.com/ledger_current.html>`_
        * `ledger_data <https://developers.ripple.com/ledger_data.html>`_
        * `ledger_entry <https://developers.ripple.com/ledger_entry.html>`_
    * `Transaction Methods <https://developers.ripple.com/transaction-methods.html>`_
        * `sign <https://developers.ripple.com/sign.html>`_ (WIP)
        * `sign_for <https://developers.ripple.com/sign_for.html>`_ (WIP)
        * `submit <https://developers.ripple.com/submit.html>`_ (WIP)
        * `submit_multisigned <https://developers.ripple.com/submit_multisigned.html>`_ (WIP)
        * `transaction_entry <https://developers.ripple.com/transaction_entry.html>`_
        * `tx <https://developers.ripple.com/tx.html>`_
        * `tx_history <https://developers.ripple.com/tx_history.html>`_
    * `Path and Order Book Methods <https://developers.ripple.com/path-and-order-book-methods.html>`_
        * `book_offers <https://developers.ripple.com/book_offers.html>`_
        * `ripple_path_find <https://developers.ripple.com/ripple_path_find.html>`_
    * `Payment Channel Methods <https://developers.ripple.com/payment-channel-methods.html>`_
        * `channel_authorize <https://developers.ripple.com/channel_authorize.html>`_ (WIP)
        * `channel_verify <https://developers.ripple.com/channel_verify.html>`_ (WIP)
    * `Server Info Methods <https://developers.ripple.com/server-info-methods.html>`_
        * `fee <https://developers.ripple.com/fee.html>`_
        * `server_info <https://developers.ripple.com/server_info.html>`_
        * `server_state <https://developers.ripple.com/server_state.html>`_
    * `Utility Methods <https://developers.ripple.com/utility-methods.html>`_
        * `ping <https://developers.ripple.com/ping.html>`_
        * `random <https://developers.ripple.com/ranndom.html>`_
* `Admin Methods <https://developers.ripple.com/admin-rippled-methods.html>`_
        * `Key Generations Methods <https://developers.ripple.com/key-generation-methods.html>`_
            * `validation create <https://developers.ripple.com/validation_create.html>`_
            * `wallet_propose <https://developers.ripple.com/wallet_propose.html>`_
        * `Logging and Data Management Methods <https://developers.ripple.com/logging-and-data-management-methods.html>`_
            * `can_delete <https://developers.ripple.com/can_delete.html>`_
        * `Server Control Methods <https://developers.ripple.com/server-control-methods.html>`_
            * `connect <https://developers.ripple.com/connect.html>`_
            * `stop <https://developers.ripple.com/stop.html>`_
        * `Status and Debugging Methods <https://developers.ripple.com/status-and-debugging-methods.html>`_
            * `consensus_info <https://developers.ripple.com/consensus_info.html>`_
            * `feature <https://developers.ripple.com/feature.html>`_
            * `fetch_info <https://developers.ripple.com/fetch_info.html>`_
            * `get_counts <https://developers.ripple.com/get_counts.html>`_
            * `peers <https://developers.ripple.com/peers.html>`_
            * `print <https://developers.ripple.com/consensus_info.html>`_
            * `validator_list_sites <https://developers.ripple.com/validator_list_sites.html>`_
            * `validators <https://developers.ripple.com/validators.html>`_




