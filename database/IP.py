# database/ip.py
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
    print(f'\n{Iblue}########## ### Consulta IP ### ##########')
    restart = 'S'
    while restart == 'S':
        ip_input = input(f'\n{Hcyan}Digite o IP: {Twhite}').strip()
        
        if len(ip_input) < 7:
            print(f'{Ired}IP inválido!{VRCRM}')
            continue
            
        try:
            request = requests.get(f'http://ip-api.com/json/{ip_input}')
            rjson = request.json()
            
            if rjson.get('status') == 'fail':
                print(f'{Ired}IP não encontrado ou inválido.{VRCRM}')
            else:
                print(f'\n{Dgreen}==> IP ENCONTRADO <=={Nyellow}')
                print(f'IP              >>> {rjson.get("query")}')
                print(f'País            >>> {rjson.get("country")}')
                print(f'Cidade          >>> {rjson.get("city")}')
                print(f'Região          >>> {rjson.get("regionName")}')
                print(f'Provedor        >>> {rjson.get("isp")}')
                print(f'Coordenadas     >>> {rjson.get("lat")}, {rjson.get("lon")}')
        except:
            print(f'{Ired}Erro ao consultar IP. API pode estar offline.{VRCRM}')
        
        restart = input(f'\n{Hcyan}Deseja consultar outro IP? (S/N): {Twhite}').strip().upper()
        if restart != 'S':
            clear()
            break
