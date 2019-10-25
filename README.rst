===================
python-ripple-lib
===================
| python-ripple-lib is a client library to access Ripple `rippled API <https://developers.ripple.com/rippled-api.html>`_ and `Data API <https://developers.ripple.com/data-api.html>`_.
| Currently it supports public and admin methods (some of them still are work in progress though). List of implemented methods is displayed below. Basically, it's just a wrapper on top of http requests made to API.

Available on `PyPi <https://pypi.org/project/python-ripple-lib/>`_

Installation
-------------

To install the package from PyPi run the following command

::

    pip install python-ripple-lib

If you want to install package from this repo, use ``setup.py``

::

    python setup.py install

If you want to install package just for development purposes, use another command

::

    python setup.py develop

This command creates symlinks to package files instead of copying it to package directory

JSON-RPC Methods
----------------

| Most of JSON-RPC methods are implemented inside, for the full list of methods please refer to list of `Public <https://developers.ripple.com/public-rippled-methods.html>`_ and `Admin <https://developers.ripple.com/admin-rippled-methods.html>`_ methods from ripple documentation
| How to use:

.. code-block:: python3

    from ripple_api import RippleRPCClient

    # module supports authentication as well
    rpc = RippleRPCClient('http://s1.ripple.com:51234/', username='<username>', password='<password>')
    account_info = rpc.account_info('r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59')


Data API Methods
----------------

| Most of Data API requests are implemented here as well, fll list located in `here <https://developers.ripple.com/data-api.html>`_
| How to use:

.. code-block:: python

    from ripple_api import RippleDataAPIClient

    api = RippleDataAPIClient('https://data.ripple.com')
    identifier = '3170DA37CE2B7F045F889594CBC323D88686D2E90E8FFD2BBCD9BAD12E416DB5'
    query_params = dict(transactions='true')
    ledger_info = api.get_ledger(ledger_identifier=identifier, **query_params)


| Example of get_transactions() query:

.. code-block:: python

   from ripple_api import RippleDataAPIClient
   from pprint import pprint

   api = RippleDataAPIClient('https://data.ripple.com')
   # to get name of a specific transaction type please refer to this link:
   # https://developers.ripple.com/transaction-types.html
   query_params = dict(type="Payment")
   txs = api.get_transactions(**query_params)
   pprint(txs)



Additional methods
------------------
Send XRP from address tp address via Account instance:

.. code-block:: python

    from ripple_api import Account

    taker = 'rYuHe4VogMzYmvHpSsgGxRH97UvqumgER'
    issuer = 'rMEmLrfkfooLjdkerU5TKTcAVpfy9fpSxt'
    seed = '<account_seed>'
    account = Account('http://localhost:5005', issuer, seed)
    tx_info = account.send_xrp(issuer=issuer, taker=taker, secret=seed, amount=10)

Contributing
------------------------

1. Fork this project
2. Clone it locally
3. Add your changes
4. Run tests:

::

    make test

or

::

    python -m unittest -v

5. If tests are successful and everything is OK, commit to your local fork
6. Submit a pull request to this repo
