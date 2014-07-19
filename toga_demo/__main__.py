#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import
'''
This is the main entry point for the Toga Demo.
'''
import os

import toga


def button_handler(widget):
    print("button press")


def action1():
    print("action 1")


def action2():
    print("action 2")


def main():
    app = toga.App('Toga Demo', 'org.pybee.toga-demo')

    left_container = toga.Table(['Hello', 'World'])

    left_container.insert(None, 'root1', 'value1')
    left_container.insert(None, 'root2', 'value2')
    left_container.insert(None, 'root3', 'value3')
    left_container.insert(1, 'root4', 'value4')

    right_content = toga.Container()
    buttons = [
        toga.Button('Hello world %s' % b, on_press=button_handler)
        for b in range(0, 10)
    ]

    for i, button in enumerate(buttons):
        right_content.add(button)

        if i == 0:
            right_content.constrain(button.TOP == right_content.TOP + 50)
        else:
            right_content.constrain(button.TOP == buttons[i-1].BOTTOM + 50)
        right_content.constrain(button.LEADING == right_content.LEADING + 50)
        right_content.constrain(button.TRAILING + 50 == right_content.TRAILING)

    right_content.constrain(buttons[-1].BOTTOM + 50 < right_content.BOTTOM)

    right_container = toga.ScrollContainer()

    right_container.content = right_content

    split = toga.SplitContainer()

    split.content = [left_container, right_container]

    app.main_window.content = split

    cmd1 = toga.Command(action1, 'Action 1', tooltip='Perform action 1', icon=os.path.join(os.path.dirname(__file__), 'icons/brutus-72.png'))
    cmd2 = toga.Command(action2, 'Action 2', tooltip='Perform action 2', icon=toga.TIBERIUS_ICON)

    app.main_window.toolbar = [cmd1, toga.SEPARATOR, cmd2]

    app.main_loop()


if __name__ == '__main__':
    main()