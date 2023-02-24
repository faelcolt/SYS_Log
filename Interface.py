from PySimpleGUI import PySimpleGUI as sg 

# Layouts
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o Login?')]
    [sg.Button('Entrar')]
]
# Windows

# Events

