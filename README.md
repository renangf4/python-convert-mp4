# Conversor de Vídeos para MP4 (Python)

Este script converte automaticamente todos os vídeos de uma pasta para o formato `.mp4`, usando o `ffmpeg` local via `ffmpeg-static` (instalado com NPM). Ele utiliza codec H.264 e áudio AAC para melhor compatibilidade e qualidade.

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
├── videos/                 # Coloque aqui os vídeos (.webm, .mov, .avi, .mkv, etc.)
└── convertidos_mp4/        # Pasta de saída (será criada automaticamente)
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

Ou use o arquivo batch no Windows:

```bash
exec.bat
```

Os arquivos convertidos serão salvos automaticamente na pasta `convertidos_mp4/`.

---

## 🎥 Formatos suportados

O script processa automaticamente os seguintes formatos:

- `.mp4` (reconverte com configurações otimizadas)
- `.webm` 
- `.mov`
- `.avi`
- `.mkv`

---

## 🔧 Configurações de qualidade

O script usa as seguintes configurações otimizadas:

- **Codec de vídeo**: H.264 (libx264)
- **Codec de áudio**: AAC
- **Bitrate**: 5000 kbps
- **Qualidade CRF**: 23 (excelente qualidade)
- **Threads**: Automático (usa todos os cores disponíveis)

### Ajustar qualidade (opcional)

Para modificar a qualidade, edite estas linhas no `converter.py`:

```python
"-b:v", "5000k",   # Bitrate de vídeo (aumente para mais qualidade)
"-crf", "23",      # Qualidade (0-51: menor = melhor qualidade)
```

**Sugestões de CRF:**
- `18-23`: Excelente qualidade (padrão)
- `24-28`: Boa qualidade 
- `29-35`: Qualidade média (arquivos menores)

---

## 🚀 Recursos

- ✅ **Detecção automática** do caminho do FFmpeg
- ✅ **Suporte multiplataforma** (Windows, macOS, Linux)
- ✅ **Conversão em lote** de múltiplos arquivos
- ✅ **Configurações otimizadas** para web e compatibilidade
- ✅ **Tratamento de erros** com mensagens claras
- ✅ **Criação automática** da pasta de saída

---

## 📄 Licença

Este projeto é livre para uso pessoal ou profissional.