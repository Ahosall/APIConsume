# By Feh's
import json
import PySimpleGUI as sg

import src.utils as utils
from src.layouts import Layouts

layouts = Layouts('APIConsume-PY V1.0')

HomePage = layouts.Home()

def main():
  while True:
    window, event, values = sg.read_all_windows()
    
    if event is None or event is sg.WIN_CLOSED:
      break

    if window == HomePage:
       if event == 'btnSend':
          method, url, data, dtType = values['cbMethod'], values['inURL'], values['mlData'], values['cbType']
          if method == '' or url == '':
             ErrorPage = layouts.Error('Method or URL cannot be empty!')
          else:
            res = utils.request(method, url, (dtType, data))
            if res == None:
               ErrorPage = layouts.Error('Host or connection error.!')
            else:
               if res.status_code == 200 or res.status_code == 201:
                  ResponsePage = layouts.Response(json.dumps(res.json(), indent=4))
               else:
                  ResponsePage = layouts.Response(res.text)
               HomePage.hide()
          
    if 'ErrorPage' in locals() and window == ErrorPage:
       if event == 'btnOk':
          ErrorPage.close()

    if 'ResponsePage' in locals() and window == ResponsePage:
       if event == 'btnBack':
          HomePage.un_hide()
          ResponsePage.close()
       


if __name__ == '__main__':
    main()
