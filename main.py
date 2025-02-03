import os
import tensorflow as tf
import numpy as np
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
model = tf.keras.models.load_model("liz/liz_0001.keras")
with open("liz/tokenizer.pickle", "rb") as handle:
    tokenizer = pickle.load(handle)
with open("liz/label_mapping.pickle", "rb") as handle:
    label_mapping = pickle.load(handle)

# Funciones para ejecutar comandos
def open_browser(): os.system("start chrome")
def close_browser(): os.system("taskkill /IM chrome.exe /F")
def open_music_player(): os.system("start vlc")

actions = {
    "open_browser": open_browser,
    "close_browser": close_browser,
    "open_music_player": open_music_player
}

# Predicción de intención
def get_intent(text):
    sequence = tokenizer.texts_to_sequences([text])
    padded = tf.keras.preprocessing.sequence.pad_sequences(sequence, maxlen=model.input_shape[1], padding='post')
    prediction = model.predict(padded)
    intent = list(label_mapping.keys())[np.argmax(prediction)]
    return intent

# Integración de voz con ejecución de comandos
def assistant():
    while True:
        command = escuchar()
        print(f"👤 Tú: {command}")
        if command:
            intent = get_intent(command)
            print(f"🤖 Intención detectada: {intent}")
            actions.get(intent, lambda: print("No entiendo ese comando"))()

assistant()
