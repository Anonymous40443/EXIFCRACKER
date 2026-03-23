# 🟢 EXIFCRACKER v2.0
### Hardcore Metadata Destroyer & Image Reconstructor

O **EXIFCRACKER** é uma ferramenta desenvolvida para aniquilar rastros digitais em imagens (JPEG/JPG). Diferente de limpadores comuns, ele possui um **Modo Nuclear** que reconstrói a imagem bit a bit para garantir anonimato total.

---

## ⚡ Funcionalidades
* **Extração Completa:** Visualiza todos os metadados ocultos (GPS, Modelo, Serial).
* **Deep Clean:** Remove todas as tags Exif, XMP, IPTC e trailers de arquivos.
* **Anti-Thumbnail:** Elimina miniaturas escondidas que guardam localização original.
* **Interface Matrix:** Estilo High-Intensity Green para máxima visibilidade.

## 🚀 Como Executar

### No Kali Linux:
1. Instale as dependências:
   ```bash
   sudo apt update && sudo apt install -y exiftool python3 python3-pil
   ```
2. Execute o script:
   ```bash
   python3 EXIFCRACKER.py
   ```

### No Termux (Android):
1. Instale as dependências:
   ```bash
   pkg install python exiftool termux-api -y
   pip install Pillow
   ```
2. Dê permissão de armazenamento:
   ```bash
   termux-setup-storage
   ```
3. Execute:
   ```bash
   python EXIFCRACKER.py
   ```

---

**By: [Anonymous40443](https://github.com/Anonymous40443)**
