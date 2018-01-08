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

from json import loads
from dateutil import parser

from .models import (
    ResourceProperties
)

def _parse_base_properties(response):
    '''
    Extracts basic response headers.
    '''
    resource_properties = ResourceProperties()
    resource_properties.last_modified = parser.parse(response.headers.get('last-modified'))
    resource_properties.etag = response.headers.get('etag')

    return resource_properties


def _parse_json(response):
    '''
    Parses the response body (JSON) to dictionary.
    '''
    if response is None or response.body is None:
        return None
    
    # Decode bytes to string
    body = response.body.decode('UTF-8')
    
    # Parse JSON body to dictionary
    return loads(body)


def _parse_json_to_class(response, result_class):
    '''
    Parses the response body to a class of given type.
    '''
    if response is None or response.body is None:
        return None
    
    # Parse JSON body to dictionary
    dict = _parse_json(response)

    # Return result class
    return result_class._parse(dict)