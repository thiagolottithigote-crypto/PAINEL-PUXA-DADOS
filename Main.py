## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

import os
import requests

error = f'{Twhite}[{Ired}ERROR{Twhite}]';
warning = f'{Twhite}[{Nyellow}!{Twhite}]';
info = f'{Twhite}[{Dgreen}i{Twhite}]'
result = os.popen('figlet MID-PAINEL').read()

os.system('clear')

print(f'Painel de Consultas básicas by Dr Midnight')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)
import os, sys, time, json, subprocess, platform

try:
    import requests, random, json, phonenumbers
except:
    install = input(
        f'{Twhite}{Dgreen}[i]{Twhite} Ola! Vejo que esta é sua primeira vez aqui...'
        f'\nDeseja instalar o software necessário?\n1-Sim\n2-Não\n_').strip().upper()[0]
    if install == 'S' or install == '1':
        os.system("apt install figlet -y")
        os.system('python3 -m pip install --upgrade pip')
        os.system('pip3 install requests pytube phonenumbers netifaces')
        clear()
    else:
        print(f'Ok... Tente realizar a instalação manual ou Adeus');
        exit()
    restart()

try:
    from database import cep, covid19, ip, placa, banner, root, meuip, cnpj, nome, cpf
except Exception as error:
    print(f'{Twhite}{Ired}[*]{Twhite} Erro: ' + error)
    exit()

def dialog(text='', tiled='='):
    clear();
    print(os.popen('figlet MID-PAINEL').read())
    text = text.split('\n')
    maior = 0
    for txt in text:
        tamanho = len(txt)
        if tamanho > maior:
            maior = tamanho
    print(str(Twhite) + str(Dgreen) + tiled + tiled + tiled * maior + tiled + tiled + str(Twhite))
    for txt in text:
        print(str(warning) + ' ' + txt)
    print(str(Twhite) + str(Dgreen) + tiled + tiled + tiled * maior + tiled + tiled + str(Twhite))
    time.sleep(3)

def error_dialog(text='', tiled='='):
    clear();
    print(os.popen('figlet MID-PAINEL').read())
    text = text.split('\n')
    maior = 0
    for txt in text:
        tamanho = len(txt)
        if tamanho > maior:
            maior = tamanho
    print(str(Twhite) + str(Ired) + tiled * 8 + tiled * maior + tiled * 8 + str(Twhite))
    for txt in text:
        print(str(error) + ' ' + txt + ' ' + str(error))
    print(str(Twhite) + str(Ired) + tiled * 8 + tiled * maior + tiled * 8 + str(Twhite))
    time.sleep(3)

requests = requests.Session();result = os.popen('figlet MID-PAINEL').read()

try:
    if __name__ == '__main__':
        dialog('Buscando atualizações ...')
        update = subprocess.check_output('git pull', shell=True)
        if 'Already up to date' not in update.decode():
            dialog('Atualização instalada.\nReiniciando o painel.')
            restart()
        else:
            print(f'{Twhite}[{Nyellow}i{Twhite}] Nenhuma atualização disponivel.')
            time.sleep(2)
except:
    if os.path.exists('.git'):
        pass
    else:
        error_dialog('Falta de repositório GIT local')

try:
    subprocess.check_output('apt update -y', shell=True)
    os.system("apt install figlet curl -y")
except:
    os.system("pacman -Sy figlet curl")

Sair = False
while Sair == False:
    try:
        banner.menu()
        opc = int(input(f'{Dgreen}Digite o numero da opção que deseja: \n>>> '))
    except:
        error_dialog('Caracteres não reconhecidos');
        op = None
    clear()

    if opc == 1:     # NOME
        nome.consultar()
    if opc == 2:   # CPF
        cpf.consultar()
    elif opc == 3:   # CEP
        cep.consultar()
    elif opc == 4:   # Placa
        placa.consultar()
    elif opc == 5:   # CNPJ
        cnpj.consultar()
    elif opc == 6:   # IP
        ip.consultar()
    elif opc == 7:   # Meu IP
        meuip.consultar()
    elif opc == 8:   # Covid Info
        covid19.consultar()
    elif opc == 9:   # Root Checker
        root.consultar()
    elif opc == 10:   # Atualizar painel
        os.popen('cd database && bash update.sh');
        dialog('Reiniciando o painel...');
        restart()
    elif opc == 11:  # Sair
        Sair = True
    elif opc == 12:  # Criador
        os.system('termux-open-url https://wa.me/5512988789266')
    elif opc == 13:  # Grupo
        os.system('termux-open-url https://discord.gg/kgXhZzGJDY')
    elif opc == None:
        pass
    else:
        error_dialog('Opção incorreta')


## ==================== ARQUIVO banner.py ====================

## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

def menu():
    clear()
    print(fr'''{Ired}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                  ┃
┃   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n  ┃
┃    {Gpurple} /\\,/\\,     |\         -__ /\\                       ,,     {Ired}┃
┃    {Gpurple}/| || ||   '   \\          ||  \\   _    '             ||     {Ired}┃
┃    {Gpurple}|| || ||  \\  / \\        /||__||  < \, \\ \\/\\  _-_  ||     {Ired}┃
┃    {Gpurple}||=|= ||  || || ||        \||__||  /-|| || || || || \\ ||     {Ired}┃
┃   {Gpurple}~|| || ||  || || ||         ||  |, (( || || || || ||/   ||     {Ired}┃
┃    {Gpurple}|, \\,\\, \\  \\/        _-||-_/   \/\\ \\ \\ \\ \\,/  \\ {Hcyan}2.0{Ired} ┃
┃   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n  ┃
┃                                                                  ┃
┗  ┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓  ┛
   ┃    {Nyellow}[{Dgreen} CONSULTAS {Nyellow}]{Ired}    ┃   {Nyellow}[{Iblue} FERRAMENTAS {Nyellow}]{Ired}   ┃   {Nyellow}[{Twhite} OPÇÕES {Nyellow}]{Ired}   ┃
   ┃                     ┃                     ┃                ┃
   ┣┫{Nyellow}[01]{Dgreen} Consulta Nome{Ired}  ┣┫{Nyellow}[07]{Iblue} Meu IP{Ired}         ┣┫{Nyellow}[10]{Twhite} Atualizar{Ired} ┃
   ┃                     ┃                     ┃                ┃
   ┣┫{Nyellow}[02]{Dgreen} Consulta CPF{Ired}   ┣┫{Nyellow}[08]{Iblue} Covid Info{Ired}     ┣┫{Nyellow}[11]{Twhite} Sair{Ired}      ┃
   ┃                     ┃                     ┃                ┃
   ┣┫{Nyellow}[03]{Dgreen} Consulta CEP{Ired}   ┣┫{Nyellow}[09]{Iblue} Root Checker{Ired}   ┣┫{Nyellow}[12]{Twhite} Criador{Ired}   ┃
   ┃                     ┃                     ┃                ┃
   ┣┫{Nyellow}[04]{Dgreen} Consulta Placa{Ired} ┣┫                    ┣┫{Nyellow}[13]{Twhite} Grupo{Ired}     ┃
   ┃                     ┃                     ┃                ┃
   ┣┫{Nyellow}[05]{Dgreen} Consulta CNPJ{Ired}  ┣┫                    ┣┫               ┃
   ┃                     ┃                     ┃                ┃
   ┣┫{Nyellow}[06]{Dgreen} Consulta IP{Ired}    ┣┫                    ┣┫               ┃
   ┗━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━┛+

┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')


## ==================== cep.py ====================

## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

import os
import requests

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

def consultar():
    clear()
    print('')
    print(f'\n{Iblue}########## #################### ##########')
    print('########## ### Consulta CEP ### ##########')
    print('########## #################### ##########')
    restart = 'S'
    while restart == 'S':
        while True:
            cep_input = input(f'\n{Hcyan}Digite o CEP para consulta: ').strip()
            if len(cep_input) != 8:
                print(f'{Ired}!!! {Nyellow}CEP Inválido {Ired}!!!')
            else:
                break
        request = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')
        rjson = request.json()
        if 'erro' in rjson:
            restart = str(input(
                f'{Ired}==> CEP NÃO ENCONTRADO <== \n\n\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[0]
            clear()
        else:
            print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> CEP ENCONTRADO <=={Nyellow} '))
            print(f'\nCEP             >>> {rjson["cep"]}')
            print(f'Logradouro      >>> {rjson["logradouro"]}')
            print(f'Complemento     >>> {rjson["complemento"]}')
            print(f'Bairro          >>> {rjson["bairro"]}')
            print(f'Cidade          >>> {rjson["localidade"]}')
            print(f'Estado          >>> {rjson["uf"]}')
            print(f'População[IBGE] >>> {rjson["ibge"]}')
            print(f'DDD             >>> {rjson["ddd"]}')
            print('')
            print(f'\033[1;33m-' * 48)
            restart = str(input(
                f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()


## ==================== cnpj.py ====================

## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

import os
import requests

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

def consultar():
    clear()
    print('')
    print(f'\n{Iblue}########## ##################### ##########')
    print('########## ### Consulta CNPJ ### ##########')
    print('########## ##################### ##########')
    restart = 'S'
    while restart == 'S':
        while True:
            cnpj_input = input(f'\n{Hcyan}Digite o CNPJ para consulta: ').strip()
            if len(cnpj_input) != 14:
                print(f'{Ired}!!! {Nyellow}CNPJ Inválido {Ired}!!!')
            else:
                break
        request = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj_input}')
        rjson = request.json()
        if 'ERROR' in rjson['status']:
            restart = str(input(
                f'{Ired}==> CNPJ NÃO ENCONTRADO <== \n\n\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[0]
            clear()
        else:
            print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> CNPJ ENCONTRADO <=={Nyellow} '))
            print('\nINFO:')
            print(f'CNPJ               >>> {rjson["cnpj"]}')
            print(f'Nome               >>> {rjson["nome"]}')
            print(f'Complemento        >>> {rjson["complemento"]}')
            print(f'Atividade Pri      >>> {rjson["atividade_principal"]}')
            print(f'Atividades Sec     >>> {rjson["atividades_secundarias"]}')
            print(f'Telefone           >>> {rjson["telefone"]}')
            print(f'Email              >>> {rjson["email"]}')

            print('\nLOCALIDADE:')
            print(f'Cep                >>> {rjson["cep"]}')
            print(f'Estado             >>> {rjson["municipio"]}{rjson["uf"]}')
            print(f'Bairro             >>> {rjson["bairro"]}')
            print(f'Logradouro         >>> {rjson["logradouro"]}{rjson["numero"]}')

            print('\nSITUAÇÃO')
            print(f'Situação           >>> {rjson["motivo_situacao"]}')
            print(f'Data Situação      >>> {rjson["data_situacao"]}')
            print(f'Situação Especial  >>> {rjson["situacao_especial"]}')
            print(f'Data               >>> {rjson["data_situacao_especial"]}')

            print('\nEXTRA')

            print(f'Última att         >>> {rjson["ultima_atualizacao"]}')
            print(f'Capital            >>> {rjson["capital_social"]}')
            print(f'Efr                >>> {rjson["efr"]}')
            print(f'Disponibilidade    >>> {rjson["billing"]}')

            print('')
            print(f'\033[1;33m-' * 48)
            restart = str(input(
                f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()


## ==================== covid19.py ====================

## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

import os
import requests

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

def consultar():
    clear()
    print('')
    print(f'\n{Iblue}########## #################### ##########')
    print('######## ### Consulta Covid19 ### ########')
    print('########## #################### ##########')
    restart = 'S'
    while restart == 'S':
        while True:
            covid_input = str(input(f'\n{Hcyan}Digite o UF para consulta (Ex: "SP"/"RJ"): ').strip().lower())
            if len(covid_input) != 2:
                print(f'{Ired}!!! {Nyellow}UF Inválido {Ired}!!!')
            else:
                break
        request = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{covid_input}')
        rjson = request.json()
        if 'error' in rjson:
            restart = str(input(
                f'{Ired}==> REGIÃO NÃO ENCONTRADA <== \n\n\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
        else:
            print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> REGIÃO ENCONTRADA <=={Nyellow} '))
            print(f'\nEstado(UF)       >>> {rjson["state"]}')
            print(f'Casos            >>> {rjson["cases"]}')
            print(f'Mortes           >>> {rjson["deaths"]}')
            print(f'Suspeitas        >>> {rjson["suspects"]}')
            print(f'Recusados        >>> {rjson["refuses"]}')
            print(f'Data de consulta >>> {rjson["datetime"]}')
            print('')
            print(f'\033[1;33m-' * 48)
            restart = str(input(
                f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()


## ==================== cpf.py ====================

## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'  # Preto
Ired = '\033[1;31m'  # Vermelho
Dgreen = '\033[1;32m'  # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'  # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'  # Ciano
Twhite = '\033[1;37m'  # Branco
VRCRM = '\033[0;0m'  # Remover

import os
import requests

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

def consultar():
    clear()
    print('')
    print(f'\n{Iblue}########## #################### ##########')
    print('########## ### Consulta CPF ### ##########')
    print('########## #################### ##########')
    restart = 'S'
    while restart == 'S':
        while True:
            cpf_input = str(input(f'\n{Hcyan}Digite o CPF para consulta: ')).strip().lower()
            if len(cpf_input) > 11:
                print(f'{Ired}!!! {Nyellow}CPF Inválido {Ired}!!!')
            else:
                break
        request = requests.get(f'http://ghostcenter.xyz/api/cpf/{cpf_input}')
        rjson = request.json()
    
        if rjson['status'] == 404:
            restart = str(input(
                f'{Ired}==> CPF NÃO ENCONTRADO <== \n\n\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
        else:
            print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> CPF ENCONTRADO <=={Nyellow} '))
            ordem = 0
            i = rjson['dados']
            ordem += 1
            print(f'\n{Dgreen}{ordem} PESSOA:{Nyellow}')
            print(f" CPF        >>> {i['cpf']}")
            print(f" Nome       >>> {i['nome']}")
            print(f" Nascimento >>> {i['nascimento']}")
            print(f" Sexo       >>> {i['sexo']}\n")
    
            print(f'\033[1;33m-' * 48)
            restart = str(input(
                f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()


## ==================== ip.py ====================

## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

import os
import requests

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

def consultar():
    clear()
    print('')
    print(f'\n{Iblue}########## #################### ##########')
    print('########## ### Consulta IP ### ##########')
    print('########## #################### ##########')
    restart = 'S'
    while restart == 'S':
        while True:
            ip_input = input(f'\n{Hcyan}Digite o IP para consulta: ').strip()
            if len(ip_input) != 13:
                print(f'{Ired}!!! {Nyellow}IP Inválido {Ired}!!!')
            else:
                break
        request = requests.get(f'http://ip-api.com/json/{ip_input}')
        rjson = request.json()

        if rjson['status'] == 'fail':
            restart = str(input(
                f'{Ired}==> IP NÃO ENCONTRADO <== \n\n\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
        else:
            print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> IP ENCONTRADO <=={Nyellow} '))
            print(f'\nQuery[IP]          >>> {rjson["query"]}')
            print(f'País               >>> {rjson["country"]}')
            print(f'Código             >>> {rjson["countryCode"]}')
            print(f'Região             >>> {rjson["regionName"]}')
            print(f'Cidade             >>> {rjson["city"]}')
            print(f'Zip Code           >>> {rjson["zip"]}')
            print(f'Latitude           >>> {rjson["lat"]}')
            print(f'Longitude          >>> {rjson["lon"]}')
            print(f'Fuso Horário       >>> {rjson["timezone"]}')
            print(f'Fornecedor de Rede >>> {rjson["isp"]}')
            print(f'Conexão Org        >>> {rjson["as"]}')
            print('')
            print(f'\033[1;33m-' * 48)
            restart = str(input(
                f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()


## ==================== meuip.py ====================

## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

import os
import requests

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

def consultar():
    clear()
    import netifaces
    gateways = netifaces.gateways()
    gateway_padrao = gateways['default'][netifaces.AF_INET][0]
    print(f"{Hcyan}Your computer's IP address is: \n{Nyellow}{gateway_padrao}")
    input('')
    clear()


#
