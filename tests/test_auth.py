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

import unittest
import datetime

from azure.cosmosdb.sql._auth import _get_authorization_token

class AuthTest(unittest.TestCase):
    def setUp(self):
        self.account_key = 'ZACfYMyDQHyGf0UZ2UdWCcfTyfQ0zmQnBLJ49AELlqBaHWseoRWpia7IOkQPXHKFfvFs98MMKNcUFY0CUfrDjA=='
        self.resource_link = 'dbs/ToDoList'
        self.resource_type = 'dbs'

    def test_get_authorization_token(self):
        # Generate Authorization token
        auth_token = _get_authorization_token(
            self.account_key, 
            self.resource_link, 
            self.resource_type, 
            'GET', 
            datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'))

        # Asserts
        self.assertLess(0, len(auth_token))