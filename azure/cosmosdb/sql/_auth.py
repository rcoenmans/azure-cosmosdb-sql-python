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
    def __init__(self, account_key):
        self.account_key = account_key

    def get_authorization_token(self, resource_id, resource_type, verb, headers):
        key = base64.b64decode(self.account_key)
        msg = '{}\n{}\n{}\n{}\n{}\n'.format(
            verb.lower(), 
            resource_type.lower(), 
            resource_id, 
            str(headers['x-ms-date']).lower(), 
            str(headers['date']).lower())
         
        digest = hmac.new(
            key, 
            msg.encode('utf-8'), 
            sha256).digest()
        signature = base64.encodebytes(digest).decode('utf-8')

        return 'type=master&ver=1.0&sig={}'.format(signature[:-1])