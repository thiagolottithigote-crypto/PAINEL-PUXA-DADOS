# database/cnpj.py
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
    print(f'\n{Iblue}########## ### Consulta CNPJ ### ##########')
    restart = 'S'
    while restart == 'S':
        cnpj_input = input(f'\n{Hcyan}Digite o CNPJ (14 dígitos): {Twhite}').strip()
        
        if len(cnpj_input) != 14:
            print(f'{Ired}CNPJ inválido! Digite 14 números.{VRCRM}')
            continue
            
        try:
            request = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj_input}')
            rjson = request.json()
            
            if rjson.get('status') == 'ERROR':
                print(f'{Ired}CNPJ não encontrado.{VRCRM}')
            else:
                print(f'\n{Dgreen}==> CNPJ ENCONTRADO <=={Nyellow}')
                print(f'CNPJ            >>> {rjson.get("cnpj")}')
                print(f'Nome            >>> {rjson.get("nome")}')
                print(f'Fantasia        >>> {rjson.get("fantasia")}')
                print(f'Telefone        >>> {rjson.get("telefone")}')
                print(f'Email           >>> {rjson.get("email")}')
                print(f'Cidade          >>> {rjson.get("municipio")} - {rjson.get("uf")}')
                print(f'Situação        >>> {rjson.get("situacao")}')
        except:
            print(f'{Ired}Erro ao consultar CNPJ. API pode estar offline.{VRCRM}')
        
        restart = input(f'\n{Hcyan}Deseja consultar outro CNPJ? (S/N): {Twhite}').strip().upper()
        if restart != 'S':
            clear()
            break
