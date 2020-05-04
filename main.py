Feitoimport copy
import requests
import hashlib
import json

alfabeto = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7:  'g',  8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
            13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
            24: 'x', 25: 'y', 26: 'z'}

def receber_json():

    url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=6d14c431391b31ffb842b8df79699ee0d2b84b5f'

    x = requests.get(url)
    y = x.json()
    desafio = copy.deepcopy(x.json())
    escrever_json(y)
    cifrado = desafio['cifrado']
    casas = desafio['numero_casas']
    return cifrado, casas

def escrever_json(recebido):
    with open('answer.json', 'w') as answer:
        json.dump(recebido, answer)

def ler_json(arquivo):
    with open('answer.json', 'r+') as answer:
        return json.load(answer)

def chaves(letra):
    for k, v in alfabeto.items():
        if v == letra:
            return k
        elif letra == ' ':
            return ' '
        elif letra == '.':
            return '.'

def chave_letra(resposta, casas):
    traducao = list()
    for n in resposta:
        if n == ' ':
            traducao.append(' ')
        elif n == '.':
            traducao.append('.')
        else:
            if (n - casas) < 0:
                traducao.append(alfabeto[26 - abs(n-casas)])
            else:
                traducao.append(alfabeto[n - casas])
    traducao = ''.join(traducao)
    return traducao

def decodificador():
    cifrado, casas = receber_json()
    resposta = list()
    for l in cifrado:
        resposta.append(chaves(l))
    traducao = chave_letra(resposta, casas)
    return traducao

def criar_sha1(traducao):
    sha1 = hashlib.sha1(traducao.encode('utf-8')).hexdigest()
    return sha1

def update_json(traducao, sha1):
    arq = ler_json('answer.json')
    arq['decifrado'] = traducao
    arq['resumo_criptografico'] = sha1
    escrever_json(arq)

def enviar_json():
    url_envio = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=6d14c431391b31ffb842b8df79699ee0d2b84b5f'
    response = requests.post(url_envio, files=dict(answer=open('answer.json', 'rb')))
    return response.json()

def principal():
    traducao = decodificador()
    sha1 = criar_sha1(traducao)
    update_json(traducao, sha1)
    response = enviar_json()
    return 'done'

print(principal())

