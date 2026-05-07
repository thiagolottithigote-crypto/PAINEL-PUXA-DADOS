# database/placa.py
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
    print(f'\n{Iblue}########## ### Consulta PLACA ### ##########')
    restart = 'S'
    while restart == 'S':
        placa_input = input(f'\n{Hcyan}Digite a Placa (ex: ABC1234): {Twhite}').strip().upper()
        
        if len(placa_input) < 7:
            print(f'{Ired}Placa inválida!{VRCRM}')
            continue
            
        try:
            request = requests.get(f'https://apicarros.com/v1/consulta/{placa_input}/json')
            rjson = request.json()
            
            if rjson.get('erro') or 'placa' not in rjson:
                print(f'{Ired}Placa não encontrada.{VRCRM}')
            else:
                print(f'\n{Dgreen}==> PLACA ENCONTRADA <=={Nyellow}')
                print(f'Placa       >>> {rjson.get("placa")}')
                print(f'Marca       >>> {rjson.get("marca")}')
                print(f'Modelo      >>> {rjson.get("modelo")}')
                print(f'Ano         >>> {rjson.get("ano")}')
                print(f'Cor         >>> {rjson.get("cor")}')
                print(f'Município   >>> {rjson.get("municipio")}')
                print(f'Situação    >>> {rjson.get("situacao")}')
        except:
            print(f'{Ired}Erro ao consultar placa. API pode estar offline.{VRCRM}')
        
        restart = input(f'\n{Hcyan}Deseja consultar outra placa? (S/N): {Twhite}').strip().upper()
        if restart != 'S':
            clear()
            break
