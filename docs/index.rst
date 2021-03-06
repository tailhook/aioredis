.. aioredis documentation master file, created by
   sphinx-quickstart on Thu Jun 12 22:57:11 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

aioredis
========

asyncio (:pep:`3156`) Redis support.

The library is intended to provide simple and clear interface to Redis
based on :term:`asyncio`.


Features
--------

- Connections pool
- Low-level & high-level API
- :term:`hiredis` parser

.. note:: High-level API is under development

Installation
------------

The easiest way to install aioredis is by using the package on PyPi::

   pip install aioredis

Requirements
------------

- Python 3.3 and :term:`asyncio` or Python 3.4+
- :term:`hiredis`

Contribute
----------

- Issue Tracker: https://github.com/aio-libs/aioredis/issues
- Source Code: https://github.com/aio-libs/aioredis

Feel free to file an issue or make pull request if you find any bugs or have
some suggestions for library improvement.

License
-------

The aioredis is offered under `MIT license`_.

----

Contents
========

.. toctree::
   :maxdepth: 3

   api_reference
   mixins
   examples
   releases
   glossary

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _MIT license: https://github.com/aio-libs/aioredis/blob/master/LICENSE
