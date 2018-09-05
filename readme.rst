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

To install the package from PyPi run the following command::
    pip install ripple-python-rpc

If you want to install package from this repo, use ``setup.py``::
    python setup.py install

If you want to install package just for development purposes, use another command::
    python setup.py develop

This command creates symlinks to package files instead of copying it to package directory

API Methods
------------

This client supports either public or admin JSON-RPC methods only (some of the node requests can be only via Websocket API or using CLI):

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


