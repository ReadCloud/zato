# -*- coding: utf-8 -*-

"""
Copyright (C) 2021, Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# stdlib
from dataclasses import dataclass

# Zato
from zato.common.marshal_.api import Model
from zato.common.typing_ import strnone

# ################################################################################################################################
# ################################################################################################################################

if 0:
    from zato.sso.common import BaseRequestCtx

# ################################################################################################################################
# ################################################################################################################################

@dataclass(init=False)
class RequestCtx(Model):
    cid:         'str'
    current_ust: 'strnone'
    current_app: 'strnone'
    remote_addr: 'strnone'
    user_agent:  'strnone'

    @staticmethod
    def from_ctx(ctx:'BaseRequestCtx') -> 'RequestCtx':
        req_ctx = RequestCtx()
        req_ctx.cid = ctx.cid
        req_ctx.remote_addr = ctx.remote_addr
        req_ctx.user_agent = ctx.user_agent

        return req_ctx

# ################################################################################################################################
# ################################################################################################################################