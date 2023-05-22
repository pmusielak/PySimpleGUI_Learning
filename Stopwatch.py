import PySimpleGUI as sg
sg.theme('black')
layout = [
    [sg.Push(),sg.Image('./images/cross1.png', enable_events=True, key='-CLOSE-')],
    [sg.VPush()],
    [sg.Text('time')],
    [sg.Button('Start'), sg.Button('lap')],
    [sg.VPush()]
]

window = sg.Window('Stopwatch', layout, 
                   size=(300,300), 
                   no_titlebar=True,
                   element_justification='center')

while True:
    event, values = window.read()
    if event == (sg.WIN_CLOSED or '-CLOSE-'):
        break
window.close()