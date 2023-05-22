import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Franklin 14', button_element_size= (6,3))
    button_size=(6,3)
    layout = [
        [sg.Text('0', key='-TEXT-', font='Franklin 26', expand_x=True, justification='right', pad=(10, 20), right_click_menu=theme_menu)],
        [sg.Button('C', key='-CLEAR-', expand_x=True), sg.Button('÷', key='/', expand_x=True)],
        [sg.Button('7', size=button_size), sg.Button('8', size=button_size), sg.Button('9', size=button_size), sg.Button('X', key='*', size=button_size)],
        [sg.Button('4', size=button_size), sg.Button('5', size=button_size), sg.Button('6', size=button_size), sg.Button('-', key='-', size=button_size)],
        [sg.Button('1', size=button_size), sg.Button('2', size=button_size), sg.Button('3', size=button_size), sg.Button('+', key='+', size=button_size)],
        [sg.Button('0', expand_x=True), sg.Button('.', size=button_size), sg.Button('=', key='-ENTER-', size=button_size)]
            ]
    return sg.Window('Calculator', layout)

theme_menu=['menu',['LightGrey1', 'dark', 'DarkGrey8', 'random']]
window = create_window('LightGrey1')
current_number=[]
equation=[]

while True:
    event, values = window.read()
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_number.append(event)
        num_string = ''.join(current_number)
        window['-TEXT-'].update(num_string)
        con=False
    if event in ['+','-','*','/']:
        if con==False:
            current_number.append(event)
            equation.append(''.join(current_number))
            current_number=[]
            window['-TEXT-'].update('0')
        if con:
            current_number.append(str(result))
            current_number.append(event)
            equation.append(''.join(current_number))
            current_number=[]
            window['-TEXT-'].update('0')
    if event==('-ENTER-'):
        equation.append(''.join(current_number))
        result=eval(''.join(equation))
        current_number=[]
        equation=[]
        con=True
        window['-TEXT-'].update(result)
    if event=='-CLEAR-':
        current_number=[]
        window['-TEXT-'].update('0')
    if event == sg.WIN_CLOSED:
        break

window.close()