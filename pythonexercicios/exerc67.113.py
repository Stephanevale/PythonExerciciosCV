import requests
try:
    site = "http://www.pudim.com.br/"
    requests.get(site)
except requests.exceptions.ConnectionError:
    print('O site pudim não está acessível')
else:
    print('O site pudim está acessível')