import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
s = r.status_code
print(s)
r.status_code
#200
print('this is headers')
r.headers['content-type']
#'application/json; charset=utf8'
print('this is encoding')
r.encoding
#'utf-8'
print('this is text value')
r.text
#u'{"type":"User"...'
print('this is json value')
r.json()
#{u'private_gists': 419, u'total_private_repos': 77, ...}