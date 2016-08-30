"""Db adapter utility functions."""

import json
from datetime import datetime as dt


def reformat_data(data, c_id):
    """Format/clean existing config data to be re-inserted into database."""
    data.update(dict(id=c_id, date=dt.now()))
    return data


def format_modules(data):
    """Form module data for JSON."""
    modules = []
    # Format modules data for json usage
    for item in data:
        if item.startswith('module_'):
            val_json = json.loads(data[item])
            modules.append(val_json)
    return modules
