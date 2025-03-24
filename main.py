import subprocess
import datetime
import torch
import numpy as np
import whisper
import wave
import contextlib
from sklearn.cluster import AgglomerativeClustering
from pyannote.audio import Audio
from pyannote.core import Segment
from pyannote.audio.pipelines.speaker_verification import PretrainedSpeakerEmbedding

# Função para converter para WAV se necessário
def convert_to_wav(audio_path):
    if not audio_path.endswith('.wav'):
        wav_path = 'audio.wav'
        subprocess.call(['ffmpeg', '-i', audio_path, wav_path, '-y'])
        return wav_path
    return audio_path

# Função auxiliar de tempo
def time(secs):
    return datetime.timedelta(seconds=round(secs))

# Função principal
def main(audio_path, num_speakers, model_size):
    print("Preparando modelo Whisper e PyAnnote...")

    path = convert_to_wav(audio_path)

    model = whisper.load_model(model_size)
    result = model.transcribe(path)
    segments = result["segments"]

    with contextlib.closing(wave.open(path,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)

    embedding_model = PretrainedSpeakerEmbedding(
        "speechbrain/spkrec-ecapa-voxceleb",
        device=torch.device("cuda" if torch.cuda.is_available() else "cpu"))

    audio = Audio()

    def segment_embedding(segment):
        start = segment["start"]
        end = min(duration, segment["end"])
        clip = Segment(start, end)
        waveform, _ = audio.crop(path, clip)
        # 💡 Corrigir áudio estéreo para mono
        if waveform.shape[0] > 1:
            waveform = waveform.mean(dim=0, keepdim=True)
        return embedding_model(waveform[None])

    print("Gerando embeddings de voz...")
    embeddings = np.zeros(shape=(len(segments), 192))
    for i, segment in enumerate(segments):
        embeddings[i] = segment_embedding(segment)

    embeddings = np.nan_to_num(embeddings)
    clustering = AgglomerativeClustering(num_speakers).fit(embeddings)
    labels = clustering.labels_

    for i in range(len(segments)):
        segments[i]["speaker"] = 'SPEAKER ' + str(labels[i] + 1)

    print("Gerando transcrição com identificação dos participantes...")
    with open("transcricao_formatada.txt", "w", encoding="utf-8") as f:
        for i, segment in enumerate(segments):
            if i == 0 or segments[i - 1]["speaker"] != segment["speaker"]:
                f.write("\n" + segment["speaker"] + ' ' + str(time(segment["start"])) + '\n')
            f.write(segment["text"][1:] + ' ')

    print("Transcrição salva em transcricao_formatada.txt")


if __name__ == "__main__":
    audio_path = 'akita.webm'
    speakers = 1
    model = 'turbo'

    main(audio_path, speakers, model)
