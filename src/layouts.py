# By Feh's
import PySimpleGUI as sg

sg.theme('Dark Grey 11')

class Layouts:
  def __init__(self, title):
    self.title = title

  def Home(self):
    methods = [
      'GET',
      'POST',
      'PUT',
      'DELETE',
    ]

    types = [
      'JSON',
      'FORM-DATA',
      'FORM-URLENCODED'
    ]

    layout = [
      [sg.Text(self.title, font='Any 20', key='lblTitle')],

      [sg.Combo(methods, default_value=methods[0], key='cbMethod'), sg.Input(key='inURL')],
      
      [sg.Text('Data', key='lblResponseData')],
      [sg.Multiline(expand_x=True, size=(30, 10), key='mlData')],
      [sg.Combo(types, default_value=types[0], key='cbType'), sg.Button('SEND', key="btnSend")]
    ]

    return sg.Window(f'{self.title} - Home', layout, finalize=True)

  def Response(self, data):
    layout = [
      [sg.Text("Response", font='Any 20', key='lblTitle')],

      [sg.Multiline(default_text=data, disabled=True, size=(120, 30), key='mlData')],
      [sg.Button('BACK', key="btnBack")]
    ]

    return sg.Window(f'{self.title} - Response', layout, finalize=True, disable_close=True, no_titlebar=True)
  
  def Error(self, message):
    layout = [
      [sg.Text("⚠️ | Error", font='Any 20', key='lblTitle')],

      [sg.Text(message, key='lblMessage')],
      [sg.Button('OK', key='btnOk')],
    ]

    return sg.Window(f'{self.title} - Error: {message}', layout, size=(270, 120), finalize=True, disable_close=True, no_titlebar=True)