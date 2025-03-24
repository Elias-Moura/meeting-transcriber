# 🗣️ Transcrição de Reuniões com Separação de Participantes (Whisper + Pyannote)

Este script Python realiza a transcrição de áudios ou vídeos com identificação de diferentes participantes (diarização de locutor), utilizando:

- 🎤 [Whisper](https://github.com/openai/whisper) da OpenAI para transcrição automática
- 🧠 [pyannote-audio](https://github.com/pyannote/pyannote-audio) para separação de falas por participante
- 🎧 Suporte para entrada em `.mp3`, `.wav`, `.mp4`, `.webm` (qualquer formato que o FFmpeg aceite)

---

Boa parde do código foi tirada desse tutorial do canal 1littlecoder:
[link do video](https://www.youtube.com/watch?v=MVW746z8y_I)

## 🚀 Funcionalidades

- Converte vídeos ou áudios para `.wav` automaticamente usando **FFmpeg**
- Transcreve o conteúdo do áudio para texto com **Whisper**
- Separa as falas por participantes usando **clustering de embeddings de voz**
- Gera um arquivo `transcricao_formatada.txt` com o conteúdo dividido por `SPEAKER 1`, `SPEAKER 2`, etc.

---

## 📦 Requisitos

- Python 3.8+
- GPU com CUDA (recomendado)
- FFmpeg instalado no sistema [Linux](https://www.geeksforgeeks.org/how-to-install-ffmpeg-in-linux/) [Windows](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)
- Dependências Python:

```bash
pip install -r requirements.txt
```

🛠️ Como usar
1. Configure o script

No final do arquivo .py, altere estas variáveis conforme seu caso:

audio_path = 'akita.webm'  # Caminho para o arquivo de áudio ou vídeo
speakers = 2               # Número estimado de participantes
model = 'turbo'             # Modelo Whisper: tiny, base, small, medium, large, turbo *escolha conforme a sua GPU

O modelo turbo uso algo entre 6 a 7Gb de VRAM


1. Execute o script
```
python main.py
```

🧾 Exemplo de saída (transcricao_formatada.txt)

```
SPEAKER 1 0:00:03
Bom dia a todos, vamos iniciar a reunião.

SPEAKER 2 0:00:10
Tudo certo, podemos seguir com a pauta de hoje.
```

❓ Dúvidas comuns
📌 Por que o arquivo .wav fica tão grande?

O .wav é um formato sem compressão, usado para garantir máxima fidelidade de áudio para os modelos. Ele ocupa mais espaço, mas é necessário para a precisão.

📌 O script melhora a qualidade ao converter de .mp3 para .wav?

Não. A conversão não recupera qualidade perdida, apenas transforma o áudio para um formato compatível com os modelos.

📍 Melhorias futuras (sugestões) 
Geração de ata automatizada com GPT (via http) ou implementação usando llama

Interface web com upload de arquivos


# 🗣️ Meeting Transcription with Speaker Separation (Whisper + Pyannote)

This Python script performs audio or video transcription with speaker identification (speaker diarization), using:

- 🎤 [Whisper](https://github.com/openai/whisper) by OpenAI for automatic transcription
- 🧠 [pyannote-audio](https://github.com/pyannote/pyannote-audio) for separating speech by speaker
- 🎧 Supports input formats like `.mp3`, `.wav`, `.mp4`, `.webm` (any format supported by FFmpeg)

---

A good part of the code was adapted from this tutorial by 1littlecoder:  
[Watch the video](https://www.youtube.com/watch?v=MVW746z8y_I)

---

## 🚀 Features

- Automatically converts video or audio to `.wav` using **FFmpeg**
- Transcribes audio content to text using **Whisper**
- Separates speech by speaker using **voice embedding clustering**
- Generates a `transcricao_formatada.txt` file with content divided by `SPEAKER 1`, `SPEAKER 2`, etc.

---

## 📦 Requirements

- Python 3.8+
- CUDA-enabled GPU (recommended)
- FFmpeg installed on your system ([Linux](https://www.geeksforgeeks.org/how-to-install-ffmpeg-in-linux/) | [Windows](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/))
- Python dependencies:

```bash
pip install -r requirements.txt
```

🛠️ How to Use
1. Configure the script

At the end of the .py file, adjust these variables according to your setup:

```
audio_path = 'akita.webm'  # Path to your audio or video file
speakers = 2               # Estimated number of participants
model = 'turbo'            # Whisper model: tiny, base, small, medium, large, turbo (choose based on your GPU)
```

💡 The turbo model uses around 6 to 7GB of VRAM

2. Run the script
```
python main.py
```

🧾 Example Output (transcricao_formatada.txt)

```
SPEAKER 1 0:00:03
Good morning everyone, let's start the meeting.

SPEAKER 2 0:00:10
All set, we can proceed with today's agenda.
```
❓ Frequently Asked Questions
📌 Why is the .wav file so large?

The .wav format is uncompressed, used to ensure maximum audio fidelity for the models. It takes up more space but is required for accurate processing.

📌 Does the script improve audio quality when converting from .mp3 to .wav?

No. Conversion does not recover lost quality — it only transforms the file into a model-compatible format.

📍 Future Improvements (Ideas)
Automated meeting summary (minutes) generation using GPT (via HTTP) or local model integration like LLaMA

Web interface for file upload