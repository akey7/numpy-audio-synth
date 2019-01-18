import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd
import time

f_s = 44100
duration_s = 2.5
f_c = 440.0
f_m = 220.0
k = 50.0

tis = np.arange(duration_s * f_s)
carrier = 2 * np.pi * tis * f_c / f_s
modulator = k * np.sin(2 * np.pi * tis * f_m / f_s)
waveform = np.cos(carrier + modulator)

waveform_quiet = waveform * 0.3
waveform_integers = np.int16(waveform_quiet * 32767)
write('fm-out.wav', f_s, waveform_integers)

sd.play(waveform_quiet, f_s)
time.sleep(duration_s)
sd.stop()
