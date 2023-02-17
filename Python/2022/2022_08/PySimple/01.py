"""
    The Official Python GUI Programming with PySimpleGUI Course
    Lesson 1

    http://www.PySimpleGUI.org
"""

# 1 - Import
import PySimpleGUI as sg

# 2 - Layout
layout = [
            [sg.Text('Hello, World!')],
            [sg.Button('Ok')],
         ]

# 3 - Window
window = sg.Window('Title', layout)

# 4 - Event loop / handling
event, values = window.read()

# 5 - Close
window.close()
