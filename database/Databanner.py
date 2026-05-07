# database/banner.py
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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear()
    print(fr'''{Ired}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                  ┃
┃   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    ┃
┃    {Gpurple} /\\,/\\,     |\         -__ /\\                       ,,     {Ired}┃
┃    {Gpurple}/| || ||   '   \\          ||  \\   _    '             ||     {Ired}┃
┃    {Gpurple}|| || ||  \\  / \\        /||__||  < \, \\ \\/\\  _-_  ||     {Ired}┃
┃    {Gpurple}||=|= ||  || || ||        \||__||  /-|| || || || || \\ ||     {Ired}┃
┃   {Gpurple}~|| || ||  || || ||         ||  |, (( || || || || ||/   ||     {Ired}┃
┃    {Gpurple}|, \\,\\, \\  \\/        _-||-_/   \/\\ \\ \\ \\ \\,/  \\ {Hcyan}2.0{Ired} ┃
┃   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    ┃
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
