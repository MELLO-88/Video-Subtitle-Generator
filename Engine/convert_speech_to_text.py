import os
import speech_recognition as sr

def convert_speech_to_text(folder_path):
    # List all WAV files and sort them numerically
    files = sorted(os.listdir(folder_path), key=lambda f: int(f.split('.')[0]))
    converted_texts = []

    recognizer = sr.Recognizer()
    for filename in files:
        if not filename.endswith('.wav'):
            continue
        try:
            with sr.AudioFile(os.path.join(folder_path, filename)) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)
                converted_texts.append(text)
                print(f"Reading - {filename}")
                print(text)
        except Exception as e:
            # Append "error" in case of any exceptions during conversion
            converted_texts.append("error")
            print("error")

    return converted_texts

