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

from six.moves.urllib.parse import quote as urllib_quote

from ._conversion import (
    _sign_string,
    _lower
)

def _get_authorization_token(account_key, resource_link, resource_type, verb, date):
    '''
    Returns the authorization header.

    :param str account_key:
        The account key.
    :param str resource_link:
        Identity property of the resource that the request is directed at, 
        eg. "dbs/MyDatabase/colls/MyCollection".
    :param str resource_type:
        Type of resource that the request is for, eg. "dbs", "colls", "docs".
    :param str verb:
        HTTP verb, such as GET, POST or PUT.
    :param str date:
        String of UTC date and time in HTTP-date format. This same date 
        (in same format) also needs to be passed as x-ms-date header in the 
        request.
    '''
    string_to_sign = '{}\n{}\n{}\n{}\n\n'.format(
        _lower(verb),
        _lower(resource_type),
        resource_link,
        _lower(date)
    )
    signature = _sign_string(account_key, string_to_sign)
    return urllib_quote('type=master&ver=1.0&sig={}'.format(signature), '-_.!~*\'()')