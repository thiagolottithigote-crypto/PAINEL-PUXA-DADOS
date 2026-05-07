# database/meuip.py
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
    print(f'\n{Iblue}########## ### Meu IP ### ##########')
    try:
        # IP externo
        request = requests.get('https://api.ipify.org?format=json')
        ip_externo = request.json()['ip']
        
        print(f'\n{Dgreen}Seu IP Externo:{Nyellow}')
        print(f'IP → {ip_externo}')
        
        # Info adicional do IP
        request2 = requests.get(f'http://ip-api.com/json/{ip_externo}')
        info = request2.json()
        
        print(f'País       → {info.get("country")}')
        print(f'Cidade     → {info.get("city")}')
        print(f'Provedor   → {info.get("isp")}')
        
    except:
        print(f'{Ired}Não foi possível obter seu IP.{VRCRM}')
    
    input(f'\n{Hcyan}Pressione ENTER para voltar...{Twhite}')
    clear()
