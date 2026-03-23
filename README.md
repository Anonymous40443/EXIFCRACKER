# 🟢 EXIFCRACKER v3.0 [MODO ATÔMICO]
### Hardcore Metadata Destroyer & Forensic Scanner

O **EXIFCRACKER** é uma ferramenta desenvolvida para aniquilar rastros digitais em imagens (JPEG/JPG). Diferente de limpadores comuns, ele possui um **Modo Atômico** que reconstrói a imagem bit a bit (pixel por pixel) para garantir anonimato total.

---

## ⚡ Funcionalidades
* **Extração Completa:** Visualiza todos os metadados ocultos (GPS, Modelo, Serial).
* **Deep Clean:** Remove todas as tags Exif, XMP, IPTC e trailers de arquivos.
* **Anti-Thumbnail:** Elimina miniaturas escondidas que guardam a localização original.
* **Modo Atômico:** Reconstrói a imagem do zero, enviando-a "pelada" para sua galeria.

---

## 🚀 Como Instalar e Executar

### 🔵 No Kali Linux:
1. `git clone https://github.com/Anonymous40443/EXIFCRACKER.git`
2. `cd EXIFCRACKER`
3. `sudo apt update && sudo apt install -y exiftool python3 python3-pil`
4. `python3 EXIFCRACKER.py`

### 🟢 No Termux (Android):
1. `pkg install python exiftool termux-api -y`
2. `pip install Pillow`
3. `termux-setup-storage`
4. `python EXIFCRACKER.py`

---

## 📱 Dica de Uso no Mobile
Para processar fotos da sua galeria no Android, indique o caminho:
` /sdcard/Download/suafoto.jpg `
O arquivo limpo será salvo como `PELADA_suafoto.jpg` na sua pasta de Downloads e aparecerá na galeria automaticamente.

---
**By: [Anonymous40443](https://github.com/Anonymous40443)**
