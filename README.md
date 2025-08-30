# Conversor de Vídeos para WebM (Python)

Este script converte automaticamente todos os vídeos de uma pasta para o formato `.webm`, usando o `ffmpeg` local via `ffmpeg-static` (instalado com NPM). Ele utiliza compressão VP9 e áudio Opus para melhor qualidade e compatibilidade com navegadores modernos.

---

## ✅ Requisitos

- Python 3.x instalado
- Node.js instalado
- FFmpeg local com [ffmpeg-static](https://www.npmjs.com/package/ffmpeg-static)

Instale o FFmpeg local com:

```bash
npm install ffmpeg-static
```

---

## 📁 Estrutura esperada

Crie a seguinte estrutura de pastas:

```
projeto/
├── converter.py              # Script principal em Python
├── package.json
├── node_modules/           # Instalado automaticamente pelo NPM
├── videos/                 # Coloque aqui os vídeos (.mp4, .mov, etc.)
└── convertidos_webm/       # Pasta de saída (será criada automaticamente)
```

> ⚠️ **Importante**: Crie a pasta `videos/` e coloque seus vídeos antes de rodar o script.

---

## ▶️ Como usar

1. Instale as dependências com:

```bash
npm install ffmpeg-static
```

2. Coloque seus vídeos na pasta `videos/`
3. Execute o script com:

```bash
python converter.py
```

Os arquivos convertidos serão salvos automaticamente na pasta `convertidos_webm/`.

---

## 🔧 Ajustes (opcional)

- O script usa o codec VP9 (`libvpx-vp9`) com bitrate de `1M` e áudio Opus (`libopus`).
- Para reduzir ou aumentar a qualidade, edite a linha:

```python
"-b:v", "1M",  # ← aumente para 2M, 3M, etc.
```

---

## 📄 Licença

Este projeto é livre para uso pessoal ou profissional.
