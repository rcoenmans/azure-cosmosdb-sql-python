# -------------------------------------------------------------------------
# Copyright (c) Microsoft.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------

from ._error import (
    ERROR_VALUE_SHOULD_BE_BYTES_OR_STREAM
)

def _get_data_bytes_or_stream_only(param_name, param_value):
    '''Validates the request body passed in is a stream/file-like or bytes
    object.'''
    if param_value is None:
        return b''

    if isinstance(param_value, bytes) or hasattr(param_value, 'read'):
        return param_value

    raise TypeError(ERROR_VALUE_SHOULD_BE_BYTES_OR_STREAM.format(param_name))