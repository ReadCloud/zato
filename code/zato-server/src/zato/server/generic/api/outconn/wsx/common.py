# -*- coding: utf-8 -*-

"""
Copyright (C) 2023, Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# stdlib
from logging import getLogger

# Zato
from zato.common.api import WEB_SOCKET

# ################################################################################################################################
# ################################################################################################################################

if 0:
    from zato.common.typing_ import any_, callable_, stranydict, strnone
    from zato.common.wsx_client import MessageFromServer
    from zato.server.generic.api.outconn.wsx.base import OutconnWSXWrapper

# ################################################################################################################################
# ################################################################################################################################

logger = getLogger(__name__)

# ################################################################################################################################
# ################################################################################################################################

class WSXCtx:
    """ Details of a message received from a WebSocket outgoing connection.
    """
    type = None

    def __init__(self, config:'stranydict', conn:'OutconnWSXWrapper') -> 'None':
        self.config = config
        self.conn = conn

# ################################################################################################################################
# ################################################################################################################################

class Connected(WSXCtx):
    type = WEB_SOCKET.OUT_MSG_TYPE.CONNECT

# ################################################################################################################################
# ################################################################################################################################

class OnMessage(WSXCtx):
    type = WEB_SOCKET.OUT_MSG_TYPE.MESSAGE

    def __init__(self, data:'MessageFromServer', *args:'any_', **kwargs:'any_') -> 'None':
        self.data = data
        super(OnMessage, self).__init__(*args, **kwargs)

# ################################################################################################################################
# ################################################################################################################################

class Close(WSXCtx):
    type = WEB_SOCKET.OUT_MSG_TYPE.CLOSE

    def __init__(self, code:'int', reason:'strnone'=None, *args:'any_', **kwargs:'any_') -> 'None':
        self.code = code
        self.reason = reason
        super(Close, self).__init__(*args, **kwargs)

# ################################################################################################################################
# ################################################################################################################################

class _BaseWSXClient:
    def __init__(
        self,
        config:'stranydict',
        on_connected_cb:'callable_',
        on_message_cb:'callable_',
        on_close_cb:'callable_',
        *ignored_args:'any_',
        **ignored_kwargs:'any_'
    ) -> 'None':
        self.config = config
        self.on_connected_cb = on_connected_cb
        self.on_message_cb = on_message_cb
        self.on_close_cb = on_close_cb

# ################################################################################################################################

    def opened(self) -> 'None':
        self.on_connected_cb(self)

# ################################################################################################################################

    def received_message(self, msg:'MessageFromServer') -> 'None':
        self.on_message_cb(msg.data)

# ################################################################################################################################

    def closed(self, code:'int', reason:'strnone'=None) -> 'None':
        self.on_close_cb(code, reason)

# ################################################################################################################################
# ################################################################################################################################

# For flake8
_BaseWSXClient = _BaseWSXClient # type: ignore

# ################################################################################################################################
# ################################################################################################################################