import os
import subprocess
from pathlib import Path

try:
    resultado = subprocess.run(
        ['node', '-e', 'console.log(require("./node_modules/ffmpeg-static"))'],
        capture_output=True,
        text=True,
        check=True
    )
    ffmpeg_path = resultado.stdout.strip()
except subprocess.CalledProcessError:
    print("Erro: Não foi possível obter o caminho do FFmpeg.")
    print("Certifique-se de que o ffmpeg-static foi instalado corretamente com: npm install ffmpeg-static")
    exit(1)

if not os.path.exists(ffmpeg_path):
    print(f"Erro: FFmpeg não encontrado em: {ffmpeg_path}")
    print("Certifique-se de que o ffmpeg-static foi instalado corretamente com: npm install ffmpeg-static")
    exit(1)

print(f"Usando FFmpeg em: {ffmpeg_path}")

input_dir = "videos"
output_dir = "convertidos_mp4" 

os.makedirs(output_dir, exist_ok=True)

extensoes_validas = (".mp4", ".mov", ".avi", ".mkv", ".webm")

for nome_arquivo in os.listdir(input_dir):
    if nome_arquivo.lower().endswith(extensoes_validas):
        caminho_entrada = os.path.join(input_dir, nome_arquivo)
        
        nome_base = os.path.splitext(nome_arquivo)[0]
        
        caminho_saida = os.path.join(output_dir, f"{nome_base}.mp4")

        try:
            comando = [
                ffmpeg_path,
                "-i", caminho_entrada,
                "-c:v", "libx264", # Codec de vídeo para MP4
                "-c:a", "aac",     # Codec de áudio para MP4
                "-b:v", "5000k",   # Bitrate de vídeo (5000 kbps), ajuste este valor para mudar a qualidade
                "-crf", "23",      # Fator de qualidade (0-51, onde 0 é sem perdas e 51 é o pior)
                "-threads", "0",
                caminho_saida
            ]

            subprocess.run(comando, check=True)
            print(f"Convertido: {nome_arquivo} → {nome_base}.mp4")

        except subprocess.CalledProcessError as e:
            print(f"Erro ao converter {nome_arquivo}: {e}")