#!/usr/bin/env python3
import os
import sys
import time
import subprocess
import getpass
import shutil
import base64  

G = '\033[1;92m'  
R = '\033[1;91m'  
W = '\033[0m'     

CHAVE_MASCARADA = "NDk4MEtMQg=="

def loading_screen(text="SINCRONIZANDO", duration=1):
    print(f"{G}", end="")
    chars = "⣾⣽⣻⢿⡿⣟⣯⣷"
    for i in range(duration * 10):
        sys.stdout.write(f"\r[{chars[i % len(chars)]}] {text}... ")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"OK!{W}")

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{G}
███████╗██╗  ██╗██╗███████╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝╚██╗██╔╝██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
█████╗   ╚███╔╝ ██║█████╗  ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══╝   ██╔██╗ ██║██╔══╝  ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████╗██╔╝ ██╗██║██║     ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                     [By: Anonymous40443 On Github ]{W}""")

def login():
    banner()
    print(f"\n{G}[ SECURITY GATE ]{W}")
    attempt = getpass.getpass(f"{G}DIGITE A CHAVE: {W}").strip()
    chave_real = base64.b64decode(CHAVE_MASCARADA).decode('utf-8')
    
    if attempt == chave_real:
        loading_screen("VERIFICANDO CREDENCIAIS", 1)
        return True
    
    print(f"{R}[!] CHAVE INCORRETA. ACESSO NEGADO.{W}")
    sys.exit()

def deep_clean_and_save(input_path):
    if not os.path.exists(input_path):
        print(f"{R}[!] Erro: Foto não encontrada.{W}")
        return

    home = os.path.expanduser("~")
    dest_dir = os.path.join(home, "Downloads")
    if not os.path.exists(dest_dir):
        dest_dir = os.getcwd() 

    file_name = "LIMPO_" + os.path.basename(input_path)
    output_path = os.path.join(dest_dir, file_name)
    print(f"\n{G}[*] LIMPANDO E RECONSTRUINDO ARQUIVO...{W}")
    
    try:
        cmd = ["exiftool", "-all=", "--thumbnail", "-CommonStateTags=", "-o", output_path, input_path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if os.path.exists(output_path):
            os.chmod(output_path, 0o644)
            print(f"\n{G}[✓] SUCESSO ABSOLUTO!{W}")
            print(f"{G}➤ ARQUIVO SALVO EM: {output_path}{W}")
        else:
            print(f"{R}[!] Erro ao gerar arquivo limpo: {result.stderr}{W}")
    except Exception as e:
        print(f"{R}[!] Falha no processo: {e}{W}")

def main():
    if not login(): return
    while True:
        banner()
        print(f"\n{G}╔══════════════════════════════════════════════════════╗")
        print(f"║ [1] EXTRAIR METADADOS                                ║")
        print(f"║ [2] APAGAR METADADOS                                 ║")
        print(f"║ [0] SAIR                                             ║")
        print(f"╚══════════════════════════════════════════════════════╝{W}")
        choice = input(f"\n{G}EXIFCRACKER:~$ {W}")
        
        if choice == '1':
            path = input(f"\n{G}➤ ARRASTE A FOTO: {W}").strip().replace("'", "").replace('"', '')
            print(f"\n{G}--- RESULTADO EXIF ---{W}")
            subprocess.run(["exiftool", path])
            input(f"\n{G}Pressione ENTER para voltar...{W}")
        elif choice == '2':
            path = input(f"\n{G}➤ ARRASTE A FOTO PARA LIMPAR: {W}").strip().replace("'", "").replace('"', '')
            loading_screen("EXECUTANDO DEEP CLEAN", 2)
            deep_clean_and_save(path)
            input(f"\n{G}Pressione ENTER para continuar...{W}")
        elif choice == '0':
            print(f"{G}Eu Te Observo...{W}")
            sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
