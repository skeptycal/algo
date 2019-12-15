#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Creating C Extensions for Python """
# pylint: disable=missing-docstring,superfluous-parens
# Ref: https://medium.com/practo-engineering/execute-python-code-at-the-speed-of-c-extending-python-93e081b53f04

from distutils.core import setup, Extension
MOD = "benchmark"
setup(name=MOD, ext_modules=[Extension(MOD, sources=['benchmark.c'])],
      description="My C Extension Module")
