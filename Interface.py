from PySimpleGUI import PySimpleGUI as sg 

# Layouts
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]
# Windows
janela = sg.Window('Tela de Login', layout)

# Events
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'meuNome' and valores['senha'] == '12345':
            print('Login efetuado com sucesso! ')
