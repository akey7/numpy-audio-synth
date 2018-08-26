import numpy as np
from scipy.io.wavfile import write

sps = 44100
freq_hz = 440.0
duration_s = 3.0

t_samples = np.arange(sps * duration_s)
waveform = np.sin(2 * np.pi * freq_hz * t_samples / sps)
waveform *= 0.3
waveform_ints = np.int16(waveform * 32767)
write('first_sine.wav', sps, waveform_ints)
