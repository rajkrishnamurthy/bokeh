#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2018, Anaconda, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
''' Bokeh Application Handler to execute on_session_destroyed callbacks defined
on the Document.

'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports

# External imports

# Bokeh imports
from .lifecycle import LifecycleHandler

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

class DocumentLifecycleHandler(LifecycleHandler):
    ''' Calls on_session_destroyed callbacks defined on the Document.

    '''

    def __init__(self, *args, **kwargs):
        super(DocumentLifecycleHandler, self).__init__(*args, **kwargs)
        self._on_session_destroyed = _on_session_destroyed

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

def _on_session_destroyed(session_context):
    '''
    Calls any on_session_destroyed callbacks defined on the Document
    '''
    for callback in session_context._document._session_destroyed_callbacks:
        callback(session_context)

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
