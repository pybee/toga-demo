#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import
'''
This is the main entry point for the Toga Demo.
'''
from .app import TogaDemo


def main():
    app = TogaDemo('Toga Demo', 'org.pybee.toga-demo')
    app.main_loop()


main()
