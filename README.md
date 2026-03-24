# 😈 EXIFCRACKER v3.0 - Forensics & Metadata Eraser

**EXIFCRACKER** é uma ferramenta de elite para análise e destruição de metadados em imagens. O sistema reconstrói os pixels do arquivo e elimina rastros de GPS, modelo de dispositivo, data/hora e miniaturas ocultas, devolvendo um arquivo totalmente "anônimo" para sua galeria.

---

### 🛡️ Engenharia Forense
Diferente de ferramentas comuns, o EXIFCRACKER não apenas "edita" as tags. Ele:

* 🔍 **Análise Profunda:** Varre o arquivo em busca de tags ocultas e metadados persistentes.
* 🛠️ **Reconstrução:** Refaz o fluxo de dados da imagem (pixel por pixel) para garantir limpeza total.
* 📂 **Output Direto:** Gera um novo arquivo (com o prefixo `LIMPO_`) na pasta de Downloads do sistema.
* 🏁 **Resultado:** A foto volta para sua galeria visualmente idêntica, mas digitalmente limpa e sem rastros forenses.

---

### 📥 Guia de Instalação

#### 🐧 Linux (Debian / Ubuntu / Kali / Parrot)
O motor do script depende do `exiftool`. Instale via terminal:

```bash
sudo apt update && sudo apt install python3 exiftool git -y
git clone [https://github.com/Anonymous40443/EXIFCRACKER](https://github.com/Anonymous40443/EXIFCRACKER)
cd EXIFCRACKER
python3 EXIFCRACKER.py




🪟 Windows (Powershell / CMD)

Para rodar no Windows, siga estes passos rigorosamente:

    Python: Instale o Python 3 através do site oficial python.org. Certifique-se de marcar a opção "Add Python to PATH" na instalação.

    Motor ExifTool: * Baixe o pacote executável no site oficial exiftool.org.

        Extraia o arquivo exiftool(-k).exe.

        Renomeie-o para apenas exiftool.exe.

        Mova o arquivo exiftool.exe para dentro da pasta C:\Windows. (Isso permite que o script chame o motor de qualquer lugar).

    Execução:

PowerShell

git clone [https://github.com/Anonymous40443/EXIFCRACKER](https://github.com/Anonymous40443/EXIFCRACKER)
cd EXIFCRACKER
python EXIFCRACKER.py

    ⚠️ AVISO: Esta ferramenta foi desenvolvida para fins de privacidade pessoal e segurança da informação. Use com responsabilidade.

By: Anonymous40443 🕵️‍♂️
# GRABER-X
