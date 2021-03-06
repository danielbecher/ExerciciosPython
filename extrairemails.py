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
    for i in email:
        if (re.search(regex, email)):
            return True

#Esta função faz a contabilização de quantos e-mails foram extraídos da base de dados e salvos no arquivo .txt
def contaEmail():
    with open('emails.txt') as arqEmails:
        return sum(1 for line in arqEmails)

#Esta função faz a contabilização de quantos comentários existem no arquivo .json
def contaComentario():
    with open('wp_comments.json', encoding="utf8") as arqComentarios:
        return sum(1 for line in arqComentarios)

#Esta função exporta no arquivo .txt os endereços válidos após fazer as devidas checagens.
def exportatxt(listaemails):
    for i in listaemails:
        if checaEmail(i) == True:
            arquivotxt = open('emails.txt', 'a')
            arquivotxt.write(i)
            arquivotxt.write("\n")
            arquivotxt.close()

#Esta função verifica se existem e-mails duplicados na lista evitando falsos-positivos.
def verificaDup(endereco):
    listalimpa = []
    listasuja = []
    for i in endereco:
        if i not in listalimpa:
            listalimpa.append(i)
        else:
            listasuja.append(i)
    return listalimpa

#Aqui está o motor que lerá o arquivo .json e fará a exportação dos endereços válidos
with open("wp_comments.json", encoding='utf-8') as meu_json:
    print("*"*40)
    print("*** Iniciando a leitura do JSON ***")
    dados = json.load(meu_json)
    print("*" * 40)
    print("*** Verificando endereços válidos ***")
    print("*" * 40)
    print("*** Exportando e-mails ***")
    for i in dados:
        emails.append(dados[controle]['comment_author_email'])
        endereco = dados[controle]['comment_author_email']
        controle += 1
    emailslimpos = verificaDup(emails)
    exportatxt(emailslimpos)
    contarenderecos = contaEmail()
    contarcomentarios = contaComentario()
    print("*" * 40)
    print('A tabela do banco de dados possui {} comentários.'.format(contarcomentarios))
    print('Destes comentários, {} são endereços de e-mail válidos e foram exportados'.format(contarenderecos))
    print("*" * 40)