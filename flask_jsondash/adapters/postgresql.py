"""Adapter for mongodb CRUD."""


def read(c_id=None):
    """Read a record."""
    raise NotImplemented('PostgreSQL is not yet supported.')


def update(c_id, data=None, fmt_modules=True):
    """Update a record."""
    if data is None:
        return
    raise NotImplemented('PostgreSQL is not yet supported.')


def create(data=None):
    """Add a new record."""
    raise NotImplemented('PostgreSQL is not yet supported.')


def delete(c_id):
    """Delete a record."""
    raise NotImplemented('PostgreSQL is not yet supported.')
