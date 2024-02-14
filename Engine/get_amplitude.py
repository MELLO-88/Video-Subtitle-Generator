import wave
import numpy as np


def get_amplitude(filename):
  with wave.open(filename, 'rb') as wf:
    # Extract Raw Audio from Wav File
    signal = wf.readframes(-1)
    sw = wf.getsampwidth()
    dt = np.int16 if sw == 2 else np.int8
    audio = np.frombuffer(signal, dtype=dt)

    # If stereo, take the mean of the two channels
    if wf.getnchannels() == 2:
      audio = (audio[::2] + audio[1::2]) / 2

    return audio