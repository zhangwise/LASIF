#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project specific function for modifying synthetics on the fly.

:copyright:
    Lion Krischer (krischer@geophysik.uni-muenchen.de), 2015
:license:
    GNU General Public License, Version 3
    (http://www.gnu.org/copyleft/gpl.html)
"""


def process_synthetics(st, iteration):  # NOQA
    """
    This function is called after a synthetic file has been read.

    Do whatever you need to do in here an return a potentially modified
    stream object. Make sure that anything you do works with the
    preprocessing function. LASIF expects data and synthetics to have
    exactly the same length before it can pick windows and calculate adjoint
    sources.

    Potential uses for this function are to shift synthetics in time if
    required or to apply some processing to them which LASIF by default does
    not do.

    Please note that you also got the iteration object here, so if you
    want some parameters to change depending on the iteration, just use
    if/else on the iteration objects.

    >>> iteration.name  # doctest: +SKIP
    '11'
    >>> iteration.get_process_params()  # doctest: +SKIP
    {'dt': 0.75,
     'highpass': 0.01,
     'lowpass': 0.02,
     'npts': 500}

    Use ``$ lasif shell`` to play around and figure out what the iteration
    objects can do.
    """
    # Currently a no-op.
    return st
