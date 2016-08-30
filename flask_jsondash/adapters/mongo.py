"""Adapter for mongodb CRUD."""

from __future__ import absolute_import
from datetime import datetime as dt

from pymongo import MongoClient

from .. import settings
from . import utils


client = MongoClient(host=settings.DB_URI, port=settings.DB_PORT)
conn = client[settings.DB_NAME]
coll = conn[settings.DB_TABLE]


def read(c_id=None):
    """Read a record."""
    if c_id is None:
        return coll.find()
    else:
        return coll.find_one(dict(id=c_id))


def update(c_id, data=None, fmt_modules=True):
    """Update a record."""
    if data is None:
        return
    modules = utils.format_modules(data) \
        if fmt_modules else data.get('modules')
    save_conf = {
        '$set': {
            'name': data.get('name', 'NONAME'),
            'modules': modules,
            'date': dt.now()
        }
    }
    coll.update(dict(id=c_id), save_conf)


def create(data=None):
    """Add a new record in mongo."""
    if data is None:
        return
    coll.insert(data)


def delete(c_id):
    """Delete a record."""
    coll.delete_one(dict(id=c_id))
