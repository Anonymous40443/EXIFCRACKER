# 💀 EXIFCRACKER v3.0 - Forensics & Metadata Eraser

![Version](https://img.shields.io/badge/version-3.0-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20Termux-orange)

**EXIFCRACKER** é uma ferramenta de elite para análise e destruição de metadados em imagens. O sistema reconstrói os pixels da imagem e elimina rastros de GPS, modelo de dispositivo, data/hora e miniaturas ocultas, devolvendo um arquivo totalmente "anônimo" para sua galeria.

---

## 🛠️ Como funciona a Limpeza Atômica?
Diferente de apagadores comuns, o EXIFCRACKER não apenas "edita" as tags. Ele:
1. **Analisa** o arquivo em busca de tags ocultas.
2. **Reconstrói** o fluxo de dados da imagem (pixel por pixel).
3. **Gera um novo arquivo** (com o prefixo `LIMPO_`) na sua pasta de Downloads.
4. **Resultado:** A foto volta para sua galeria visualmente idêntica, mas digitalmente limpa e sem rastros.

---

## 📥 Instalação

### 🐧 Linux (Debian/Ubuntu/Kali - APT)
```bash
sudo apt update && sudo apt install python3 exiftool git -y
git clone [https://github.com/Anonymous40443/EXIFCRACKER](https://github.com/Anonymous40443/EXIFCRACKER)
cd EXIFCRACKER
python3 EXIFCRACKER.py

🏹 Linux (Arch/Manjaro - Pacman)
Bash

sudo pacman -S python exiftool git
git clone [https://github.com/Anonymous40443/EXIFCRACKER](https://github.com/Anonymous40443/EXIFCRACKER)
cd EXIFCRACKER
python EXIFCRACKER.py

📱 Android (Termux)
Bash

pkg update && pkg install python exiftool git -y
termux-setup-storage
git clone [https://github.com/Anonymous40443/EXIFCRACKER](https://github.com/Anonymous40443/EXIFCRACKER)
cd EXIFCRACKER
python EXIFCRACKER.py

🪟 Windows (Powershell/CMD)

    Python: Instale o Python 3 via python.org.

    ExifTool: - Baixe o exiftool(-k).exe no site oficial.

        Renomeie para exiftool.exe.

        Mova o arquivo para a pasta C:\Windows.

    Execução:

PowerShell

git clone [https://github.com/Anonymous40443/EXIFCRACKER](https://github.com/Anonymous40443/EXIFCRACKER)
cd EXIFCRACKER
python EXIFCRACKER.py

🔐 Security Gate

A ferramenta possui uma camada de proteção de acesso (Chave: 4980KLB). A chave está mascarada no código fonte em Base64 para evitar detecção simples.

Aviso: Esta ferramenta foi desenvolvida para fins de privacidade pessoal. Use com responsabilidade.

By: Anonymous40443 🕵️‍♂️
