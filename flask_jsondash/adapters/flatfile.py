"""Adapter for flat file crud.

Options for flat-file include:

* local file system
* Any typical filesystem mount available to the
    python os module (e.g SMB, NFS, etc)

"""

from datetime import datetime as dt

from flask_jsondash import settings
from flask_jsondash.adapters import utils


def read(c_id=None):
    """Read a record."""


def update(c_id, data=None, fmt_modules=True):
    """Update a record."""


def create(data=None):
    """Add a new record."""


def delete(c_id):
    """Delete a record."""
