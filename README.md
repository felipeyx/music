# easy_dl.py — Baixar MP4/MP3 com yt-dlp

> Script simples em **Python** para baixar **vídeos (MP4)** ou **áudio (MP3)** a partir de URLs suportadas pelo `yt-dlp`.  
> Feito para uso **legal**: conteúdos próprios, materiais com **permissão/licença** ou bibliotecas **royalty-free**.

---

## ✨ O que ele faz
- Baixa **MP4** na melhor qualidade (remux para `.mp4` sem recodificar, quando possível).
- Extrai **MP3** em alta qualidade (V0), com **miniatura** e **metadados** (quando disponíveis).
- Cria a pasta `downloads/` automaticamente e salva os arquivos como `%(title)s.%(ext)s`.
- Faz tentativas automáticas (`retries`) e lida melhor com quedas de rede (`fragment_retries`).

---

## 🔧 Requisitos
- **Python 3.8+**
- **yt-dlp**
- **FFmpeg** (recomendado para remux/conversão)

### Instalação rápida
```bash
python -m pip install -U yt-dlp
# FFmpeg:
# Windows: winget install Gyan.FFmpeg
# Linux:   sudo apt install ffmpeg
# macOS:   brew install ffmpeg
