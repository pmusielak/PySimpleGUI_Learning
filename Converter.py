import PySimpleGUI as sg

layout = [
    [sg.Input(key='-INPUT-'), sg.Spin(['km to mile', 'kg to lb'], key='-UNITS-')],
    [sg.Button('Convert', key='-CONVERTER-')],
    [sg.Text(key='-RESULT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break
    if(value['-INPUT-'].isnumeric()):
        if event == '-CONVERTER-':
            match(value['-UNITS-']):
                case 'km to mile':
                    window['-RESULT-'].update(round(float(value['-INPUT-'])*0.6214, 2))
                case 'kg to lb':
                    window['-RESULT-'].update(round(float(value['-INPUT-'])*2.20462, 2))
    else:
        window['-RESULT-'].update('Given value must be numeric')

window.close()