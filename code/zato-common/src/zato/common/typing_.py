# -*- coding: utf-8 -*-

"""
Copyright (C) 2021, Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# ################################################################################################################################
# ################################################################################################################################

# stdlib
from typing import           \
    Any as any_,             \
    Callable as callable_,   \
    cast as cast_,           \
    Dict as dict_,           \
    Generator as generator_, \
    NoReturn as noreturn,    \
    List as list_,           \
    Optional as optional,    \
    Text as str_,            \
    Tuple as tuple_,         \
    TypeVar as typevar_,     \
    Set as set_,             \
    Union as union_

# dacite
from dacite import from_dict

# Be explicit about which import error we want to catch
try:
    import dataclasses # noqa: F401

# Python 3.6
except ImportError:
    from zato.common.ext.dataclasses import * # noqa: F401

# Python 3.6+
else:
    from dataclasses import * # noqa: F401

# ################################################################################################################################
# ################################################################################################################################

#
# TypedDict
#
try:
    from typing import TypedDict
    from typing import Protocol
except ImportError:
    from zato.common.ext.typing_extensions import TypedDict
    from zato.common.ext.typing_extensions import Protocol

# ################################################################################################################################
# ################################################################################################################################

# For flake8
from_dict = from_dict
optional  = optional
Protocol  = Protocol
TypedDict = TypedDict

# ################################################################################################################################
# ################################################################################################################################

def instance_from_dict(class_, data):
    # type: (object, dict) -> object
    instance = class_()
    for key, value in data.items():
        setattr(instance, key, value)
    return instance

# ################################################################################################################################
# ################################################################################################################################

anydict    = dict_[any_, any_]
anylist    = list_[any_]
anytuple   = tuple_[any_, ...]
callable_  = callable_
cast_      = cast_
dictlist   = list_[anydict]
generator_ = generator_
intlist    = list_[int]
intnone    = optional[int]
noreturn   = noreturn
set_       = set_
strint     = union_[str_, int]
strintnone = union_[optional[str_], optional[int]]
strintbool = union_[str_, int, bool]
strnone    = optional[str]
strlist    = list_[str]
stranydict = dict_[str, any_]
strintdict = dict_[str, strint]
intdict    = dict_[int, int]
strtuple   = tuple_[str]
tuple_     = tuple_
typevar_   = typevar_
union_     = union_
