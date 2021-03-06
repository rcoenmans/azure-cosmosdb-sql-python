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

import datetime
import requests

from ._auth import (
    _get_authorization_token
)

from ._constants import (
    DEFAULT_X_MS_VERSION,
    DEFAULT_USER_AGENT_STRING,

    DEFAULT_PROTOCOL,
    DEFAULT_SOCKET_TIMEOUT,
    SERVICE_HOST_BASE
)

from ._error import (
    ERROR_MISSING_INFO,
    _validate_not_none
)

from ._conversion import (
    _bool_to_str,
    _datetime_to_utc_string
)

from ._deserialization import (
    _parse_json,
    _parse_json_to_databases,
    _parse_json_to_database
)

from .models import Database
from .models import Collection

from ._http import HTTPRequest
from ._http.httpclient import _HTTPClient

class DocumentService(object):
    def __init__(self, account_name, account_key):
        self.account_name = account_name
        self.account_key = account_key

        self._http_client = _HTTPClient(
            protocol = DEFAULT_PROTOCOL,
            session  = requests.Session(),
            timeout  = DEFAULT_SOCKET_TIMEOUT,
        )


    def get_databases(self):
        '''
        Retrieves a list of all databases.
 
        :return: A list of databases.
        :rtype: List<Database(:class:`~azure.cosmosdb.sql.models.Database`)>
        '''
        request = HTTPRequest()
        request.method = 'GET'
        request.host = self._get_host_location()
        request.path = self._get_path('dbs')
        request.headers = {
            'Cache-Control': 'no-cache',
            'User-Agent': DEFAULT_USER_AGENT_STRING,
            'Accept': 'application/json',
            'x-ms-version': DEFAULT_X_MS_VERSION,
            'x-ms-documentdb-query-iscontinuationexpected': _bool_to_str(False),
            'x-ms-date': _datetime_to_utc_string(datetime.datetime.utcnow())
        }
        request.headers['authorization'] = _get_authorization_token(
            self.account_key,
            '',
            'dbs',
            'GET',
            request.headers['x-ms-date'])

        return self._perform_request(request, _parse_json_to_databases)


    def get_database(self, database_name):
        '''
        Retrieves a database by its name.
 
        :param str database_name:
            The name of the database to retrieve.
        :return: A Database.
        :rtype: Database(:class:`~azure.cosmosdb.sql.models.Database`)
        '''
        _validate_not_none('database_name', database_name)

        request = HTTPRequest()
        request.method = 'GET'
        request.host = self._get_host_location()
        request.path = self._get_path('dbs', database_name)
        request.headers = {
            'Cache-Control': 'no-cache',
            'User-Agent': DEFAULT_USER_AGENT_STRING,
            'Accept': 'application/json',
            'x-ms-version': DEFAULT_X_MS_VERSION,
            'x-ms-documentdb-query-iscontinuationexpected': _bool_to_str(False),
            'x-ms-date': _datetime_to_utc_string(datetime.datetime.utcnow())
        }

        request.headers['authorization'] = _get_authorization_token(
            self.account_key,
            'dbs/{}'.format(database_name),
            'dbs',
            'GET',
            request.headers['x-ms-date'])

        return self._perform_request(request, _parse_json_to_database)


    def _get_host_location(self):
        return '{}.{}'.format(self.account_name, SERVICE_HOST_BASE)


    def _get_path(self, resource_type, resource_id=None):
        if resource_id:
            return '/{}/{}'.format(resource_type, resource_id)
        else:
            return '/{}'.format(resource_type)


    def _perform_request(self, request, parser = None):
        response = self._http_client.perform_request(request)
        
        if parser:
            return parser(_parse_json(response))    
        else:
            return response