#!/usr/bin/env python
#
# License: BSD
#   https://raw.githubusercontent.com/splintered-reality/py_trees/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Syntax highlighting hints for core py_tree types/enums.

.. module:: syntax_highlighting
   :synopsis: Syntax highlighting for various py_trees objects

Oh my spaghettified magnificence,
Bless my noggin with a tickle from your noodly appendages!
"""

##############################################################################
# Imports
##############################################################################

from . import common
from . import console

##############################################################################
# Syntax Highlighting
##############################################################################


_status_colour_strings = {common.Status.SUCCESS: console.green + str(common.Status.SUCCESS) + console.reset,
                          common.Status.RUNNING: console.blue + str(common.Status.RUNNING) + console.reset,
                          common.Status.FAILURE: console.red + str(common.Status.FAILURE) + console.reset,
                          common.Status.INVALID: console.yellow + str(common.Status.INVALID) + console.reset
                          }

_status_colour_codes = {common.Status.SUCCESS: console.green,
                        common.Status.RUNNING: console.cyan,
                        common.Status.FAILURE: console.red,
                        common.Status.INVALID: console.yellow
                        }


def status(status):
    """
    Retrieve a coloured string representing a :py:class:`~py_trees.common.Status`.

    This is used for syntax highlighting in various modes.

    :param :py:class:`~py_trees.common.Status` Status: behaviour status
    :returns: syntax highlighted string representation of the status
    """
    return _status_colour_strings[status]


def status_colour_code(status):
    """
    Retrieve the colour code associated with a :py:class:`~py_trees.common.Status`.

    This is used for syntax highlighting in various modes.

    :param :py:class:`~py_trees.common.Status` Status: behaviour status
    :returns: console colour code associated with the status
    """
    return _status_colour_codes[status]
