# database/cep.py
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
    print(f'\n{Iblue}########## ### Consulta CEP ### ##########')
    restart = 'S'
    while restart == 'S':
        cep_input = input(f'\n{Hcyan}Digite o CEP (8 dígitos): {Twhite}').strip()
        
        if len(cep_input) != 8:
            print(f'{Ired}CEP inválido! Digite 8 números.{VRCRM}')
            continue
            
        try:
            request = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')
            rjson = request.json()
            
            if 'erro' in rjson:
                print(f'{Ired}CEP não encontrado.{VRCRM}')
            else:
                print(f'\n{Dgreen}==> CEP ENCONTRADO <=={Nyellow}')
                print(f'CEP         >>> {rjson.get("cep")}')
                print(f'Logradouro  >>> {rjson.get("logradouro")}')
                print(f'Bairro      >>> {rjson.get("bairro")}')
                print(f'Cidade      >>> {rjson.get("localidade")}')
                print(f'Estado      >>> {rjson.get("uf")}')
                print(f'DDD         >>> {rjson.get("ddd")}')
        except:
            print(f'{Ired}Erro ao consultar CEP.{VRCRM}')
        
        restart = input(f'\n{Hcyan}Deseja consultar outro CEP? (S/N): {Twhite}').strip().upper()
        if restart != 'S':
            clear()
            break
