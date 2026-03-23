#!/usr/bin/env python3
import os, sys, time, subprocess, getpass
from PIL import Image

# Cores High-Intensity
G = '\033[1;92m'
R = '\033[1;91m'
W = '\033[0m'

PASSWORD_REQUIRED = "4980KLB"

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{G}
 █████╗ ███╗  ██╗ ██████╗ ███╗  ██╗██╗   ██╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║╚██╗ ██╔╝████╗ ████║██╔═══██╗██║   ██║██╔════╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║ ╚████╔╝ ██╔████╔██║██║   ██║██║   ██║███████╗
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║  ╚██╔╝  ██║╚██╔╝██║██║   ██║██║   ██║╚════██║
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║   ██║   ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
                     [ V3.0 - MODO DESTRUIÇÃO TOTAL ]{W}""")

def login():
    banner()
    print(f"\n{G}[ SECURITY GATE ]{W}")
    attempt = getpass.getpass(f"{G}DIGITE A CHAVE: {W}")
    if attempt == PASSWORD_REQUIRED: return True
    print(f"{R}[!] CHAVE INCORRETA.{W}")
    sys.exit()

def get_path():
    print(f"\n{G}Dica: No Termux, fotos ficam em /sdcard/Download/nome.jpg{W}")
    path = input(f"{G}➤ CAMINHO DO ARQUIVO: {W}").strip().replace("'", "").replace('"', '')
    return path if os.path.exists(path) else None

def nuclear_clean(path):
    try:
        print(f"{G}[*] Iniciando Reconstrução Atômica de Pixels...{W}")
        img = Image.open(path)
        img_pure = Image.new(img.mode, img.size)
        img_pure.putdata(list(img.getdata()))
        
        out_dir = "/sdcard/Download" if os.path.exists('/data/data/com.termux') else os.path.join(os.path.expanduser("~"), "Downloads")
        out_path = os.path.join(out_dir, "ANONIMO_" + os.path.basename(path))
        
        # O segredo da v3.0: exif=b"" limpa o que o putdata esquece
        img_pure.save(out_path, "JPEG", quality=100, optimize=True, exif=b"")
        print(f"\n{G}[✓] SUCESSO! TOTALMENTE PELADA EM: {out_path}{W}")
    except Exception as e: print(f"{R}[!] Erro: {e}{W}")

def main():
    if not login(): return
    if os.path.exists('/data/data/com.termux') and not os.path.exists('/sdcard/Download'):
        os.system('termux-setup-storage')

    while True:
        banner()
        print(f"\n{G}╔══════════════════════════════════════════════════════╗")
        print(f"║ [1] SCAN FORENSE (VER TUDO OCULTO)                   ║")
        print(f"║ [2] DESTRUIÇÃO ATÔMICA (RECONSTRUIR FOTO)            ║")
        print(f"║ [0] SAIR                                             ║")
        print(f"╚══════════════════════════════════════════════════════╝{W}")
        op = input(f"\n{G}ANONYMOUS@SYSTEM:~$ {W}")
        
        if op == '1':
            p = get_path()
            if p:
                subprocess.run(["exiftool", "-all", "-G", p])
                input(f"\n{G}ENTER para voltar...{W}")
        elif op == '2':
            p = get_path()
            if p: nuclear_clean(p); time.sleep(2)
        elif op == '0': break

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: sys.exit()
