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

import platform

__version__ = '0.0.1'

# UserAgent string sample: 'Azure-CosmosDB-Sql/0.0.1 (Python CPython 3.4.2; Windows 10)'
USER_AGENT_STRING_PREFIX = 'Azure-CosmosDB-Sql/{}-'.format(__version__)
USER_AGENT_STRING_SUFFIX = '(Python {} {}; {} {})'.format(platform.python_implementation(),
                                                          platform.python_version(), platform.system(),
                                                          platform.release())

# default values for common package, in case it is used directly
DEFAULT_X_MS_VERSION = '2017-11-15'
DEFAULT_USER_AGENT_STRING = '{} {}'.format(USER_AGENT_STRING_PREFIX, USER_AGENT_STRING_SUFFIX)

# Live DocumentService URLs
SERVICE_HOST_BASE = 'documents.azure.com'
DEFAULT_PROTOCOL = 'https'

# Socket timeout in seconds
DEFAULT_SOCKET_TIMEOUT = 20

# Encryption constants
_ENCRYPTION_PROTOCOL_V1 = '1.0'