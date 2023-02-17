import PySimpleGUI as sg                            # Part 1 - The import

# Define the window's contents
layout = [  [sg.Text("What's your name?")],         # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('Window Title', layout)          # Part 3 - Window Define
                                                
# Display and interact with the Window
event, values = window.read()                       # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0],"!\n\tThanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()                                      # Part 5 - Close the Window