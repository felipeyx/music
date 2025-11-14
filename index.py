# easy_dl.py - cmd python easy_dl.py

from yt_dlp import YoutubeDL

def main():
    url = input("Cole a URL (vídeo/playlist): ").strip()
    if not url:
        print("URL vazia. Saindo.")
        return

    print("\nBaixar como:\n  [1] MP4 (vídeo)\n  [2] MP3 (áudio)")
    choice = input("Escolha 1 ou 2: ").strip()

    if choice == "1":
        # MP4 melhor qualidade (remux para .mp4 sem recodificar quando possível)
        ydl_opts = {
            "format": "bv*+ba/b",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "retries": 10,
            "fragment_retries": 10,
            "postprocessors": [
                {"key": "FFmpegVideoRemuxer", "preferedformat": "mp4"}
            ],
        }
        modo = "MP4"
    elif choice == "2":
        # MP3 de alta qualidade, com capa/metadados quando disponíveis
        ydl_opts = {
            "format": "ba/b",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "retries": 10,
            "fragment_retries": 10,
            "postprocessors": [
                {"key": "FFmpegExtractAudio",
                 "preferredcodec": "mp3",
                 "preferredquality": "0"},
                {"key": "EmbedThumbnail"},
                {"key": "FFmpegMetadata"},
            ],
        }
        modo = "MP3"
    else:
        print("Opção inválida. Saindo.")
        return

    print(f"\nBaixando em {modo} para a pasta 'downloads/'...\n")
    with YoutubeDL(ydl_opts) as ydl:
        code = ydl.download([url])

    if code == 0:
        print("\n✅ Concluído!")
    else:
        print(f"\n❌ Erro (código {code}). Verifique a URL e o FFmpeg.")

if __name__ == "__main__":
    main()