import os
import numpy as np
import keras
import pickle
import pyaudio
import vosk
import json

def escuchar():
    model = vosk.Model("liz/voice_engine/models/vosk-model-en-us-0.42-gigaspeech")
    recognizer = vosk.KaldiRecognizer(model, 16000)

    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("🎤 Escuchando...")
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            return result["text"]


# Cargar modelo y tokenizer
model: keras.Sequential = keras.models.load_model("liz/liz_0000.keras")
with open("liz/vectorizer.pickle", "rb") as handle:
    vectorizer = pickle.load(handle)
with open("liz/label_mapping.pickle", "rb") as handle:
    label_mapping: dict = pickle.load(handle)

# Funciones para ejecutar comandos
def open_browser(): os.system("start chrome")
def close_browser(): os.system("taskkill /IM chrome.exe /F")
def open_music_player(): os.system("start vlc")
def close_music_player(): os.system("taskkill /IM vlc.exe /F")
def open_whatsapp(): os.system("start whatsapp")
def close_whatsapp(): os.system("taskkill /IM WhatsApp.exe /F")

actions = {
    "open_browser": open_browser,
    "close_browser": close_browser,
    "open_music_player": open_music_player,
    "close_music_player": close_music_player,
    "open_whatsapp": open_whatsapp,
    "close_whatsapp": close_whatsapp,
}

# Predicción de intención
def get_intent(text):
    vectorized_input = vectorizer([text])
    prediction = model.predict(vectorized_input)
    intent = list(label_mapping.keys())[np.argmax(prediction)]
    return intent

# Integración de voz con ejecución de comandos
def assistant():
    command = escuchar()
    print(f"👤 Tú: {command}")
    if command:
        intent = get_intent(command)
        print(f"🤖 Intención detectada: {intent}")
        actions.get(intent, lambda: print("No entiendo ese comando"))()
        