# database/nome.py
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
    print(f'\n{Iblue}########## ### Consulta NOME ### ##########')
    restart = 'S'
    while restart == 'S':
        nome_input = input(f'\n{Hcyan}Digite o Nome completo ou parte dele: {Twhite}').strip()
        
        if len(nome_input) < 3:
            print(f'{Ired}Nome muito curto!{VRCRM}')
            continue
            
        try:
            request = requests.get(f'http://ghostcenter.xyz/api/nome/{nome_input}')
            rjson = request.json()
            
            if rjson.get('status') == 404:
                print(f'{Ired}Nenhum resultado encontrado.{VRCRM}')
            else:
                print(f'\n{Dgreen}==> RESULTADOS ENCONTRADOS <=={Nyellow}')
                print(f'Total encontrado: {rjson.get("total", 0)}\n')
                
                dados = rjson.get('dados', [])
                for i, pessoa in enumerate(dados, 1):
                    print(f'{Dgreen}{i}ª Pessoa:{Nyellow}')
                    print(f'Nome       >>> {pessoa.get("nome")}')
                    print(f'CPF        >>> {pessoa.get("cpf")}')
                    print(f'Nascimento >>> {pessoa.get("nascimento")}')
                    print(f'Sexo       >>> {pessoa.get("sexo")}')
                    print('-' * 40)
        except:
            print(f'{Ired}Erro ao consultar nome. API pode estar offline.{VRCRM}')
        
        restart = input(f'\n{Hcyan}Deseja consultar outro nome? (S/N): {Twhite}').strip().upper()
        if restart != 'S':
            clear()
            break
