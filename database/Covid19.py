# database/covid19.py
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
    print(f'\n{Iblue}########## ### Consulta COVID-19 ### ##########')
    restart = 'S'
    while restart == 'S':
        uf = input(f'\n{Hcyan}Digite a UF (ex: SP, RJ, MG): {Twhite}').strip().upper()
        
        if len(uf) != 2:
            print(f'{Ired}UF inválida! Digite apenas 2 letras.{VRCRM}')
            continue
            
        try:
            request = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{uf}')
            rjson = request.json()
            
            if 'error' in rjson:
                print(f'{Ired}UF não encontrada.{VRCRM}')
            else:
                print(f'\n{Dgreen}==> DADOS COVID-19 - {uf} <=={Nyellow}')
                print(f'Estado     >>> {rjson.get("state")}')
                print(f'Casos      >>> {rjson.get("cases"):,}')
                print(f'Mortes     >>> {rjson.get("deaths"):,}')
                print(f'Suspeitos  >>> {rjson.get("suspects"):,}')
                print(f'Data       >>> {rjson.get("datetime")}')
        except:
            print(f'{Ired}Erro ao consultar dados de COVID.{VRCRM}')
        
        restart = input(f'\n{Hcyan}Deseja consultar outra UF? (S/N): {Twhite}').strip().upper()
        if restart != 'S':
            clear()
            break
