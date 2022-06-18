import requests 

content = {
    'from_fio': 'diyar',
    'to_fio': 'dd',
    'phone': '8766',
    'email': 'djars500@gmaik.com',
    'iin': '423423',
    'content': 'dsds'
}

data = requests.post('http://127.0.0.1:8000/api/message/', content)

print(data.text)