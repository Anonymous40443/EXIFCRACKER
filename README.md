# 😈 EXIFCRACKER v3.0 - Forensics & Metadata Eraser

**EXIFCRACKER** é uma ferramenta de elite para análise e destruição de metadados em imagens. O sistema reconstrói os pixels do arquivo e elimina rastros de GPS, modelo de dispositivo, data/hora e miniaturas ocultas, devolvendo um arquivo totalmente "anônimo" para sua galeria.

---

### 🛡️ Engenharia Forense
Diferente de ferramentas comuns, o EXIFCRACKER não apenas "edita" as tags. Ele:

* 🔍 **Análise Profunda:** Varre o arquivo em busca de tags ocultas e metadados persistentes.
* 🛠️ **Reconstrução:** Refaz o fluxo de dados da imagem (pixel por pixel) para garantir limpeza total.
* 📂 **Output Direto:** Gera um novo arquivo (com o prefixo **LIMPO_**) na pasta de Downloads do sistema.
* 🏁 **Resultado:** A foto volta para sua galeria visualmente idêntica, mas digitalmente limpa e sem rastros forenses.

---

### 📥 Guia de Instalação

#### 🐧 Linux (Debian / Ubuntu / Kali / Parrot)
O motor do script depende do exiftool. Instale via terminal:
```bash
sudo apt update && sudo apt install python3 exiftool git -y
git clone [https://github.com/Anonymous40443/EXIFCRACKER](https://github.com/Anonymous40443/EXIFCRACKER)
cd EXIFCRACKER
python3 EXIFCRACKER.py
