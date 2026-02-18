import sounddevice as sd
import numpy as np
import noisereduce as nr
from faster_whisper import WhisperModel
from openai import OpenAI
from gtts import gTTS
import os
import time
import io
import pygame
from gtts import gTTS
import os
from dotenv import load_dotenv

load_dotenv()
pygame.mixer.init(frequency=24000)



#################### CONFIG ####################

fs = 16000
seconds = 5

print("Carregando modelo Whisper...")
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

# 🔑 COLOQUE SUA CHAVE GEMINI AQUI
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#################### GRAVAÇÃO DE VOZ ####################

def gravar_audio(duracao=5):
    print("\n🎤 Gravando por 5 segundos...")
    recording = sd.rec(
        int(duracao * fs),
        samplerate=fs,
        channels=1,
        dtype='float32'
    )
    sd.wait()

    audio = recording.flatten()
    audio = nr.reduce_noise(y=audio, sr=fs)

    return audio

#################### TRANSCRIÇÃO DE VOZ ####################

def transcrever_audio(audio_array):
    segments, info = model.transcribe(
        audio_array,
        language="pt"
    )

    texto = ""
    for segment in segments:
        texto += segment.text

    return texto

#################### GEMINI (COM TRATAMENTO DE COTA) ####################

def perguntar_gemini(texto_usuario):
    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": texto_usuario}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        if "429" in str(e):
            return "Desculpe, mestre, mas atingi meu limite de fôlego por agora. Por favor, aguarde 30 segundos e tente novamente."
        return f"Ocorreu um erro: {e}"

#################### TTS GOOGLE ####################

def falar_google(texto):
    if not texto: 
        return
    
    try:
        # 1. Gera o TTS
        tts = gTTS(text=texto, lang="pt")
        
        # 2. Usa um buffer de memória
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        
        # 3. Carrega o áudio
        pygame.mixer.music.load(mp3_fp, "mp3")
        
        # 4. Toca o áudio
        print("🔊 Reproduzindo resposta...")
        pygame.mixer.music.play()
        
        # 5. BLOQUEIO ESSENCIAL: Impede o código de continuar até o som acabar
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        # Limpa o carregamento para liberar a memória
        pygame.mixer.music.unload()
        
    except Exception as e:
        print(f"Erro na reprodução de áudio: {e}")

#################### EXECUÇÃO (EM LOOP) ####################

print("--- Sistema Pronto! Pressione Ctrl+C para encerrar no terminal ---")

try:
    while True:
        # 1️⃣ Grava
        audio = gravar_audio(seconds)

        # 2️⃣ Transcreve
        texto_usuario = transcrever_audio(audio)
        print("Você disse:", texto_usuario)

        # Comando para sair se detectar a palavra
        if "sair" in texto_usuario.lower() or "encerrar" in texto_usuario.lower():
            print("Encerrando...")
            falar_google("Até logo!")
            break

        # 3️⃣ Pergunta para Gemini
        resposta = perguntar_gemini(texto_usuario)
        print("Gemini respondeu:", resposta)

        # 4️⃣ Gemini fala
        falar_google(resposta)
        
        # Pequena pausa para você ler a resposta antes de gravar de novo
        time.sleep(2)

except KeyboardInterrupt:
    print("\nSaindo com segurança...")