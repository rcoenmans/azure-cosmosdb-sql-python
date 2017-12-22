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

import requests
import datetime

from _auth import (
    _DocumentServiceAuthentication
)

from _constants import (
    DEFAULT_X_MS_VERSION,
    DEFAULT_USER_AGENT_STRING,

    DEFAULT_PROTOCOL,
    DEFAULT_SOCKET_TIMEOUT,
    SERVICE_HOST_BASE
)

from _error import (
    ERROR_MISSING_INFO
)

from azure.storage.common._http import (
    HTTPResponse,
    HTTPRequest,
    _HTTPClient
)

class DocumentService(object):
    def __init__(self, account_name, account_key):
        self.account_name = account_name
        self.account_key = account_key

        if not self.account_key:
            raise ValueError(ERROR_MISSING_INFO)

        self._http_client = _HTTPClient(
            protocol = DEFAULT_PROTOCOL,
            session  = requests.Session(),
            timeout  = DEFAULT_SOCKET_TIMEOUT,
        )


    def get_databases(self):
        request = HTTPRequest()
        request.method = 'GET'
        request.host_locations = self._get_host_location()
        request.path = self._get_path('dbs')
        request.headers = {
            'Cache-Control': 'no-cache',
            'User-Agent': DEFAULT_USER_AGENT_STRING,
            'x-ms-version': DEFAULT_X_MS_VERSION,
            'x-ms-documentdb-query-iscontinuationexpected': False,
            'x-ms-date': (datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'))
        }

    def get_database(self, database_name):
        request = HTTPRequest()
        request.method = 'GET'
        request.host_locations = self._get_host_location()
        request.path = self._get_path('dbs', database_name)
        request.headers = {
            'Cache-Control': 'no-cache',
            'User-Agent': DEFAULT_USER_AGENT_STRING,
            'Accept': 'application/json',
            'date': datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'),
            'x-ms-version': DEFAULT_X_MS_VERSION,
            'x-ms-documentdb-query-iscontinuationexpected': False,
            'x-ms-date': datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        }

        auth = _DocumentServiceAuthentication(self)
        auth_token = auth.get_authorization_token(database_name, 'dbs', 'GET', request.headers)
        request.headers['authorization'] = auth_token

        self._perform_request(request)


    def _get_host_location(self):
        location = {}
        location['primary'] = '{}.{}'.format(self.account_name, SERVICE_HOST_BASE)
        return location


    def _get_path(resource_name, resource_id=None):
        if resource_id:
            return '/{}/{}'.format(resource_name, resource_id)
        else:
            return '/{}'.format(resource_name)


    def _perform_request(self, request):
        response = self._http_client.perform_request(request)
        return response