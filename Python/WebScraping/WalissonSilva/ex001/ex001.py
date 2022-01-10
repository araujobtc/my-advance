# requests

import requests

response = requests.get('http://www.walissonsilva.com/')

print('status code: ', response.status_code)
print('headers: ', response.headers)
print('content:\n', response.content)
