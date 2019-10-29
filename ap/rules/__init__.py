# -*- coding: utf-8 -*-

"""
AP Rules Engine

A simple rules engine, written in python.

Basic Usage:
    TODO: Add Usage

:copyright: (c) 2019 Anna Poulakos
:license: MIT, see LICENSE for more details.
"""


from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __author__, __author_email__, __license__
from .__version__ import __copyright__, __cake__

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
