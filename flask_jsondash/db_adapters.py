"""A translation adapter for making queries between storage types.

Types are either:
1. MongoDB collections.
2. Flat json files.
3. PostgreSQL json fields.

"""

from datetime import datetime as dt

import settings

DB_NAME = settings.ACTIVE_DB

if DB_NAME == 'mongo':
    from adapters.mongo import (
        read,
        update,
        create,
        delete,
    )
elif DB_NAME == 'flatfile':
    from adapters.flatfile import (
        read,
        update,
        create,
        delete,
    )
else:
    raise NotImplemented('PostgreSQL is not yet supported.')
