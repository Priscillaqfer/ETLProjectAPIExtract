import requests
import json



url = 'https://api.openai.com/v1/chat/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'k-proj-gHorKAQk8TxGfcgeWa32HFeSoJHw5hhacfNngfgUebNtE90aHc8E6okxUPIW6KjMzBrfyXsP97T3BlbkFJFM51HsesiiGknosvHd3sR8FnqBuxxYh2f3RTiPo9SvT-bcOnAJkqreQQPqAPBmkDssgwjy6iEA'
}
data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {'role': 'user', 'content': 'Qual a capital da FRança?'}
    ]
}

resposta = requests.post(url, headers=headers, data=json.dumps(data))

print(resposta.json())



