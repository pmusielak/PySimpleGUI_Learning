import PySimpleGUI as sg

layout = [
    [sg.Text('Text', enable_events=True, key='-Text-'), sg.Spin(['item 1', 'item 2'])],
    [sg.Button('Button', key='-Button1-')],
    [sg.Input(key='-INPUT-')],
    [sg.Text('Text'), sg.Button('Test Button', key='-Button2-')]
]

window = sg.Window('Converter', layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '-Button1-':
        print(value['-INPUT-'])
    if event == '-Button2-':
        window['-Text-'].update(value['-INPUT-'])
    if event=='-Text-':
            print("text was pressed")
window.close()