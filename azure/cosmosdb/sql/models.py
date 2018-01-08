# -----------------------------------------------------------------------------
# The MIT License (MIT)
# Copyright (c) 2017 Robbie Coenmans
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------

import sys

if sys.version_info < (3,):
    from collections import Iterable

    _unicode_type = unicode
else:
    from collections.abc import Iterable

    _unicode_type = str

class ResourceProperties(object):
    def __init__(self):
        self.last_modified = None
        self.etag = None


class Database(object):
    def __init__(self):
        self.id = None
        self._rid = None
        self._self = None
        self._etag = None
        self._colls = None
        self._users = None
        self._ts = None

    def _parse(obj):
        if 'Databases' in obj:
            dbs = []
            for db in obj['Databases']: 
                dbs.append(Database._parse(db))
            return dbs
        else:
            db = Database()
            db.id = obj['id']
            db._rid = obj['_rid']
            db._self = obj['_self']
            db._etag = obj['_etag']
            db._colls = obj['_colls']
            db._users = obj['_users']
            db._ts = int(obj['_ts'])
            return db


class Collection(object):
    def __init__(self):
        self.id = None
        self.rid= None
        self.indexing_policy = None