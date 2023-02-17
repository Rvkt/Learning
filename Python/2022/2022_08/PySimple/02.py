import PySimpleGUI as sg
# import PySimpleGUIQt as sg
# import PySimpleGUIWx as sg
# import PySimpleGUIWeb as sg


def main():

    layout = [[sg.text('My Window')]],
    [sg.Input(key='-IN-')],
    [sg.text(size=(30, 1), key='-OUT-')],
    [sg.Button('Go'), sg.Button('Exit')]

    window = sg.Window('Window Title', layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        window['-OUT-'].update(f'You clicked {event}')

    window.close()  