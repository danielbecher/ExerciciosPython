# ExtrairEmails.py é uma ferramenta que extrai do JSON exportado da tabela wp_comments de um site/blog em WordPress
#todos os endereços de e-mail com formato válido e salva num arquivo .txt.

# IMPORTANTE!!! o arquivo .json precisa estar no mesmo diretório do programa, bem como o arquivo emails.txt será
#gerado neste mesmo local.

#Importação das bibliotecas que uso nesta aplicação
import json
import os
import re

#Aqui inserimos numa variável as strings verificadoras para o formato de e-mail (REGEX)
regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

#Listas e dicionários usados para exploração das informações
dados = {}
emails = []

#Variável de controle para o loop
controle = 0

#Esta função checa se o e-mail tem formato válido
def checaEmail(email):
    if (re.search(regex, email)):
        return True

#Esta função faz a contabilização de quantos e-mails foram extraídos da base de dados e salvos no arquivo .txt
def contaEmail():
    with open('emails.txt') as arqEmails:
        return sum(1 for line in arqEmails)

#Esta função exporta no arquivo .txt os endereços válidos após fazer as devidas checagens.
def exportatxt(f):
    if checaEmail (f) == True:
        arquivotxt = open('emails.txt', 'a')
        arquivotxt.write(f)
        arquivotxt.write("\n")
        arquivotxt.close()

#Aqui está o motor que lerá o arquivo .json e fará a exportação dos endereços válidos
with open("wp_comments.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)
    for i in dados:
        emails.append(dados[controle]['comment_author_email'])
        endereco = dados[controle]['comment_author_email']
        exportatxt(endereco)
        controle += 1
    contarenderecos = contaEmail()
    print('Foram extraídos {} endereços de e-mail deste arquivo!'.format(contarenderecos))