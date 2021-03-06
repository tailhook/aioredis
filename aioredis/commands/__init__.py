import asyncio

from aioredis.connection import create_connection
from .generic import GenericCommandsMixin
from .string import StringCommandsMixin
from .hash import HashCommandsMixin
from .hyperloglog import HyperLogLogCommandsMixin
from .set import SetCommandsMixin
from .sorted_set import SortedSetCommandsMixin
from .transaction import TransactionsCommandsMixin
from .list import ListCommandsMixin
from .scripting import ScriptingCommandsMixin

__all__ = ['create_redis', 'Redis']


class Redis(GenericCommandsMixin, StringCommandsMixin,
            HyperLogLogCommandsMixin, SetCommandsMixin,
            HashCommandsMixin, TransactionsCommandsMixin,
            SortedSetCommandsMixin, ListCommandsMixin,
            ScriptingCommandsMixin):
    """High-level Redis interface.

    Gathers in one place Redis commands implemented in mixins.

    For commands details see: http://redis.io/commands/#connection
    """

    def __init__(self, connection):
        self._conn = connection

    def __repr__(self):
        return '<Redis {!r}>'.format(self._conn)

    def close(self):
        self._conn.close()

    @property
    def db(self):
        """Currently selected db index."""
        return self._conn.db

    @property
    def encoding(self):
        """Current set codec or None."""
        return self._conn.encoding

    @property
    def connection(self):
        """:class:`aioredis.RedisConnection` instance."""
        return self._conn

    @property
    def closed(self):
        """True if connection is closed."""
        return self._conn.closed

    @asyncio.coroutine
    def auth(self, password):
        """Authenticate to server.

        This method wraps call to :meth:`aioredis.RedisConnection.auth()`
        """
        return self._conn.auth(password)

    @asyncio.coroutine
    def echo(self, message):
        """Echo the given string."""
        return (yield from self._conn.execute('ECHO', message))

    @asyncio.coroutine
    def ping(self):
        """Ping the server."""
        return (yield from self._conn.execute('PING'))

    @asyncio.coroutine
    def quit(self):
        """Close the connection."""
        return (yield from self._conn.execute('QUIT'))

    @asyncio.coroutine
    def select(self, db):
        """Change the selected database for the current connection.

        This method wraps call to :meth:`aioredis.RedisConnection.select()`
        """
        return self._conn.select(db)


@asyncio.coroutine
def create_redis(address, *, db=None, password=None,
                 encoding=None, commands_factory=Redis,
                 loop=None):
    """Creates high-level Redis interface.

    This function is a coroutine.
    """
    conn = yield from create_connection(address, db=db,
                                        password=password,
                                        encoding=encoding,
                                        loop=loop)
    return commands_factory(conn)
