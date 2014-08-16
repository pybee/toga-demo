#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import
'''
This is the main entry point for the Toga Demo.
'''
import os
import toga


class DemoApp(toga.App):

    def startup(self):
        left_container = toga.OptionContainer()

        left_table = toga.Table(['Hello', 'World'])

        left_table.insert(None, 'root1', 'value1')
        left_table.insert(None, 'root2', 'value2')
        left_table.insert(None, 'root3', 'value3')
        left_table.insert(1, 'root4', 'value4')

        left_tree = toga.Tree(['Navigate'])

        left_tree.insert(None, None, 'root1')

        root2 = left_tree.insert(None, None, 'root2')

        left_tree.insert(root2, None, 'root2.1')
        root2_2 = left_tree.insert(root2, None, 'root2.2')

        left_tree.insert(root2_2, None, 'root2.2.1')
        left_tree.insert(root2_2, None, 'root2.2.2')
        left_tree.insert(root2_2, None, 'root2.2.3')

        left_container.add('Table', left_table)
        left_container.add('Tree', left_tree)

        right_content = toga.Container()
        buttons = [
            toga.Button('Hello world %s' % b, on_press=self.button_handler)
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

        cmd1 = toga.Command(self.action1, 'Action 1', tooltip='Perform action 1', icon=os.path.join(os.path.dirname(__file__), 'icons/brutus-32.png'))
        cmd2 = toga.Command(self.action2, 'Action 2', tooltip='Perform action 2', icon=toga.TIBERIUS_ICON)

        self.main_window.toolbar = [cmd1, toga.SEPARATOR, cmd2]

        self.main_window.content = split


    def button_handler(self, widget):
        print("button press")
        for i in range(0, 10):
            yield 1
            print ('still running... (iteration %s)' % i)

    def action1(self, widget):
        toga.Dialog.info('Toga', 'THIS! IS! TOGA!!')

    def action2(self, widget):
        if toga.Dialog.question('Toga', 'Is this cool or what?'):
            toga.Dialog.info('Happiness', 'I know, right! :-)')
        else:
            toga.Dialog.info('Shucks...', "Well aren't you a spoilsport... :-(")


def main():

    app = DemoApp('Toga Demo', 'org.pybee.toga-demo')

    app.main_loop()


if __name__ == '__main__':
    main()