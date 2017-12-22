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

from hashlib import sha256

import hmac
import base64

class _DocumentServiceAuthentication(object):
    def __init__(self, document_service=None):
        self.document_service = document_service

    def get_authorization_token(self, resource_id = '', resource_type = '', verb = '', headers):
        account_key = self.document_service.account_key



        text = '{verb}\n{resource_type}\n{resource_id_or_fullname}\n{x_date}\n{http_date}\n'.format(
            verb=(verb.lower() or ''),
            resource_type=(resource_type.lower() or ''),
            resource_id_or_fullname=(resource_id_or_fullname or ''),
            x_date=headers.get(http_constants.HttpHeaders.XDate, '').lower(),
            http_date=headers.get(http_constants.HttpHeaders.HttpDate, '').lower())