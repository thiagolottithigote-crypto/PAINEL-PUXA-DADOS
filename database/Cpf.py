# database/cpf.py
Mblack = '\033[1;30m'
Ired = '\033[1;31m'
Dgreen = '\033[1;32m'
Nyellow = '\033[1;33m'
Iblue = '\033[1;34m'
Gpurple = '\033[1;35m'
Hcyan = '\033[1;36m'
Twhite = '\033[1;37m'
VRCRM = '\033[0;0m'

import os
import requests

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def consultar():
    clear()
    print(f'\n{Iblue}########## ### Consulta CPF ### ##########')
    restart = 'S'
    while restart == 'S':
        cpf_input = input(f'\n{Hcyan}Digite o CPF: {Twhite}').strip()
        
        if len(cpf_input) < 11:
            print(f'{Ired}CPF inválido!{VRCRM}')
            continue
            
        try:
            request = requests.get(f'http://ghostcenter.xyz/api/cpf/{cpf_input}')
            rjson = request.json()
            
            if rjson.get('status') == 404:
                print(f'{Ired}CPF não encontrado.{VRCRM}')
            else:
                print(f'\n{Dgreen}==> CPF ENCONTRADO <=={Nyellow}')
                dados = rjson.get('dados', {})
                print(f'CPF        >>> {dados.get("cpf")}')
                print(f'Nome       >>> {dados.get("nome")}')
                print(f'Nascimento >>> {dados.get("nascimento")}')
                print(f'Sexo       >>> {dados.get("sexo")}')
        except:
            print(f'{Ired}Erro ao consultar CPF. API pode estar offline.{VRCRM}')
        
        restart = input(f'\n{Hcyan}Deseja consultar outro CPF? (S/N): {Twhite}').strip().upper()
        if restart != 'S':
            clear()
            break
