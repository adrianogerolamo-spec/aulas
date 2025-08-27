#bibliotecas
import os

""" lista_arquivos = os.listdir() #lista os arquivos no diretorio
print(lista_arquivos) """

#pra instalar a biblioteca no python:
#toggle panel -> seta pra baixo no terminal -> command prompt -> pip install (nome da biblioteca)
#SO INSTALA UMA VEZ NA VIDA, POIS FOI PELO PROMPT, TA NO PROPRIO PYTHON

import requests #rquisita arquivos da net

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link)
dic_resposta = resposta.json() #transforma a resposta da net q esta no formato .json num dicionario

#print(dic_resposta)
cotacao_dolar = dic_resposta["USDBRL"] #a chave (key) do dicionario
print(cotacao_dolar["bid"])