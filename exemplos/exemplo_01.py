import requests

url = 'https://www.google.com/'

resposta = requests.post(url)

print(resposta)