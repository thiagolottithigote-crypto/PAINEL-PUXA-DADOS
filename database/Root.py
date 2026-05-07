# database/root.py
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

def consultar():
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    print(f'\n{Iblue}########## ### Root Checker ### ##########')
    
    try:
        if os.geteuid() == 0:
            print(f'\n{Dgreen}✅ Você está com privilégios ROOT!{VRCRM}')
        else:
            print(f'\n{Ired}❌ Você NÃO está com privilégios ROOT.{VRCRM}')
    except:
        # Para Termux / Android (não tem geteuid)
        print(f'\n{Nyellow}🔍 Verificando ambiente...')
        if 'ANDROID_ROOT' in os.environ or 'TERMUX' in os.environ or os.path.exists('/data/data/com.termux'):
            print(f'{Dgreen}✅ Ambiente Termux/Android detectado.{VRCRM}')
        else:
            print(f'{Ired}❌ Sem privilégios ROOT detectados.{VRCRM}')
    
    input(f'\n{Hcyan}Pressione ENTER para voltar ao menu...{Twhite}')
