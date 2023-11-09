# By Feh's
import json

from requests import get, post, put, delete, ConnectionError

def request(method, url, data = False):
  switch = {
    'GET': get,
    'POST': post,
    'PUT': put,
    'DELETE': delete 
  }
  print(data)
  meth = switch[method]
  try:
    if data != False and method in ['POST', 'PUT']:
      body = data[1]
      if data[0] == 'JSON':
        return meth(url, json.loads(body))
      return meth(url, body)
    return meth(url)
  except ConnectionError:
    return 500
