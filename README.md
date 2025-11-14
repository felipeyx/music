# 🎧 easy_dl.py — Baixar MP4/MP3 com yt-dlp

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB)](#)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-enabled-orange)](#)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](#)

Script **simples e eficiente** em **Python** para baixar **vídeo (MP4)** ou **áudio (MP3)** a partir de URLs suportadas pelo `yt-dlp`.  
---

## ✨ Recursos
- **MP4** na melhor qualidade (remux para `.mp4` sem recodificar quando possível).
- **MP3** em alta qualidade (V0) com **capa** e **metadados** (quando disponíveis).
- Salva automaticamente em `downloads/` como `%(title)s.%(ext)s`.
- Mais robusto contra quedas de rede (`retries` e `fragment_retries`).

---

## 🔧 Requisitos
- **Python 3.8+**
- **yt-dlp**
- **FFmpeg** (recomendado para remux/conversão)

### Instalação
```bash
python -m pip install -U yt-dlp
# FFmpeg:
# Windows: winget install Gyan.FFmpeg
# Linux:   sudo apt install ffmpeg
# macOS:   brew install ffmpeg
